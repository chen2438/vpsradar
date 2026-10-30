#!/usr/bin/env python3
"""Generate bilingual post share cards. Requires Pillow and a system CJK font."""
import argparse
from functools import lru_cache
import hashlib
import re
import io
import json
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'source/img/cards'
LIMIT = 120_000
# Curated vivid accents: red through pink, with separate warm/cool steps.
PALETTE = ('#FF5252', '#FF852D', '#FFB82E', '#F5E642',
           '#BAE535', '#60D653', '#26CD91', '#2ED5BE',
           '#28D6EC', '#39B6FF', '#648CFF', '#8D78FF',
           '#B56AFF', '#DF58ED', '#FF59B3', '#FF7591')


def font_path():
    result = subprocess.check_output(['fc-list', ':lang=zh', 'file'], text=True)
    fonts = sorted({line.split(':')[0] for line in result.splitlines()})
    if not fonts:
        raise SystemExit('Install a CJK font, e.g. fonts-noto-cjk, or pass --font.')
    return next((p for p in fonts if 'NotoSansCJK-Bold' in p), fonts[0])


def posts():
    # Reuse Hexo's YAML parser, including quoted/multiline titles.
    script = """
const fs = require('node:fs');
const path = require('node:path');
const fm = require('hexo-front-matter');
function walk(dir) {
  return fs.readdirSync(dir, {withFileTypes:true}).flatMap(e => {
    const p = path.join(dir, e.name);
    if(e.isDirectory()) return walk(p);
    if(!p.endsWith('.md')) return [];
    const post = fm.parse(fs.readFileSync(p, 'utf8'));
    return [{slug:path.relative('source/_posts', p).slice(0, -3), title:post.title,
      vendor:Array.isArray(post.categories) ? post.categories[0] : post.categories || path.basename(dir),
      lang:post.lang || (p.endsWith('.en.md') ? 'en' : 'zh-CN'),
      price:post.price, coupon:post.coupon}];
  });
}
const yaml = require('js-yaml');
const vendors = yaml.load(fs.readFileSync('source/_data/vendors.yml', 'utf8')) || {};
process.stdout.write(JSON.stringify(walk('source/_posts').map(post => ({
  ...post, color:vendors[post.vendor]?.color
}))));
"""
    return json.loads(subprocess.check_output(['node', '-e', script], cwd=ROOT, text=True))


def accent_color(post):
    override = post.get('color')
    if override is not None:
        if not isinstance(override, str) or not re.fullmatch(r'#[0-9a-fA-F]{6}', override):
            raise ValueError('Vendor color must be "#RRGGBB": ' + str(post['vendor']))
        return tuple(int(override[i:i + 2], 16) for i in (1, 3, 5))
    bucket = int.from_bytes(hashlib.sha256(str(post['vendor']).encode()).digest()[:8], 'big') % len(PALETTE)
    return tuple(bytes.fromhex(PALETTE[bucket][1:]))


def luminance(rgb):
    linear = [c / 255 / 12.92 if c / 255 <= .04045 else
              ((c / 255 + .055) / 1.055) ** 2.4 for c in rgb]
    return sum(c * w for c, w in zip(linear, (.2126, .7152, .0722)))


def contrast(a, b):
    high, low = sorted((luminance(a), luminance(b)), reverse=True)
    return (high + .05) / (low + .05)


def badge_text_color(accent):
    return max(((0, 0, 0), (255, 255, 255)), key=lambda c: contrast(c, accent))


def label_color(accent):
    # Lift dark manual overrides against the brightest part behind the label.
    color = accent
    while contrast(color, (38, 46, 59)) < 4.5:
        color = tuple(round(c + (255 - c) * .12) for c in color)
    return color


def field_text(value):
    # Optional deal fields are scalar front matter, never body-derived.
    return ' '.join(str(value).split()) if isinstance(value, (str, int, float)) and not isinstance(value, bool) else ''


def badge_lines(post):
    price, coupon = (field_text(post.get(key)) for key in ('price', 'coupon'))
    return ([price] if price else []) + ([('Code ' if post.get('lang') == 'en' else '码 ') + coupon] if coupon else [])


def ellipsize(draw, text, font, width):
    if draw.textlength(text, font=font) <= width:
        return text
    while text and draw.textlength(text.rstrip() + '…', font=font) > width:
        text = text[:-1]
    return text.rstrip() + '…'


# Currency, numbers with units, and Latin words/codes remain indivisible.
CJK = r'\u3400-\u9fff'
TOKEN = re.compile(
    r'[$€¥£]?\d+(?:[.,]\d+)*(?:/(?:[A-Za-z]+|[年月天日季周])(?:起)?)?'
    r'(?:\s*(?:美元|欧元|元|折|%|GB|TB|MB|Mbps|Gbps))?(?:起)?[,:;.!?]?'
    r'(?=$|[\s' + CJK + r'])'
    r'|[^\s' + CJK + r']+|[' + CJK + r']')


def title_tokens(text):
    text = ' '.join(str(text).split())
    tokens, end = [], 0
    for match in TOKEN.finditer(text):
        tokens.append(text[end:match.start()] + match.group())
        end = match.end()
    return tokens


def wrap(draw, text, font, width, max_lines):
    tokens = title_tokens(text)
    # An oversized indivisible token gets an ellipsis, never a continuation line.
    clipped = any(draw.textlength(t.strip(), font=font) > width for t in tokens)
    tokens = [ellipsize(draw, t, font, width) for t in tokens]
    n = len(tokens)

    solutions = {n: (0, 0, [])}
    for start in range(n - 1, -1, -1):
        best = None
        for end in range(start + 1, n + 1):
            line = ''.join(tokens[start:end]).strip()
            length = draw.textlength(line, font=font)
            if length > width:
                break
            count, cost, rest = solutions[end]
            # First minimise line count, then balance widths. Penalise orphan
            # final words/characters whenever an alternative break is possible.
            orphan = end == n and end - start == 1 and start > 0
            candidate = (1 + count, cost + (width - length) ** 2 + orphan * width ** 2 * 10,
                         [line] + rest)
            if best is None or candidate[:2] < best[:2]:
                best = candidate
        solutions[start] = best

    lines = solutions[0][2]
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        # Remove whole tokens to make space for the truncation marker.
        tail = title_tokens(lines[-1])
        while tail and draw.textlength(''.join(tail).rstrip() + '…', font=font) > width:
            tail.pop()
        lines[-1] = ''.join(tail).rstrip() + '…'
    elif clipped and lines and not lines[-1].endswith('…'):
        lines[-1] = ellipsize(draw, lines[-1] + '…', font, width)
    return lines


@lru_cache(maxsize=32)
def background(accent):
    image = Image.new('RGB', (1200, 630))
    pixels = image.load()
    for y in range(630):
        for x in range(1200):
            glow = max(0, 1 - ((x - 1050) ** 2 + (y - 80) ** 2) ** .5 / 1100) * .48
            pixels[x, y] = tuple(round(base + (c - base) * glow)
                                 for base, c in zip((12, 20, 35), accent))
    return image


def render(post, font):
    accent = accent_color(post)
    image = background(accent).copy()
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 19, 629), fill=accent)
    vendor_font = ImageFont.truetype(font, 32)
    draw.text((64, 80), ellipsize(draw, str(post['vendor']).upper(), vendor_font, 1060),
              font=vendor_font, fill=label_color(accent), anchor='lt')
    badges = badge_lines(post)
    title_font = ImageFont.truetype(font, 52)
    lines = wrap(draw, post['title'], title_font, 1060, 2 if badges else 4)
    for i, line in enumerate(lines):
        draw.text((64, 156 + i * 72), line, font=title_font, fill='#f3f7fc', anchor='lt')
    if badges:
        top = 348 if len(badges) == 2 else 412
        draw.rounded_rectangle((64, top, 1136, 514), radius=18, fill=accent)
        for i, text in enumerate(badges):
            badge_font = ImageFont.truetype(font, 42 if i == 0 else 36)
            draw.text((88, top + 23 + i * 68), ellipsize(draw, text, badge_font, 1024),
                      font=badge_font, fill=badge_text_color(accent), anchor='lt')
    draw.line((64, 544, 1136, 544), fill='#35475d', width=2)
    draw.text((64, 565), 'VPS Radar', font=ImageFont.truetype(font, 30), fill='#f3f7fc', anchor='lt')
    draw.text((780, 572), 'vpsradar.vayki.com', font=ImageFont.truetype(font, 22), fill='#a5b8ca', anchor='lt')
    for quality in range(90, 19, -5):
        output = io.BytesIO()
        image.save(output, 'JPEG', quality=quality, optimize=True, progressive=True)
        if output.tell() <= LIMIT:
            thumbnail = io.BytesIO()
            image.resize((600, 315), Image.Resampling.LANCZOS).save(
                thumbnail, 'WEBP', quality=80, method=6)
            if thumbnail.tell() > 30_000:
                raise ValueError('Could not meet thumbnail budget: ' + post['slug'])
            return output.getvalue(), thumbnail.getvalue()
    raise ValueError('Could not meet JPEG budget: ' + post['slug'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--font', help='Path to a CJK-capable TTF/OTF/TTC font')
    args = parser.parse_args()
    font = args.font or font_path()
    OUT.mkdir(parents=True, exist_ok=True)
    entries = posts()
    slugs = [p['slug'] for p in entries]
    if len(slugs) != len(set(slugs)):
        raise SystemExit('Duplicate post file slugs; choose unique filenames before generating cards.')
    for post in entries:
        jpeg, thumbnail = render(post, font)
        for suffix, data in [('.jpg', jpeg), ('.webp', thumbnail)]:
            target = OUT / (post['slug'] + suffix)
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists() or target.read_bytes() != data:
                target.write_bytes(data)
    print(f'Generated {len(entries)} JPEG cards (1200x630, <=120KB each) and WebP covers '
          f'(600x315, <=30KB each) with {font}.')


if __name__ == '__main__':
    main()
