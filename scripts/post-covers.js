'use strict';
const { readFileSync } = require('node:fs');
const { join } = require('node:path');
const { parse } = require('hexo-front-matter');
const { resolveCover } = require('./lib/post-cover');

// Run before i18n.js copies posts into language-specific site views (priority 20)
// and before Butterfly's generator detects cover_type and links prev/next posts.
// Re-resolve on every build, including cached posts and newly generated cards.
hexo.extend.filter.register('before_generate', () => {
  for (const post of hexo.locals.get('posts').toArray()) {
    const front = parse(readFileSync(join(hexo.source_dir, post.source), 'utf8'));
    post.cover = resolveCover({ ...front, source: post.source }, hexo.source_dir).cover;
    post.cover_type = 'img';
    // Covers must not implicitly turn on Butterfly's large post banner.
    if (post.top_img == null) post.top_img = false;
  }
}, 10);
