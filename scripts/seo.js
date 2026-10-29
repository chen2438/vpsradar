'use strict';
const { existsSync } = require('node:fs');
const { join } = require('node:path');
const text = require('../seo-i18n.json');
const safeJson = value => JSON.stringify(value).replace(/</g, '\\u003c');

hexo.extend.helper.register('page_seo', function (type) {
  const { page, config } = this;
  if (page.type === '404') type = '404';
  const en = page.lang === 'en';
  const t = text[en ? 'en' : 'zh-CN'];
  const root = en ? '/en/' : '/';
  const absolute = path => new URL(path, config.url + '/').href;
  const canonical = config.url.replace(/\/$/, '') + this.language_links().current;
  const format = (value, values = {}) => value.replace(/\{(\w+)\}/g, (_, key) => values[key] ?? '');
  let title = page.title || config.title;
  let description = page.description || config.description;
  let key;
  const values = { name: page.category || page.tag, date: page.year ? ` ${page.year}${page.month ? '-' + String(page.month).padStart(2, '0') : ''}` : '' };
  if (type === 'home') key = 'home';
  else if (type === 'category' || type === 'tag') key = type;
  else if (type === 'archive') key = 'archives';
  else if (type === '404') key = 'not_found';
  else if (['tags', 'categories'].includes(page.type)) key = page.type;
  if (key) {
    title = format(t[key], values);
    description = format(t[key + '_description'], values);
  }
  if (Number(page.current) > 1) {
    title += format(t.pagination, { page: page.current });
    description += format(t.pagination_description, { page: page.current });
  }
  title += ' | VPS Radar';
  const slug = page.source && page.source.replace(/^_posts\//, '').replace(/\.md$/, '');
  const card = slug && `/img/cards/${slug}.jpg`;
  const image = absolute(type === 'post' && card && existsSync(join(hexo.source_dir, card)) ? card : '/img/og-default-v2.jpg');
  const organization = { '@type': 'Organization', '@id': absolute('/#organization'), name: 'VPS Radar', url: absolute('/'), logo: { '@type': 'ImageObject', url: absolute('/img/logo-v2.webp') } };
  if (config.seo?.same_as?.length) organization.sameAs = config.seo.same_as;
  const structured = [];
  if (type === 'home' && (!page.current || page.current === 1)) {
    structured.push(organization, { '@type': 'WebSite', '@id': absolute(root + '#website'), name: 'VPS Radar', url: absolute(root), inLanguage: en ? 'en-US' : 'zh-CN', publisher: { '@id': organization['@id'] } });
  }
  const crumbs = [{ name: t.home_label, item: absolute(root) }];
  if (type === 'post') {
    const category = page.categories?.toArray()[0];
    if (category) crumbs.push({ name: category.name, item: absolute('/' + category.path.replace(/index\.html$/, '')) });
    crumbs.push({ name: page.title, item: canonical });
    structured.push({ '@type': 'NewsArticle', headline: page.title, description, url: canonical, image: [image], datePublished: page.date.toISOString(), dateModified: (page.updated || page.date).toISOString(), inLanguage: en ? 'en-US' : 'zh-CN', author: [{ '@type': 'Person', name: page.copyright_author || config.author, url: absolute(page.copyright_author_href || '/') }], publisher: organization, mainEntityOfPage: { '@type': 'WebPage', '@id': canonical } });
  } else if (['category', 'tag'].includes(type)) {
    crumbs.push({ name: t[type === 'category' ? 'categories_label' : 'tags_label'], item: absolute(root + (type === 'category' ? 'categories/' : 'tags/')) });
    crumbs.push({ name: page.category || page.tag, item: canonical });
  } else if (['categories', 'tags'].includes(page.type)) {
    crumbs.push({ name: title, item: canonical });
  }
  if (crumbs.length > 1) structured.push({ '@type': 'BreadcrumbList', itemListElement: crumbs.map((crumb, i) => ({ '@type': 'ListItem', position: i + 1, ...crumb })) });
  const term = type === 'category' ? this.site.categories.toArray().find(t => t.name === page.category) : type === 'tag' ? this.site.tags.toArray().find(t => t.name === page.tag) : null;
  const noindex = type === 'archive' || Number(page.current) > 1 || (term && term.length < 3) || page.noindex === true || page.indexing === false;
  return { noindex, title, description, canonical, image, locale: en ? 'en_US' : 'zh_CN', alternateLocale: en ? 'zh_CN' : 'en_US', t, root, json: structured.length ? safeJson({ '@context': 'https://schema.org', '@graph': structured }) : null };
});
