'use strict';
const { escapeHTML } = require('hexo-util');
const moment = require('moment-timezone');
const esc = value => escapeHTML(String(value ?? ''));
const labels = {
  'zh-CN': { price: '价格', location: '机房', network: '线路', expires: '有效期', coupon: '优惠码', buy_url: '前往官网', expired: '已过期', notice: '此优惠已过期，请前往官网确认当前活动。', related: '同商家其他优惠', latest: '最新优惠', count: '篇优惠', vendors: '商家' },
  en: { price: 'Price', location: 'Location', network: 'Network', expires: 'Valid until', coupon: 'Coupon', buy_url: 'Visit vendor', expired: 'Expired', notice: 'This deal has expired. Check the vendor website for current offers.', related: 'More deals from this vendor', latest: 'Latest deals', count: 'deals', vendors: 'Vendors' }
};
const t = ctx => labels[ctx.page.lang === 'en' ? 'en' : 'zh-CN'];
// Dates are calendar dates in the site's configured timezone, valid through that day.
function expiry(post) {
  const value = post.expires;
  const day = value instanceof Date ? value.toISOString().slice(0, 10) : String(value || '');
  return /^\d{4}-\d{2}-\d{2}$/.test(day) && moment(day, 'YYYY-MM-DD', true).isValid() ? day : '';
}
const expired = day => day < moment().tz(hexo.config.timezone || 'UTC').format('YYYY-MM-DD');
function marker(ctx, post, notice = false) {
  const day = expiry(post);
  if (!day) return '';
  return `<${notice ? 'aside' : 'span'} class="${notice ? 'deal-expiry-notice' : 'deal-expired'}" data-expires="${day}"${expired(day) ? '' : ' hidden'}>${esc(t(ctx)[notice ? 'notice' : 'expired'])}</${notice ? 'aside' : 'span'}>`;
}
function safeLink(ctx, value, label) {
  try {
    const url = new URL(String(value), hexo.config.url);
    if (!['https:', 'http:'].includes(url.protocol)) return '';
    const external = url.origin !== new URL(hexo.config.url).origin;
    return `<a class="deal-vendor-link" href="${esc(url.href)}"${external ? ' target="_blank" rel="sponsored nofollow noopener"' : ''}>${esc(label)}</a>`;
  } catch { return ''; }
}
const list = (ctx, posts) => '<ul>' + posts.map(p => `<li><a href="${esc(ctx.url_for(p.path))}">${esc(p.title)}</a>${marker(ctx, p)}</li>`).join('') + '</ul>';
const latest = posts => posts.slice().sort((a, b) => b.date.valueOf() - a.date.valueOf() || a.path.localeCompare(b.path));
hexo.extend.helper.register('expiry_badge', function (post) { return marker(this, post); });
hexo.extend.helper.register('deal_summary', function (post) {
  const fields = ['price', 'location', 'network', 'expires', 'coupon'];
  const populated = fields.filter(k => k === 'expires' ? expiry(post) : post[k] != null && String(post[k]).trim());
  const buy = post.buy_url ? safeLink(this, post.buy_url, t(this).buy_url) : '';
  if (!populated.length && !buy) return '';
  return marker(this, post, true) + `<section class="deal-summary" aria-label="${this.page.lang === 'en' ? 'Deal summary' : '优惠概要'}">${marker(this, post)}<dl>` + populated.map(k => `<div><dt>${t(this)[k]}</dt><dd>${esc(k === 'expires' ? expiry(post) : post[k])}</dd></div>`).join('') + '</dl>' + buy + '</section>';
});
hexo.extend.helper.register('vendor_related', function (post) {
  const ids = post.categories.toArray().map(c => c._id);
  const posts = latest(this.site.posts.toArray().filter(p => p.path !== post.path && p.categories.toArray().some(c => ids.includes(c._id)))).slice(0, 5);
  return `<section class="vendor-related"><h2>${t(this).related}</h2>${posts.length ? list(this, posts) : ''}</section>`;
});
hexo.extend.helper.register('vendor_header', function () {
  const term = this.site.categories.toArray().find(c => c.name === this.page.category);
  if (!term) return '';
  const data = this.site.data.vendors?.[term.name] || {};
  const intro = data[this.page.lang === 'en' ? 'intro_en' : 'intro_zh'];
  return `<section class="vendor-header"><h2>${esc(term.name)}</h2>${intro ? `<p>${esc(intro)}</p>` : ''}${data.website ? safeLink(this, data.website, t(this).buy_url) : ''}<p>${term.length} ${t(this).count}</p><h3>${t(this).latest}</h3>${list(this, latest(term.posts.toArray()).slice(0, 5))}</section>`;
});
hexo.extend.helper.register('vendors_index', function () {
  return '<ul class="vendors-index">' + this.site.categories.toArray().sort((a, b) => a.name.localeCompare(b.name)).map(c => {
    const day = latest(c.posts.toArray())[0].date.format('YYYY-MM-DD');
    return `<li><a href="${esc(this.url_for(c.path))}">${esc(c.name)}</a> <span>${c.length} ${t(this).count}</span> · <time datetime="${day}">${day}</time></li>`;
  }).join('') + '</ul>';
});
hexo.extend.generator.register('vendors', () => ['zh-CN', 'en'].map(lang => ({ path: `${lang === 'en' ? 'en/' : ''}vendors/index.html`, layout: 'page', data: { lang, title: labels[lang].vendors, type: 'vendors', comments: false } })));
hexo.extend.generator.register('deal-search', locals => ['zh-CN', 'en'].map(lang => ({
  path: `${lang === 'en' ? 'en/' : ''}search-v4.json`,
  data: JSON.stringify(latest(locals.posts.toArray().filter(p => (p.lang === 'en' ? 'en' : 'zh-CN') === lang && p.noindex !== true && p.indexing !== false)).map(p => ({ title: p.title, description: p.description || '', url: '/' + p.path.replace(/^\/+/, '') })))
})));
// Calendar rollover is checked in the browser as well, without a new deployment.
hexo.extend.filter.register('after_render:html', html => html.includes('data-expires=') ? html.replace('</body>', `<script>(()=>{const today=new Intl.DateTimeFormat('en-CA',{timeZone:${JSON.stringify(hexo.config.timezone || 'UTC')},year:'numeric',month:'2-digit',day:'2-digit'}).formatToParts(new Date());const get=t=>today.find(p=>p.type===t).value;const day=get('year')+'-'+get('month')+'-'+get('day');document.querySelectorAll('[data-expires]').forEach(el=>{el.hidden=el.dataset.expires>=day})})();</script></body>`) : html);
