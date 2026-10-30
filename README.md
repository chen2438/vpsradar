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
5. Regenerate cards, build and check:

   ```sh
   python3 tools/generate-cards.py
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
the script also translates the configured out-of-date notice. Local search uses separate language indexes, fetched only on first search focus.

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
  home, vendor and taxonomy indexes. Taxonomy detail pages require **at least three
  posts in that language**. Archives and pagination are excluded and emit
  `noindex,follow`, as do thinner taxonomy pages. Paired included pages advertise
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
  WebP default cover and padded 1200×630 JPEG social image. Post social images
  use the per-post cards described in phase 3 below. Old `favicon.png` and
  `default.png` URLs
  remain available as small PNG replacements. Full originals live under
  `tools/original-img/`, outside Hexo's published source directory.

Regenerate the images with Pillow (including WebP support), then rebuild and check:

```sh
python3 tools/optimize-images.py
npx hexo clean && npx hexo generate
python3 tools/check-i18n.py
python3 tools/check-seo.py
```

## IndexNow

[IndexNow](https://www.indexnow.org/documentation) notifies participating search
engines when URLs are added or updated. The ownership key is in
`source/e40d982adb11c40759f947a7a287d1e3.txt`; Hexo copies it unchanged to the
site root via `skip_render`. This static file is excluded from the sitemap.

Run the Python 3 stdlib script manually **after the deployment is live**, so
search engines can fetch the new pages and the key file. For newly published
posts, put one absolute URL per line in `new-urls.txt`, including both Chinese
and English URLs as applicable:

```sh
python3 tools/indexnow.py --urls-from-file new-urls.txt --dry-run
python3 tools/indexnow.py --urls-from-file new-urls.txt
```

Without `--urls-from-file`, the script reads every URL (zh + en) from the locally
generated `public/sitemap.xml`. An optional positional argument accepts another
sitemap path or URL:

```sh
python3 tools/indexnow.py --dry-run
python3 tools/indexnow.py https://vpsradar.vayki.com/sitemap.xml --dry-run
```

`--dry-run` prints the count and first five URLs without contacting IndexNow
(a remote sitemap still needs to be fetched). Submissions are deduplicated and
sent in batches of up to 10,000 URLs. HTTP 200/202 means success (exit 0);
input, network or other HTTP errors exit 1; invalid command arguments exit 2.
The script never runs during `hexo generate` or the Vercel build.

## Phase 3 page metadata and share cards

Localized SEO strings live in `seo-i18n.json`; `scripts/seo.js` builds titles,
unique descriptions, clean canonical social URLs and JSON-LD for each language.
Home, category, tag, archive and paginated lists have their own metadata.
Pagination keeps its own canonical and emits `noindex,follow`. Both 404 pages have
localized titles, `noindex, follow`, and links to home, latest posts and providers.
Posts emit NewsArticle and BreadcrumbList; taxonomy pages emit BreadcrumbList.
Both homes emit Organization and WebSite. Populate `_config.yml`'s empty
`seo.same_as` list when official social profiles are ready; empty lists are omitted.

Every post's social image is a 1200×630 JPEG of at most 120KB, with its title,
vendor and VPS Radar brand. Cards mirror source paths under
`source/img/cards/<vendor>/<slug>.jpg`; English filenames retain `.en` so they
never replace Chinese cards. Missing cards fall back to `/img/og-default-v2.jpg`.
Open Graph and Twitter use the page's title and absolute card URL; Open Graph
includes both locales and posts' publication/modification times.

Before publishing new or edited posts, regenerate and **commit the cards**:

```sh
# If Pillow is missing:
python3 -m venv /tmp/vpsradar-cards-venv
/tmp/vpsradar-cards-venv/bin/pip install pillow
# Activate that venv for the commands below when needed:
source /tmp/vpsradar-cards-venv/bin/activate
# A system CJK font and fontconfig are required (e.g. fonts-noto-cjk).
# Inspect available fonts with: fc-list :lang=zh file
python3 tools/generate-cards.py
# Optional custom font: python3 tools/generate-cards.py --font /path/to/font.ttc
npx hexo clean && npx hexo generate
python3 tools/check-seo.py
python3 tools/check-i18n.py
```

The publishing preparation command `npm run prepare:publish` runs card generation,
a clean build and both checks. Run it before committing/pushing content; Vercel
uses the committed JPEGs without requiring Python or CJK fonts during deployment.
If replacing an already published card, account for the existing one-year immutable
image cache (purge the old cached URL when deploying the replacement).


## Publishing checklist

- Use a title near 30 Chinese characters: 「商家名 + 活动 + 年份 + 优惠码/折扣」.
  English pattern: "Vendor + offer + year + coupon/discount". Include only verified details.
- Put verified prices in `description` and/or optional `price` front matter. All
  deal fields are optional: `price` (text), `location`, `network`, `expires`
  (`YYYY-MM-DD`, quoted recommended), `coupon`, and `buy_url`. Omit unknown values;
  never infer an expiry date, price, coupon or vendor fact. See `scaffolds/post.md`.
- Set `cover: /img/default-cover-v2.webp` in both posts, or use an existing local
  vendor image under `source/`. Covers are required and must not use remote HTTP(S)
  URLs; local `cover` and `top_img` paths must point to files under `source/`.
- Publish Chinese `<slug>.md` and English `<slug>.en.md` together; set `lang: en`
  on English and follow the translation key, category and date rules above.
- Run `python3 tools/generate-cards.py`, commit the generated cards, then run
  `npx hexo clean && npx hexo generate`, `python3 tools/check-seo.py` and
  `python3 tools/check-i18n.py` before pushing.
- After deployment is live, run `python3 tools/indexnow.py` (or submit selected
  new URLs using `--urls-from-file` as described above).

## Phase 4 content templates

Optional deal fields produce a localized summary above the post. Missing fields
are omitted; posts without them have no card. External vendor buttons carry
`sponsored nofollow noopener` and open in a new tab. Only HTTP(S) links are allowed.

`expires` is valid through the specified calendar day in the configured site
timezone (`Asia/Singapore`). Earlier dates show a badge on cards/lists and a
notice above the post. Vercel rebuilds only on push: a small inline script also
checks these dates when a visitor loads the page, so an older deployment still
shows newly expired offers. This uses the visitor's clock in the site timezone.
Invalid dates are ignored. Expiry is not added to JSON-LD.

Categories serve as vendor collections with counts and latest deals. Optional
verified introductions and official links go in `source/_data/vendors.yml`, keyed
by exact category name (`website`, `intro_zh`, `intro_en`). The file ships with only
comments. `/vendors/` and `/en/vendors/` list vendors and their latest post dates.
Each post links to up to five latest other deals in its vendor categories, within
its own language. No matching deals means the section has no links.

Search uses native browser APIs and a custom Hexo generator, requiring no new
package. `/search-v4.json` and `/en/search-v4.json` contain only titles,
descriptions and internal URLs; article bodies are excluded. The index loads on
first focus, is reused for subsequent queries and returns at most 20 results.
Versioned CSS and JavaScript respect the site's immutable asset cache policy.
