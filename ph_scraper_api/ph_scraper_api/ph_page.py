import json

import requests
from bs4 import BeautifulSoup

from ph_scraper_api.ph_scraper_api.ph_helper.content import get_all_video_tumbs, get_all_channel_tumbs, \
    get_page_content, get_all_video_details, get_all_channel_details
from ph_scraper_api.ph_scraper_api.ph_helper.url import create_url


# TODO
# problems with 'query-search'
#   combind with => 'category'
#


def get_videos(
        subdomain=None,
        page=None,  # '[number]'
        hd=None,  # '1' for True
        min_duration=None,  # '[10, 20, 30]'
        max_duration=None,  # '[10, 20, 30]'
        option=None,
        country=None,
        category=None,
        letter=None,
        video_type=None,
        search=None,
        rel_url=None,
        channel=None,
        model=None
):
    if not rel_url:
        search_page = {
            'search': 'video',
            'subdomain': subdomain,
            'channel': channel,
            'model': model,
            'query': {
                'page': page,
                'hd': hd,
                'min_duration': min_duration,
                'max_duration': max_duration,
                'option': option,
                'country': country,
                'category': category,
                'letter': letter,
                'video_type': video_type,
                'search': search
            }
        }
        if search_page['query']['search'] is not None:
            search_page['query']['search'] = search_page['query']['search'].replace(' ', '+')
            search_page['search'] = 'video/search'
        if search_page['channel'] is not None:
            search_page['search'] = 'channels/' + channel + '/videos'
        if search_page['model'] is not None:
            search_page['search'] = 'model/' + model + '/videos'
    else:
        search_page = rel_url
    return get_all_video_tumbs(create_url(search_page))


def get_video_details(rel_url):
    return get_all_video_details(create_url(rel_url))


def get_channel_details(rel_url):
    if 'channels' not in rel_url:
        rel_url = 'channels/' + rel_url
    return get_all_channel_details(create_url(rel_url))


def get_channels(
        page=None,
        subdomain=None,
        option=None,
        letter=None,
        search=None
):
    search_page = {
        'search': 'channels',
        'subdomain': subdomain,
        'query': {
            'page': page,
            'option': option,
            'letter': letter,
            'search': search
        }
    }
    if search_page['query']['search']:
        search_page['query']['option'] = None
        search_page['query']['letter'] = None
        search_page['search'] = search_page['search'] + '/search'

    return get_all_channel_tumbs(create_url(search_page))


def get_pornstars():
    print('NOT SUPPORTED JET')
    # TODO
    # implement with content getter in content.py

