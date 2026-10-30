'use strict';
const { existsSync } = require('node:fs');
const { join } = require('node:path');
const FALLBACK = '/img/default-cover-v2.webp';

// Source filenames retain .en, independently of translated titles/permalinks.
function resolveCover(post, sourceDir) {
  const slug = post.source.replace(/^_posts\//, '').replace(/\.md$/, '');
  const card = `/img/cards/${slug}.jpg`;
  const thumbnail = `/img/cards/${slug}.webp`;
  const vendor = slug.split('/')[0].replace(/\.en$/, '');
  const vendorLogo = typeof post.cover === 'string' &&
    new RegExp(`^/img/${vendor.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}(?:\\.[^/]+)$`, 'i').test(post.cover);
  const automatic = !post.cover || post.cover === FALLBACK || vendorLogo;
  const hasCard = existsSync(join(sourceDir, card));
  const hasThumbnail = hasCard && existsSync(join(sourceDir, thumbnail));
  return {
    card: hasCard ? card : null,
    thumbnail: hasThumbnail ? thumbnail : null,
    cover: automatic ? (hasThumbnail ? thumbnail : hasCard ? card : FALLBACK) : post.cover
  };
}
module.exports = { resolveCover, FALLBACK };
