'use strict';

// Keep the stock generators and Butterfly helpers, but give each language its
// own view of the site. No global config/model mutation during rendering.
const { full_url_for, encodeURL } = require('hexo-util');
const { readFileSync } = require('node:fs');
const { join } = require('node:path');
const { parse: parseFrontMatter } = require('hexo-front-matter');
const taxonomyNames = require('../i18n-taxonomy.json');
const languageOf = post => post.lang === 'en' ? 'en' : 'zh-CN';
const keyOf = post => post.translation_key || post.source.replace(/^_posts\//, '').replace(/(?:\.en)?\.md$/, '');
const own = (obj, key, value) => Object.defineProperty(obj, key, { value, enumerable: true, configurable: true, writable: true });
const prefix = lang => lang === 'en' ? 'en/' : '';
let sites = {};
let counterparts = new Map();
let routes = new Set();
let sitemapDates = new Map();

hexo.extend.filter.register('before_post_render', data => {
  if (data.lang === 'en') {
    // Explicit permalink is supported for English-only posts with custom paths.
    data.__permalink = data.__permalink || `en/${keyOf(data)}/`;
  }
  return data;
}, 1);

hexo.extend.filter.register('before_generate', () => {
  const locals = hexo.locals.toObject();
  const { Query } = hexo.model('Post');
  counterparts = new Map();
  sitemapDates = new Map();
  for (const post of locals.posts.toArray()) {
    // Hexo supplies file mtime as updated when front matter omits it. Inspect
    // the source before language views can replace updated for feed pairing.
    const front = parseFrontMatter(readFileSync(join(hexo.source_dir, post.source), 'utf8'));
    const explicitUpdate = Object.prototype.hasOwnProperty.call(front, 'updated') && front.updated;
    sitemapDates.set(post.source, (explicitUpdate ? post.updated : post.date).toISOString());
    const key = keyOf(post);
    const pair = counterparts.get(key) || {};
    const lang = languageOf(post);
    if (pair[lang]) throw new Error(`Duplicate translation key: ${key} (${lang})`);
    pair[lang] = post;
    counterparts.set(key, pair);
  }
  sites = {};
  for (const lang of ['zh-CN', 'en']) {
    const posts = locals.posts.toArray().filter(p => languageOf(p) === lang).map(post => {
      const view = { ...post };
      own(view, 'path', post.path);
      own(view, 'permalink', post.permalink);
      own(view, 'tags', post.tags);
      own(view, 'categories', post.categories);
      own(view, 'lang', lang);
      own(view, 'prev', null);
      own(view, 'next', null);
      // Blank updated values use the original file's mtime, never translation time.
      const original = counterparts.get(keyOf(post))['zh-CN'];
      if (lang === 'en' && original) own(view, 'updated', original.updated);
      return view;
    });
    const site = { ...locals, posts: new Query(posts) };
    for (const type of ['categories', 'tags']) {
      const terms = locals[type].toArray().map(term => {
        const members = posts.filter(p => p[type].toArray().some(t => t._id === term._id));
        if (!members.length) return null;
        const view = { ...term, slug: term.slug, path: term.path };
        own(view, 'posts', new Query(members));
        own(view, 'length', members.length);
        own(view, 'path', prefix(lang) + term.path);
        own(view, 'permalink', full_url_for.call(hexo, view.path));
        return view;
      }).filter(Boolean);
      site[type] = new Query(terms);
      for (const post of posts) {
        const ids = post[type].toArray().map(t => t._id);
        own(post, type, new Query(terms.filter(t => ids.includes(t._id))));
      }
    }
    sites[lang] = site;
  }
}, 20);

// Wrap once after plugins/theme scripts have registered their generators/helpers.
hexo.on('ready', () => {
  for (const name of ['index', 'archive', 'category', 'tag', 'post']) {
    const generator = hexo.extend.generator.get(name);
    if (!generator) throw new Error(`Missing generator: ${name}`);
    hexo.extend.generator.register(name, async function () {
      const groups = await Promise.all(['zh-CN', 'en'].map(async lang => {
        const config = { ...this.config, archive_dir: prefix(lang) + this.config.archive_dir,
          index_generator: { ...this.config.index_generator, path: prefix(lang) } };
        const context = Object.create(this);
        context.config = config;
        const result = await generator.call(context, sites[lang]) || [];
        return [].concat(result).map(route => {
          route.data.lang = lang;
          return route;
        });
      }));
      return groups.flat();
    });
  }
  // Reuse hexo-generator-feed with the same language-scoped post views.
  const atom = hexo.extend.generator.get('atom');
  const feedGenerator = require('hexo-generator-feed/lib/generator');
  if (!atom) throw new Error('Missing Atom feed generator');
  hexo.extend.generator.register('atom', function () {
    return ['zh-CN', 'en'].map(lang => {
      const context = Object.create(this);
      context.config = { ...this.config, ...(lang === 'en' ? this.config.english : {}),
        language: lang };
      const feed = feedGenerator.call(context, sites[lang], 'atom', prefix(lang) + 'atom.xml');
      if (!feed) return null;
      // feedsmith currently omits xml:lang and HTML content type. Keep escaped
      // full HTML readable to Atom consumers, and set the English site identity.
      const home = this.config.url.replace(/\/$/, '') + '/';
      feed.data = feed.data.replace('<feed ', `<feed xml:lang="${lang}" `)
        .replace(/<content>/g, '<content type="html">');
      if (lang === 'en') feed.data = feed.data
        .replace(`<id>${home}</id>`, `<id>${home}en/</id>`)
        .replace(`<link href="${home}" rel="alternate"/>`, `<link href="${home}en/" rel="alternate"/>`);
      const latest = sites[lang].posts.toArray().map(p => (p.updated || p.date).toISOString()).sort().pop();
      feed.data = feed.data.replace(/<updated>[^<]+<\/updated>/, `<updated>${latest}</updated>`);
      return feed;
    }).filter(Boolean);
  });
  // Butterfly caches menus, sidebar counts, UI config and footers. Scope all
  // fragment/partial caches by language, including nested cached partials.
  const fragment = hexo.extend.helper.get('fragment_cache');
  hexo.extend.helper.register('fragment_cache', function (id, fn) {
    return fragment.call(this, `${this.page.lang}:${id}`, fn);
  });
});

// Record actual generated paths: missing translations fall back to home, never
// an invented URL. Taxonomy pages are paired through the shared vocabulary.
hexo.extend.filter.register('after_generate', () => { routes = new Set(hexo.route.list()); });
const normalized = path => path.replace(/^\//, '').replace(/index\.html$/, '');
function languageLinks(page, path) {
  const en = page.lang === 'en';
  const current = normalized(path);
  let other;
  if (page.__post) {
    const pair = counterparts.get(keyOf(page));
    other = pair && pair[en ? 'zh-CN' : 'en']?.path;
  } else {
    other = en ? current.replace(/^en\//, '') : 'en/' + current;
    for (const [zh, english] of Object.entries(taxonomyNames)) {
      const from = en ? english.replace(/ /g, '-') : zh.replace(/\//g, '-');
      const to = en ? zh.replace(/\//g, '-') : english.replace(/ /g, '-');
      if (other.includes(`tags/${from}/`)) other = other.replace(`tags/${from}/`, `tags/${to}/`);
    }
  }
  const missing = other == null;
  other = missing ? (en ? '' : 'en/') : normalized(other);
  const file = other.endsWith('.html') ? other : other + 'index.html';
  const exists = !missing && routes.has(file);
  const target = exists ? '/' + other : (en ? '/' : '/en/');
  return { current: '/' + current, other: target, translated: exists,
    zh: en ? (exists ? target : null) : '/' + current,
    en: en ? '/' + current : (exists ? target : null) };
}
hexo.extend.helper.register('language_links', function () { return languageLinks(this.page, this.path); });

hexo.extend.filter.register('template_locals', locals => {
  const lang = locals.page.lang === 'en' || locals.path.startsWith('en/') ? 'en' : 'zh-CN';
  locals.page.lang = lang;
  locals.site = sites[lang];
  locals.config = { ...locals.config, language: lang };
  if (lang === 'en') {
    const english = locals.config.english;
    Object.assign(locals.config, english);
    for (const key of ['archive_dir', 'tag_dir', 'category_dir']) locals.config[key] = 'en/' + hexo.config[key];
    locals.theme = { ...locals.theme, menu: hexo.theme.config.menu_en,
      noticeOutdate: { ...locals.theme.noticeOutdate, message_prev: 'It has been ', message_next: ' days since the last update. This article may be out of date.' } };
  }
  locals.__ = hexo.theme.i18n.__([lang]);
  locals._p = hexo.theme.i18n._p([lang]);
  return locals;
}, 20);

hexo.extend.generator.register('english-pages', () => [
  { path: 'en/tags/index.html', layout: 'page', data: { title: 'Tags', type: 'tags', lang: 'en', orderby: 'length', order: -1 } },
  { path: 'en/categories/index.html', layout: 'page', data: { title: 'Categories', type: 'categories', lang: 'en' } },
  { path: 'en/404.html', layout: 'page', data: { type: '404', lang: 'en', top_img: false, comments: false, aside: false } }
]);

// Use actual routes, keeping only page one of each list. Thin taxonomy and
// dated archive pages stay accessible but out of the sitemap.
const xml = value => String(value).replace(/[<>&"']/g, c => ({ '<': '&lt;', '>': '&gt;', '&': '&amp;', '"': '&quot;', "'": '&apos;' }[c]));
const indexable = post => post.sitemap !== false && post.indexing !== false && post.noindex !== true;
const modified = post => sitemapDates.get(post.source);
hexo.extend.filter.register('after_generate', () => {
  const entries = new Map();
  for (const lang of ['zh-CN', 'en']) {
    const site = sites[lang];
    const posts = site.posts.toArray().filter(indexable);
    const latest = members => members.map(modified).sort().pop();
    const add = (path, members, page = { lang }) => {
      path = normalized(path);
      if (!routes.has(path + 'index.html') || !members.length) return;
      entries.set(path, { lastmod: latest(members), page });
    };
    for (const post of posts) add(post.path, [post], { ...post, __post: true });
    const root = prefix(lang);
    for (const route of routes) {
      if (route.startsWith('en/') !== (lang === 'en')) continue;
      const path = normalized(route).slice(root.length);
      if (/^(?:|tags\/|categories\/|vendors\/)$/.test(path)) {
        add(route, posts);
      }
    }
    for (const type of ['tags', 'categories']) {
      for (const term of site[type].toArray()) {
        const members = term.posts.toArray().filter(indexable);
        if (members.length < 3) continue;
        add(term.path, members);
      }
    }
    for (const page of site.pages.toArray().filter(indexable)) {
      if ((page.path.startsWith('en/')) === (lang === 'en') && !/404\.html$/.test(page.path)) add(page.path, posts);
    }
  }
  const url = path => encodeURL(hexo.config.url.replace(/\/$/, '') + '/' + normalized(path));
  const records = [...entries].sort(([a], [b]) => a.localeCompare(b)).map(([path, entry]) => {
    const links = languageLinks(entry.page, path);
    let alternates = '';
    if (links.translated && [links.zh, links.en].every(p => entries.has(normalized(p)))) {
      alternates = [['zh-CN', links.zh], ['en', links.en], ['x-default', links.zh]]
        .map(([lang, path]) => `<xhtml:link rel="alternate" hreflang="${lang}" href="${xml(url(path))}"/>`).join('');
    }
    return `<url><loc>${xml(url(path))}</loc><lastmod>${entry.lastmod}</lastmod>${alternates}</url>`;
  });
  hexo.route.set('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n' +
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + records.join('\n') + '\n</urlset>\n');
}, 20);
