#!/usr/bin/env python3
"""Manually notify IndexNow after deployment; uses only the Python 3 stdlib."""
import argparse
import json
from pathlib import Path
import sys
from urllib.error import URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET

HOST = 'vpsradar.vayki.com'
KEY = 'e40d982adb11c40759f947a7a287d1e3'
KEY_LOCATION = f'https://{HOST}/{KEY}.txt'
ENDPOINT = 'https://api.indexnow.org/indexnow'
BATCH_SIZE = 10000
DEFAULT_SITEMAP = Path(__file__).resolve().parents[1] / 'public/sitemap.xml'
NS = '{http://www.sitemaps.org/schemas/sitemap/0.9}'


def sitemap_urls(source):
    if urlsplit(source).scheme in ('http', 'https'):
        with urlopen(source, timeout=30) as response:
            root = ET.fromstring(response.read())
    else:
        root = ET.parse(source).getroot()
    if root.tag != NS + 'urlset':
        raise ValueError('Expected a sitemap urlset (not a sitemap index).')
    return [record.findtext(NS + 'loc', default='') for record in root.findall(NS + 'url')]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('sitemap', nargs='?', default=str(DEFAULT_SITEMAP),
                        help='Sitemap path or URL (default: public/sitemap.xml).')
    parser.add_argument('--urls-from-file', type=Path, metavar='FILE',
                        help='Submit only these URLs, one absolute URL per line; blank lines ignored.')
    parser.add_argument('--dry-run', action='store_true',
                        help='Print count and first five URLs without submitting to IndexNow.')
    args = parser.parse_args()
    try:
        if args.urls_from_file is not None:
            candidates = args.urls_from_file.read_text(encoding='utf-8').splitlines()
        else:
            candidates = sitemap_urls(args.sitemap)
        urls = list(dict.fromkeys(url.strip() for url in candidates if url.strip()))
        if not urls:
            raise ValueError('No URLs to submit.')
        for url in urls:
            parts = urlsplit(url)
            if (parts.scheme not in ('http', 'https') or parts.netloc != HOST
                    or parts.fragment or any(c.isspace() for c in url)):
                raise ValueError(f'Expected an absolute http(s) URL on {HOST} without a fragment: {url!r}')
        if args.dry_run:
            print(f'Dry run: {len(urls)} unique URLs; first {min(5, len(urls))}:')
            print('\n'.join(urls[:5]))
            return 0
        for start in range(0, len(urls), BATCH_SIZE):
            batch = urls[start:start + BATCH_SIZE]
            payload = {'host': HOST, 'key': KEY, 'keyLocation': KEY_LOCATION, 'urlList': batch}
            request = Request(ENDPOINT, data=json.dumps(payload).encode('utf-8'),
                              headers={'Content-Type': 'application/json; charset=utf-8'}, method='POST')
            with urlopen(request, timeout=30) as response:
                if response.status not in (200, 202):
                    raise ValueError(f'IndexNow returned unexpected HTTP {response.status}.')
                print(f'Batch {start // BATCH_SIZE + 1}: {len(batch)} URLs, HTTP {response.status}.')
        print(f'Submitted {len(urls)} URLs.')
        return 0
    except (OSError, URLError, ValueError, ET.ParseError) as exc:
        print(f'IndexNow error: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
