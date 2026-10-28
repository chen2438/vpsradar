#!/usr/bin/env python3
"""Offline checks for the generated bilingual sitemap, feeds and image references."""
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from zoneinfo import ZoneInfo
import json
import re
import xml.etree.ElementTree as ET
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'public'
ORIGIN = 'https://vpsradar.vayki.com'
NS = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9',
      'h': 'http://www.w3.org/1999/xhtml', 'a': 'http://www.w3.org/2005/Atom'}

def local_file(url):
    path = unquote(urlsplit(url).path).lstrip('/')
    return PUBLIC / (path + 'index.html' if not Path(path).suffix else path)

def timestamp(value):
    return datetime.fromisoformat(value.replace('Z', '+00:00'))

sitemap = ET.parse(PUBLIC / 'sitemap.xml').getroot()
assert sitemap.tag == '{' + NS['s'] + '}urlset'
assert ('start-ns', ('xhtml', NS['h'])) in list(ET.iterparse(PUBLIC / 'sitemap.xml', events=['start-ns']))
urls = {}
for record in sitemap:
    loc = record.findtext('s:loc', namespaces=NS)
    assert loc.startswith(ORIGIN + '/') and 'index.html' not in loc, loc
    assert not re.search(r'/page/\d+/', unquote(urlsplit(loc).path)), loc
    assert loc not in urls and local_file(loc).is_file(), loc
    urls[loc] = record
    timestamp(record.findtext('s:lastmod', namespaces=NS))
for loc, record in urls.items():
    alternates = {a.attrib['hreflang']: a.attrib['href'] for a in record.findall('h:link', NS)}
    if alternates:
        assert set(alternates) == {'zh-CN', 'en', 'x-default'}, loc
        assert alternates['x-default'] == alternates['zh-CN'], loc
        for lang, target in alternates.items():
            assert target in urls, (loc, target)
            reciprocal = {a.attrib['hreflang']: a.attrib['href'] for a in urls[target].findall('h:link', NS)}
            assert reciprocal == alternates, (loc, reciprocal)

post_urls = {}
term_counts = {}
expected_lastmods = {}
for lang, path in [('zh-CN', 'atom.xml'), ('en', 'en/atom.xml')]:
    feed = ET.parse(PUBLIC / path).getroot()
    assert feed.attrib['{http://www.w3.org/XML/1998/namespace}lang'] == lang
    links = {link.attrib.get('rel'): link.attrib['href'] for link in feed.findall('a:link', NS)}
    assert links['self'] == ORIGIN + '/' + path
    assert links['alternate'] == ORIGIN + ('/en/' if lang == 'en' else '/')
    assert local_file(feed.findtext('a:icon', namespaces=NS)).is_file()
    entries = feed.findall('a:entry', NS)
    assert len(entries) == 46, (lang, len(entries))
    post_urls[lang] = set()
    sources = [p for p in (ROOT / 'source/_posts').rglob('*.md') if p.name.endswith('.en.md') == (lang == 'en')]
    dates = {}
    updates = {}
    for source in sources:
        front = source.read_text().split('---', 2)[1]
        title = re.search(r'^title:\s*(.+)$', front, re.M)[1].strip().strip("'\"")
        date = re.search(r'^date:\s*(.+)$', front, re.M)[1].strip().strip("'\"")
        def content_date(value):
            parsed = datetime.fromisoformat(value)
            return parsed if parsed.tzinfo else parsed.replace(tzinfo=ZoneInfo('Asia/Singapore'))
        dates[title] = content_date(date)
        updated = re.search(r'^updated:[ \t]*([^\n]*)$', front, re.M)
        value = updated[1].strip().strip("'\"") if updated else ''
        updates[title] = content_date(value) if value and value not in ('null', '~') else dates[title]
    members = {}
    for entry in entries:
        url = entry.findtext('a:id', namespaces=NS)
        assert url in urls and ('/en/' in url) == (lang == 'en'), url
        post_urls[lang].add(url)
        for category in entry.findall('a:category', NS):
            scheme = category.attrib['scheme']
            term_counts[scheme] = term_counts.get(scheme, 0) + 1
        title = entry.findtext('a:title', namespaces=NS)
        expected_lastmods[url] = updates[title]
        members[url] = (dates[title], updates[title])
        for category in entry.findall('a:category', NS):
            term = category.attrib['scheme']
            expected_lastmods[term] = max(expected_lastmods.get(term, updates[title]), updates[title])
        assert timestamp(entry.findtext('a:published', namespaces=NS)) == dates[title], title
        timestamp(entry.findtext('a:updated', namespaces=NS))
        content = entry.find('a:content', NS)
        assert content.attrib['type'] == 'html' and len(content.text) > 100, title
        assert len(urls[url].findall('h:link', NS)) == 3, url
    assert len(post_urls[lang]) == 46
    root = ORIGIN + ('/en/' if lang == 'en' else '/')
    latest = max(updated for date, updated in members.values())
    for suffix in ['', 'tags/', 'categories/', 'archives/']:
        expected_lastmods[root + suffix] = latest
    archives = {}
    for date, updated in members.values():
        for suffix in [date.strftime('%Y/'), date.strftime('%Y/%m/')]:
            archives.setdefault(root + 'archives/' + suffix, []).append(updated)
    for archive, updates_in_archive in archives.items():
        assert (archive in urls) == (len(updates_in_archive) >= 2), archive
        if len(updates_in_archive) >= 2:
            expected_lastmods[archive] = max(updates_in_archive)

for term, count in term_counts.items():
    assert (term in urls) == (count >= 2), (term, count)
    if count < 2:
        expected_lastmods.pop(term)
assert urls.keys() == expected_lastmods.keys(), (urls.keys() - expected_lastmods.keys(), expected_lastmods.keys() - urls.keys())
for loc, record in urls.items():
    assert timestamp(record.findtext('s:lastmod', namespaces=NS)) == expected_lastmods[loc], loc
for lang, posts in post_urls.items():
    root = ORIGIN + ('/en/' if lang == 'en' else '/')
    for path in ['', 'tags/', 'categories/', 'archives/']:
        assert root + path in urls, root + path
    assert len(posts & urls.keys()) == 46

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.images, self.meta = [], [], []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'link':
            self.links.append(attrs)
            if attrs.get('rel') in ('icon', 'apple-touch-icon'):
                self.images.append(attrs['href'])
        if tag == 'img':
            self.images.append(attrs.get('src', ''))
            if attrs.get('data-lazy-src'):
                self.images.append(attrs['data-lazy-src'])
        if tag == 'meta':
            self.meta.append(attrs)
            if attrs.get('property') == 'og:image' or attrs.get('name') == 'twitter:image':
                self.images.append(attrs['content'])

count = 0
for file in PUBLIC.rglob('*.html'):
    page = Page(file.read_text())
    english = file.relative_to(PUBLIC).as_posix().startswith('en/')
    feeds = [a for a in page.links if a.get('type') == 'application/atom+xml']
    assert [a['href'] for a in feeds] == (['/en/atom.xml', '/atom.xml'] if english else ['/atom.xml', '/en/atom.xml']), file
    assert any(a.get('rel') == 'apple-touch-icon' for a in page.links), file
    assert any(a.get('property') == 'og:image' for a in page.meta), file
    assert any(a.get('name') == 'twitter:image' for a in page.meta), file
    for image in page.images:
        if not image or image.startswith(('data:', '//')):
            continue
        target = urljoin(ORIGIN + '/' + file.relative_to(PUBLIC).as_posix(), image)
        if urlsplit(target).netloc == urlsplit(ORIGIN).netloc:
            assert local_file(target).is_file(), (file, image)
            assert urlsplit(target).path not in ['/img/favicon.png', '/img/default.png'], (file, image)
    count += 1
assert (PUBLIC / 'robots.txt').read_bytes() == (ROOT / 'source/robots.txt').read_bytes()
assert (PUBLIC / 'robots.txt').read_text() == 'User-agent: *\nAllow: /\nSitemap: ' + ORIGIN + '/sitemap.xml\n'
for name, size, limit in [('favicon-32-v2.png', (32, 32), 20000),
                          ('apple-touch-icon-v2.png', (180, 180), 100000),
                          ('logo-v2.webp', (128, 128), 20000),
                          ('default-cover-v2.webp', (560, 423), 60000),
                          ('og-default-v2.jpg', (1200, 630), 100000)]:
    path = PUBLIC / 'img' / name
    assert Image.open(path).size == size and path.stat().st_size <= limit, name
vercel = json.loads((ROOT / 'vercel.json').read_text())
assert set(vercel) == {'headers'}
print(f'Checked {len(urls)} sitemap URLs, 46 zh + 46 en feed entries, {count} page heads and local image references, robots, image budgets and cache configuration.')
