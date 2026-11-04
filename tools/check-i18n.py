#!/usr/bin/env python3
"""Offline build checks. Run after Hexo generation; optional saved-build path."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'public'
ORIGIN = 'https://vpsradar.vayki.com'


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.lang = None
        self.links = []
        self.switches = []
        self.times = []
        self.anchors = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.lang = attrs.get('lang')
        if tag == 'link':
            self.links.append(attrs)
        if tag == 'a':
            self.anchors.append(attrs)
            if attrs.get('id') == 'language-switcher':
                self.switches.append(attrs)
        if tag == 'time':
            self.times.append(attrs.get('datetime'))


def file_for(url):
    path = unquote(urlsplit(url).path).lstrip('/')
    return PUBLIC / (path + 'index.html' if not Path(path).suffix else path)


def frontmatter(text, key):
    match = re.search(r'^' + key + r':(.*)$', text.split('---', 2)[1], re.M)
    return match[1] if match else None


pages = {}
for path in PUBLIC.rglob('*.html'):
    rel = path.relative_to(PUBLIC).as_posix()
    text = path.read_text()
    page = pages[rel] = Page(text)
    english = rel.startswith('en/')
    assert page.lang == ('en' if english else 'zh-CN'), rel
    canonical = [link['href'] for link in page.links if link.get('rel') == 'canonical']
    assert canonical == [ORIGIN + '/' + rel.removesuffix('index.html')], (rel, canonical)
    alternates = {link['hreflang']: link['href'] for link in page.links if 'hreflang' in link}
    assert 'x-default' in alternates, rel
    assert alternates[page.lang] == canonical[0], rel
    for target in alternates.values():
        assert file_for(target).is_file(), (rel, target)
    assert len(page.switches) == 1, rel
    switch = page.switches[0]['href']
    assert file_for(switch).is_file(), (rel, switch)
    assert switch.startswith('/en/') != english, (rel, switch)
    for marker in ['static.cloudflareinsights.com/beacon.min.js', '/_vercel/insights/script.js', 'https://events.vercount.one/js']:
        assert marker in text, (rel, marker)
    assert 'busuanzi.ibruce.info' not in text, rel
    assert 'busuanzi_value_' in text or rel.endswith('404.html'), rel
    # All same-site page links should resolve, including menu, sidebar, related
    # posts, taxonomy and pagination links. Ignore external services and assets.
    for anchor in page.anchors:
        href = anchor.get('href', '')
        url = urlsplit(href)
        if url.netloc and url.netloc != 'vpsradar.vayki.com':
            continue
        if not url.path.startswith('/') or url.path.startswith('/_vercel/'):
            continue
        if url.path.endswith('/') or url.path.endswith('.html'):
            assert file_for(href).is_file(), (rel, href)
            if anchor.get('id') != 'language-switcher':
                assert url.path.startswith('/en/') == english, ('Language leaked into navigation', rel, href)
    # A real counterpart has a reciprocal switcher and alternate, not a home
    # fallback posing as a translation.
    other_language = 'zh-CN' if english else 'en'
    if other_language in alternates:
        other = Page(file_for(alternates[other_language]).read_text())
        assert other.switches[0]['href'] == urlsplit(canonical[0]).path, rel

originals = [p for p in (ROOT / 'source/_posts').rglob('*.md') if not p.name.endswith('.en.md')]
paired = 0
for original in originals:
    english = original.with_suffix('.en.md')
    if not english.exists():
        continue
    zh, en = original.read_text(), english.read_text()
    assert frontmatter(en, 'lang') == ' en', english
    for field in ['date', 'updated']:
        assert frontmatter(zh, field) == frontmatter(en, field), (english, field)
    zh_body, en_body = zh.split('---', 2)[2], en.split('---', 2)[2]
    urls = lambda value: Counter(re.findall(r'https?://[^\s<>）)]+', value))
    assert urls(zh_body) == urls(en_body), ('URLs changed', english)
    # Numeric data in benchmarks must remain exact and in the same order.
    for a, b in zip(zh_body.split('```')[1::2], en_body.split('```')[1::2]):
        numbers = lambda value: re.findall(r'\d+(?:[.,]\d+)*', value)
        # Section numbers translated from Chinese are not measured data.
        b = re.sub(r'^\s*[1-7]\s*[.、]', '', b, flags=re.M)
        assert numbers(a) == numbers(b), ('Benchmark data changed', english)
    rel = original.relative_to(ROOT / 'source/_posts').with_suffix('').as_posix()
    zh_page, en_page = pages[rel + '/index.html'], pages['en/' + rel + '/index.html']
    assert zh_page.times == en_page.times, ('Rendered timestamps differ', english)
    paired += 1

# Unpaired posts are supported; their switchers were checked above.
if len(sys.argv) > 1:
    baseline = Path(sys.argv[1])
    missing = [str(p.relative_to(baseline)) for p in baseline.rglob('*') if p.is_file() and not (PUBLIC / p.relative_to(baseline)).is_file()]
    assert not missing, ('Old output files missing', missing)
    for old in baseline.rglob('*.html'):
        new = PUBLIC / old.relative_to(baseline)
        old_page, new_page = Page(old.read_text()), Page(new.read_text())
        assert old_page.times == new_page.times, ('Chinese dates changed', old)
        post_links = lambda page: [a.get('href') for a in page.anchors if any(c in a.get('class', '').split() for c in ['article-title', 'article-sort-item-title'])]
        assert post_links(old_page) == post_links(new_page), ('Chinese post list changed', old)
    print(f'Preserved all {sum(p.is_file() for p in baseline.rglob("*"))} baseline files.')
print(f'Checked {len(pages)} HTML pages and {paired} translated posts: routes, links, languages, SEO, analytics, dates, URLs and benchmark data passed.')

import json
import xml.etree.ElementTree as ET
sitemap_urls = {node.text for node in ET.parse(PUBLIC / 'sitemap.xml').iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
for prefix, language in [('', 'zh-CN'), ('en/', 'en')]:
    vendor_path = prefix + 'vendors/index.html'
    assert pages[vendor_path].lang == language
    assert ORIGIN + '/' + prefix + 'vendors/' in sitemap_urls
    rows = json.loads((PUBLIC / prefix / 'search-v4.json').read_text())
    assert len(rows) == len([p for p in (ROOT / 'source/_posts').rglob('*.md') if p.name.endswith('.en.md') == bool(prefix)])
    assert all(row['url'].startswith('/en/') == bool(prefix) and file_for(row['url']).is_file() for row in rows)
    assert all(set(row) == {'title', 'description', 'url'} for row in rows)
for original in originals:
    rel = original.relative_to(ROOT / 'source/_posts').with_suffix('').as_posix()
    for prefix in ['', 'en/']:
        html = (PUBLIC / prefix / rel / 'index.html').read_text()
        assert 'class="vendor-related"' in html
        assert 'More deals from this vendor' in html if prefix else '同商家其他优惠' in html
js = (PUBLIC / 'js/deals-v4.js').read_text()
assert "addEventListener('focus', search)" in js and 'fetch(input.dataset.index)' in js
assert 'preload' not in js
assert (PUBLIC / 'js/deals-v4.js').stat().st_size < 2500
assert (PUBLIC / 'css/deals-v4.css').stat().st_size < 2500
print('Checked bilingual vendors, related deals, separate search indexes and lazy-loading asset budgets.')
