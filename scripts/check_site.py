"""Check same-site links in a GitHub Pages build. Python standard library only."""
from html.parser import HTMLParser
from pathlib import Path
import sys
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self, content):
        super().__init__()
        self.links = []
        self.ids = set()
        self.feed(content)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get('id'):
            self.ids.add(attrs['id'])
        if tag == 'a' and attrs.get('href'):
            self.links.append(attrs['href'])
        if tag in {'img', 'script'} and attrs.get('src'):
            self.links.append(attrs['src'])
        if tag == 'link' and attrs.get('rel') == 'stylesheet':
            self.links.append(attrs['href'])


def main():
    root = Path(sys.argv[1]).resolve()
    # Read from the source config rather than depend on a YAML package.
    baseurl = next(line.split(':', 1)[1].strip().strip('"\'') for line in Path('_config.yml').read_text(encoding='utf-8').splitlines() if line.startswith('baseurl:'))
    pages = {p.resolve(): Page(p.read_text(encoding='utf-8')) for p in root.rglob('*.html')}
    errors = []
    checked = 0
    for source, page in pages.items():
        for link in page.links:
            url = urlsplit(link)
            if url.scheme or url.netloc:
                continue
            path = unquote(url.path)
            if path.startswith('/'):
                if not (path == baseurl or path.startswith(baseurl + '/')):
                    # The other archive is hosted by the sibling repository.
                    if path.startswith(('/Sanony/', '/monitoring/')):
                        continue
                    errors.append(f'{source.relative_to(root)}: unexpected site path {link}')
                    continue
                target = root / path[len(baseurl):].lstrip('/')
            else:
                target = source.parent / path if path else source
            if target.is_dir():
                target = target / 'index.html'
            target = target.resolve()
            if not target.is_relative_to(root) or not target.is_file():
                errors.append(f'{source.relative_to(root)}: missing {link}')
                continue
            checked += 1
            if url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{source.relative_to(root)}: missing fragment {link}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'OK: {len(pages)} HTML pages, {checked} local links and resources, including fragments.')


if __name__ == '__main__':
    main()
