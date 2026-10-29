'use strict';
// Real Hexo generation in /tmp: no fixture is ever written under source/_posts.
const assert = require('node:assert/strict');
const fs = require('node:fs/promises');
const os = require('node:os');
const path = require('node:path');
const Hexo = require('hexo');
const vm = require('node:vm');
const root = path.resolve(__dirname, '..');
(async () => {
  const dir = await fs.mkdtemp(path.join(os.tmpdir(), 'vpsradar-deals-'));
  let hexo;
  try {
    for (const name of ['node_modules', 'themes', 'scripts', 'seo-i18n.json', 'i18n-taxonomy.json']) await fs.symlink(path.join(root, name), path.join(dir, name));
    for (const name of ['_config.yml', '_config.butterfly.yml', 'package.json']) await fs.copyFile(path.join(root, name), path.join(dir, name));
    await fs.mkdir(path.join(dir, 'source/_posts'), { recursive: true });
    for (const lang of ['zh-CN', 'en']) {
      for (let n = 1; n <= 7; n++) {
        const suffix = lang === 'en' ? '.en' : '';
        const content = `---\ntitle: Fixture ${n}\ndate: 2026-01-0${n}\nlang: ${lang}\ncategories: ${n < 3 ? '[[fixture-vendor], [thin-vendor]]' : '[fixture-vendor]'}\ntags: [${n < 3 ? 'thin' : 'thick'}]\n${n === 1 ? 'price: "TEST PRICE"\nlocation: "TEST LOCATION"\nnetwork: "TEST NETWORK"\nexpires: "2000-01-01"\ncoupon: "<TEST>"\nbuy_url: "https://example.com/"' : n === 2 ? 'expires: "2999-01-01"' : n === 3 ? 'expires: "2026-02-30"\nbuy_url: "javascript:alert(1)"' : ''}\n---\nFixture content.\n`;
        await fs.writeFile(path.join(dir, `source/_posts/fixture-${n}${suffix}.md`), content);
      }
    }
    hexo = new Hexo(dir, { silent: true });
    await hexo.init();
    hexo.config.index_generator.per_page = 2;
    await hexo.call('generate');
    const html = async route => fs.readFile(path.join(dir, 'public', route, 'index.html'), 'utf8');
    for (const prefix of ['', 'en/']) {
      const post = await html(prefix + 'fixture-1');
      for (const value of ['deal-summary', 'TEST PRICE', 'TEST LOCATION', 'TEST NETWORK', '&lt;TEST&gt;', '2000-01-01', 'target="_blank" rel="sponsored nofollow noopener"', 'vendor-related']) assert(post.includes(value), value);
      for (const label of prefix ? ['Price', 'Location', 'Network', 'Valid until', 'Coupon', 'Visit vendor', 'Expired'] : ['价格', '机房', '线路', '有效期', '优惠码', '前往官网', '已过期']) assert(post.includes(label), label);
      assert.match(post, /class="deal-expired" data-expires="2000-01-01">/);
      assert.match(post, /class="deal-expiry-notice" data-expires="2000-01-01">/);
      assert.match(await html(prefix + 'fixture-2'), /data-expires="2999-01-01" hidden/);
      assert(!(await html(prefix + 'fixture-3')).includes('class="deal-summary"'));
      assert(!(await html(prefix + 'fixture-4')).includes('class="deal-summary"'));
      const related = post.match(/<section class="vendor-related">(.*?)<\/section>/s)[1].replace(/&#x2F;/g, '/');
      assert.equal((related.match(/<li>/g) || []).length, 5);
      assert(!related.includes(`href="/${prefix}fixture-1/"`));
      for (const match of related.matchAll(/href="([^"]+)"/g)) assert.equal(match[1].startsWith('/en/'), !!prefix, related);
      const category = await html(prefix + 'categories/fixture-vendor');
      assert(category.includes('vendor-header') && category.includes('7 '));
      assert.match(category, /class="deal-expired" data-expires="2000-01-01">/);
      assert((await html(prefix + 'vendors')).includes('fixture-vendor'));
      for (const route of ['tags/thin', 'categories/thin-vendor', 'archives', 'page/2']) assert((await html(prefix + route)).includes('content="noindex,follow"'));
      assert(!(await html(prefix + 'tags/thick')).includes('content="noindex,follow"'));
      const index = JSON.parse(await fs.readFile(path.join(dir, 'public', prefix, 'search-v4.json'), 'utf8'));
      assert.equal(index.length, 7);
      assert(index.every(row => row.url.startsWith('/en/') === !!prefix));
      // Execute the exact inline expiry script with a controlled browser clock.
      const script = [...post.matchAll(/<script>(.*?)<\/script>/gs)].find(m => m[1].includes("querySelectorAll('[data-expires]')"))[1];
      for (const [now, shouldHide] of [['1999-12-31T04:00:00Z', true], ['2000-01-01T04:00:00Z', true], ['2000-01-02T04:00:00Z', false]]) {
        const elements = [{ dataset: { expires: '2000-01-01' }, hidden: null }];
        class Clock extends Date { constructor() { super(now); } }
        vm.runInNewContext(script, { Intl, Date: Clock, document: { querySelectorAll: () => elements } });
        assert.equal(elements[0].hidden, shouldHide);
      }
    }
    console.log('Temporary bilingual build: optional cards, escaping, expiry boundaries/client rollover, list badges, related links, vendors, thin pages and search passed.');
  } finally {
    if (hexo) await hexo.exit();
    await fs.rm(dir, { recursive: true, force: true });
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
