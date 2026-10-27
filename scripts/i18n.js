'use strict';

// Keep the stock generators and Butterfly helpers, but give each language its
// own view of the site. No global config/model mutation during rendering.
const { full_url_for } = require('hexo-util');
const taxonomyNames = require('../i18n-taxonomy.json');
const languageOf = post => post.lang === 'en' ? 'en' : 'zh-CN';
const keyOf = post => post.translation_key || post.source.replace(/^_posts\//, '').replace(/(?:\.en)?\.md$/, '');
const own = (obj, key, value) => Object.defineProperty(obj, key, { value, enumerable: true, configurable: true, writable: true });
const prefix = lang => lang === 'en' ? 'en/' : '';
let sites = {};
let counterparts = new Map();
let routes = new Set();

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
  for (const post of locals.posts.toArray()) {
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
hexo.extend.helper.register('language_links', function () {
  const en = this.page.lang === 'en';
  const current = normalized(this.path);
  let other;
  if (this.page.__post) {
    const pair = counterparts.get(keyOf(this.page));
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
});

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
