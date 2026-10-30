#!/usr/bin/env python3
"""Report cold-cache image payloads referenced by generated zh/en home HTML.

Count each local img src (or data-lazy-src) once, including the logo/avatar.
Exclude metadata-only social images and onerror fallbacks; report file bytes,
without HTTP headers or compression. Run after hexo generate.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'public'


class Images(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.images = set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return
        attrs = dict(attrs)
        src = attrs.get('data-lazy-src') or attrs.get('src', '')
        if src.startswith('/') and not src.startswith('//'):
            self.images.add(unquote(urlsplit(src).path).lstrip('/'))


report = {}
for relative in ['index.html', 'en/index.html']:
    images = Images((PUBLIC / relative).read_text()).images
    sizes = {src: (PUBLIC / src).stat().st_size for src in sorted(images)}
    report[relative] = {'unique_image_bytes': sum(sizes.values()), 'images': sizes}
report['cards'] = {}
for suffix in ['jpg', 'webp']:
    cards = list((ROOT / 'source/img/cards').rglob('*.' + suffix))
    report['cards'][suffix] = {'count': len(cards), 'bytes': sum(p.stat().st_size for p in cards)}
print(json.dumps(report, indent=2))
