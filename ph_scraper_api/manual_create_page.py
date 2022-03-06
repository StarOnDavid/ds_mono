import json
from pathlib import Path

from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

from ph_scraper_api.create_page.create_page import create_page

PACKAGE_PATH = Path.cwd()
OUT_PATH = PACKAGE_PATH / 'out'


def main():
    with open(OUT_PATH / 'free_premium.json', "r", encoding="utf-8") as f:
        content = json.load(f)

    index_page = create_page(content, 'index.html')
    with open(OUT_PATH / 'index.html', 'w', encoding="utf-8") as f:
        f.write(index_page)

    for channel in content['porn_hub']:
        out_page = create_page(channel, 'free_premium.html')

        file = channel['channel']['rel_url'].split('/')

        with open(OUT_PATH / file[0] / (file[1] + '.html'), 'w', encoding="utf-8") as f:
            f.write(out_page)


if __name__ == '__main__':
    main()