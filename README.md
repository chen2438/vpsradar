# VPS Radar

Hexo 8 + Butterfly, deployed on Vercel. Dependencies are already installed.
The site uses `Asia/Singapore` for dates.

## Adding bilingual posts

Chinese is the default language and keeps its existing URLs. English lives under
`/en/`. Each language has independent post lists, pagination, tags, categories,
archives and theme UI. Feeds and the sitemap are language aware.

1. Create the Chinese post at `source/_posts/<vendor>/<slug>.md` as usual.
   Do not rename an existing Chinese file or change its permalink.
2. Create its translation alongside it as `<slug>.en.md` with `lang: en`.
   Set `translation_key` to `<vendor>/<slug>` (no extension). The key is optional
   when following this filename convention, but making it explicit is recommended.
3. Copy `date` and `updated` **verbatim**, including blank `updated` values. Translate
   the title, description, body, disclaimer and source labels. Preserve every URL,
   code, product name, specification, price and date. Chinese discount notation
   must be expressed correctly in English: e.g. 6折 = 40% off, not 60% off.
4. Keep vendor category identifiers (e.g. `rfchost`) in both versions. Use the
   English tag names in [i18n-taxonomy.json](i18n-taxonomy.json). When adding a new
   Chinese tag, add its English equivalent there and use that exact name in the
   English front matter. Hexo generates tag paths from those names (spaces become
   hyphens); existing Chinese tag paths remain unchanged.
5. Build and check:

   ```sh
   npx hexo clean && npx hexo generate
   python3 tools/check-i18n.py
   # Optional comparison against a saved pre-change build:
   python3 tools/check-i18n.py /workspace/public-before
   ```

Chinese example (`source/_posts/rfchost/example-deal.md`):

```yaml
---
title: RFCHost 优惠
date: 2026-10-27 19:47:45
updated: 2026-10-27 19:47:45
categories:
- rfchost
tags:
- 香港VPS
cover: /img/default-cover-v2.webp
description: 优惠详情
copyright: false
---
```

English example (`source/_posts/rfchost/example-deal.en.md`):

```yaml
---
title: RFCHost Deal
date: 2026-10-27 19:47:45
updated: 2026-10-27 19:47:45
lang: en
translation_key: rfchost/example-deal
categories:
- rfchost
tags:
- Hong Kong VPS
cover: /img/default-cover-v2.webp
description: Deal details
copyright: false
---
```

These generate `/rfchost/example-deal/` and `/en/rfchost/example-deal/`.
Chinese posts may optionally declare the same `translation_key`. A Chinese-only
post or an English-only post also builds; its switcher links to the other
language's home. For a Chinese post with a custom permalink, copy that path with
an `en/` prefix into the English post's `permalink` field. The translation key
still pairs the two posts even when their filenames or paths differ.

Ordinary pages go in `source/<path>/index.md` and
`source/en/<path>/index.md` (`lang: en` on the latter). The tags/categories index
pages and English 404 are generated automatically. There are currently no about
or links pages. Ordinary pages pair by path; a missing opposite path falls back
to the other home. Posts pair by translation key.

## How language support works

[scripts/i18n.js](scripts/i18n.js) wraps the existing post, index, archive,
category and tag generators with language-scoped collections. It also scopes
post taxonomies, related posts, previous/next posts, sidebar counts and Butterfly
fragment caches. English permalinks default to `en/<translation_key>/`.
When a paired Chinese post exists, the English rendered update timestamp uses
that post's timestamp, including Hexo's file-mtime fallback for blank values.

The root metadata stays in `_config.yml`; English overrides are under `english`.
`_config.butterfly.yml` contains the existing Chinese `menu` and a separate
`menu_en`. Butterfly's bundled `zh-CN` and `en` dictionaries provide UI text;
the script also translates the configured out-of-date notice. Search remains
at its existing disabled setting; its theme UI uses the current language if
configured later (a search index would also need language scoping).

The small Butterfly template changes add the always-visible switcher, use the
page language on `<html>`, keep logo/home links in the current language and emit
canonical/hreflang links. Alternates are emitted only for existing translations,
with `x-default` pointing to the Chinese counterpart (or Chinese home when none
exists). No nonexistent translation is advertised to search engines.

Cloudflare Web Analytics, Vercel Web Analytics and busuanzi remain enabled in
both languages. No runtime translation service is used.


## Phase 1 technical SEO

- `/sitemap.xml` is generated in `scripts/i18n.js` from real routes: Chinese
  URLs stay unchanged and English URLs stay under `/en/`. It includes posts,
  home, archive root and taxonomy indexes. Taxonomy detail and archive year/month
  pages require **at least two posts in that language**. Only page 1 of each list
  is included; pagination and thin lists remain accessible. Paired included pages advertise
  `zh-CN`, `en` and `x-default` (Chinese) alternates. Last modification uses the
  explicit front-matter `updated`, falling back to `date` when absent or blank,
  or the maximum member timestamp for lists in that language. Sitemap dates
  never use file mtime or build time. The unused stock sitemap plugin
  was removed in favor of this generator.
- `/atom.xml` contains Chinese posts; `/en/atom.xml` contains English posts.
  `hexo-generator-feed` uses the same scoped collections, all posts and full HTML
  content. Publish dates come from each post's original `date` front matter,
  parsed in `Asia/Singapore`; update dates follow the bilingual pairing rules.
  Both feeds are discoverable in the theme head, current language first.
- `source/robots.txt` is copied verbatim via `skip_render` and advertises the
  absolute sitemap URL at `https://vpsradar.vayki.com`.
- `vercel.json` gives `/css/*`, `/js/*`, `/img/*`, and `/fonts/*` one year of
  immutable caching. HTML retains Vercel's default behavior. Assets changed in
  future releases must use a new filename/version to avoid stale caches.
- New `v2` images provide a 32px favicon, 180px Apple icon, 128px WebP logo/avatar,
  WebP default cover and padded 1200×630 JPEG social image. Custom vendor covers
  keep their existing social images. Old `favicon.png` and `default.png` URLs
  remain available as small PNG replacements. Full originals live under
  `tools/original-img/`, outside Hexo's published source directory.

Regenerate the images with Pillow (including WebP support), then rebuild and check:

```sh
python3 tools/optimize-images.py
npx hexo clean && npx hexo generate
python3 tools/check-i18n.py
python3 tools/check-seo.py
```
