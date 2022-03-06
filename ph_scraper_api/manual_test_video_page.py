from pprint import pprint

import requests
from bs4 import BeautifulSoup

from ph_scraper_api.ph_scraper_api.ph_helper.filter import filter_free_premium
from ph_scraper_api.ph_scraper_api.ph_page import get_videos, get_channels, get_video_details


def main():
    # res = get_videos(page=2, min_duration=30, video_type='professional', option='most_viewed', search='gangbang teen')
    # res = get_channels(subdomain='de', option='a-z', letter='d', search='sis', page=2)
    # res = get_video_details('/view_video.php?viewkey=ph61c0772d6eda2')
    res = filter_free_premium(get_videos(channel='nubiles-porn')['videos'])
    pprint(res)


def get_page(url):
    html = requests.get(url).text
    return BeautifulSoup(html, "html.parser")


if __name__ == '__main__':
    main()
