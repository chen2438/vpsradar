#!/usr/bin/env python3
"""Focused card regressions: optional metadata, overflow, colors and glyph coverage."""
import importlib.util
import subprocess
import sys
import unittest
from PIL import Image, ImageDraw, ImageFont

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('cards', 'tools/generate-cards.py')
cards = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cards)


class CardsTest(unittest.TestCase):
    def setUp(self):
        self.font_path = cards.font_path()
        self.font = ImageFont.truetype(self.font_path, 42)
        self.draw = ImageDraw.Draw(Image.new('RGB', (1200, 630)))

    def test_fields_and_localization(self):
        self.assertEqual(cards.badge_lines({'title': '$99 coupon FAKE', 'body': 'Code FAKE'}), [])
        self.assertEqual(cards.badge_lines({'price': '$12.99/月起', 'coupon': 'LETYEARLY'}),
                         ['$12.99/月起', '码 LETYEARLY'])
        self.assertEqual(cards.badge_lines({'lang': 'en', 'coupon': 'LETYEARLY'}), ['Code LETYEARLY'])
        self.assertEqual(cards.badge_lines({'price': 0, 'coupon': None}), ['0'])
        self.assertEqual(cards.badge_lines({'price': [], 'coupon': '  '}), [])

    def test_overflow(self):
        for text in ['长标题优惠码' * 100, 'UnbrokenCoupon' * 100, 'Long English title ' * 100]:
            lines = cards.wrap(self.draw, text, self.font, 1060, 2)
            self.assertEqual(len(lines), 2)
            self.assertTrue(lines[-1].endswith('…'))
            self.assertTrue(all(self.draw.textlength(line, font=self.font) <= 1060 for line in lines))
            badge = cards.ellipsize(self.draw, text, self.font, 1024)
            self.assertTrue(badge.endswith('…'))
            self.assertLessEqual(self.draw.textlength(badge, font=self.font), 1024)

    def test_colors(self):
        self.assertEqual(cards.accent_color({'vendor': 'vpb'}), cards.accent_color({'vendor': 'vpb'}))
        self.assertEqual(cards.accent_color({'vendor': 'vpb', 'color': '#123aBC'}), (18, 58, 188))
        self.assertNotEqual(cards.accent_color({'vendor': 'vpb'}), cards.accent_color({'vendor': 'serverhost'}))
        self.assertGreater(min(cards.label_color((0, 0, 0))), 150)
        with self.assertRaises(ValueError):
            cards.accent_color({'vendor': 'test', 'color': 'red'})

    def test_font_coverage(self):
        # Fontconfig reports actual cmap coverage, not just successful Pillow loading.
        ranges = subprocess.check_output(['fc-query', '--index', '0', '--format', '%{charset}', self.font_path], text=True)
        coverage = [tuple(int(v, 16) for v in token.split('-')) for token in ranges.split()]
        for char in '$€¥/%…码月起优惠Code LETYEARLY':
            self.assertTrue(any(r[0] <= ord(char) <= r[-1] for r in coverage), repr(char))


if __name__ == '__main__':
    unittest.main()
