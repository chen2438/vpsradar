#!/usr/bin/env python3
"""Generate bilingual post share cards. Requires Pillow and a system CJK font."""
import argparse
import io
import json
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'source/img/cards'
LIMIT = 120_000


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
      vendor:Array.isArray(post.categories) ? post.categories[0] : post.categories || path.basename(dir)}];
  });
}
process.stdout.write(JSON.stringify(walk('source/_posts')));
"""
    return json.loads(subprocess.check_output(['node', '-e', script], cwd=ROOT, text=True))


def wrap(draw, text, font, width):
    # Prefer word boundaries for Latin text, permit breaks at CJK characters.
    import re
    tokens = re.findall(r'[A-Za-z0-9]+(?:[./%+$-][A-Za-z0-9]+)*\s*|.', text)
    lines, line = [], ''
    for token in tokens:
        if draw.textlength(line + token, font=font) > width and line:
            lines.append(line.rstrip())
            line = ''
        line += token
    if line:
        lines.append(line.rstrip())
    return lines


def render(post, font):
    image = Image.new('RGB', (1200, 630))
    pixels = image.load()
    for y in range(630):
        for x in range(1200):
            glow = max(0, 1 - ((x - 1050) ** 2 + (y - 80) ** 2) ** .5 / 1000)
            pixels[x, y] = (int(12 + glow * 8), int(20 + glow * 25), int(35 + glow * 38))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((64, 60, 136, 66), radius=3, fill='#56d7eb')
    draw.text((64, 92), str(post['vendor']).upper(), font=ImageFont.truetype(font, 30), fill='#56d7eb')
    for size in range(54, 19, -2):
        title_font = ImageFont.truetype(font, size)
        lines = wrap(draw, post['title'], title_font, 1060)
        if len(lines) * (size + 16) <= 320:
            break
    for i, line in enumerate(lines):
        draw.text((64, 176 + i * (size + 16)), line, font=title_font, fill='#f3f7fc')
    draw.line((64, 534, 1136, 534), fill='#35475d', width=2)
    draw.text((64, 555), 'VPS Radar', font=ImageFont.truetype(font, 30), fill='#f3f7fc')
    draw.text((780, 564), 'vpsradar.vayki.com', font=ImageFont.truetype(font, 22), fill='#a5b8ca')
    for quality in range(90, 19, -5):
        output = io.BytesIO()
        image.save(output, 'JPEG', quality=quality, optimize=True, progressive=True)
        if output.tell() <= LIMIT:
            return output.getvalue()
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
        data = render(post, font)
        target = OUT / (post['slug'] + '.jpg')
        target.parent.mkdir(parents=True, exist_ok=True)
        if not target.exists() or target.read_bytes() != data:
            target.write_bytes(data)
    print(f'Generated {len(entries)} cards with {font} (1200x630, <=120KB each).')


if __name__ == '__main__':
    main()
