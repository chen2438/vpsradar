#!/usr/bin/env python3
"""Rebuild v2 site images with Pillow; originals are never published by Hexo."""
from pathlib import Path
from shutil import copy2
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'source/img'
ORIGINAL = ROOT / 'tools/original-img'
ORIGINAL.mkdir(exist_ok=True)
for name in ('favicon.png', 'default.png'):
    if not (ORIGINAL / name).exists():
        copy2(OUT / name, ORIGINAL / name)

icon = Image.open(ORIGINAL / 'favicon.png').convert('RGBA')
cover = Image.open(ORIGINAL / 'default.png').convert('RGBA')
def png(im, name, size):
    im.resize(size, Image.Resampling.LANCZOS).save(OUT / name, optimize=True)

def rgb(im):
    # Match the artwork's upper-left background, preserving transparent artwork.
    bg = Image.new('RGB', im.size, im.getpixel((0, 0))[:3])
    bg.paste(im, mask=im.getchannel('A'))
    return bg

png(icon, 'favicon-32-v2.png', (32, 32))
png(icon, 'apple-touch-icon-v2.png', (180, 180))
icon.resize((128, 128), Image.Resampling.LANCZOS).save(OUT / 'logo-v2.webp', quality=85, method=6)
cover.save(OUT / 'default-cover-v2.webp', quality=80, method=6)
canvas = Image.new('RGB', (1200, 630), rgb(icon).getpixel((0, 0)))
art = ImageOps.contain(rgb(icon), (630, 630), Image.Resampling.LANCZOS)
canvas.paste(art, ((1200-art.width)//2, (630-art.height)//2))
canvas.save(OUT / 'og-default-v2.jpg', quality=85, optimize=True, progressive=True)
# Compatibility URLs stay available, with smaller valid PNG contents.
png(icon, 'favicon.png', (128, 128))
rgb(cover).quantize(colors=128).save(OUT / 'default.png', optimize=True)
for name, limit in [('logo-v2.webp', 20000), ('default-cover-v2.webp', 60000), ('og-default-v2.jpg', 100000)]:
    size = (OUT / name).stat().st_size
    assert size <= limit, (name, size, limit)
for name in ['favicon.png', 'default.png', 'favicon-32-v2.png', 'apple-touch-icon-v2.png', 'logo-v2.webp', 'default-cover-v2.webp', 'og-default-v2.jpg']:
    print(f'{name}: {(OUT / name).stat().st_size:,} bytes')
