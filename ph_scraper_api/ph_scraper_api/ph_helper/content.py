from pprint import pprint

import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_page_content(url):
    html = requests.get(url).text
    return BeautifulSoup(html, "html.parser")


def get_all_video_tumbs(url):
    def get_video_tumb_infos(wrap):
        ph_img = wrap.find('div', {'class': 'phimage'})
        if ph_img:
            video_infos = {'video': {}, 'user': {}, 'free_premium': False}
            img = ph_img.find('img')

            video_infos['video']['rel_url'] = ph_img.find('a', {'class': 'linkVideoThumb'}).get('href')
            video_infos['video']['title'] = ph_img.find('a', {'class': 'linkVideoThumb'}).get('title')
            video_infos['video']['tumb_img'] = img.get('data-thumb_url')
            video_infos['video']['tumb_mediabook'] = img.get('data-mediabook')
            video_infos['video']['duration'] = wrap.find('var', {'class': 'duration'}).get_text()
            ph_username_wrap = wrap.find('div', {'class': 'usernameWrap'})
            if ph_username_wrap:
                ph_username = ph_username_wrap.find('a')
                video_infos['user']['name'] = ph_username.get_text()
                video_infos['user']['rel_url'] = ph_username.get('href')
            ph_free = wrap.find('span', {'class': 'phpFreeBlock'})
            if ph_free:
                video_infos['free_premium'] = True
            return video_infos
        else:
            return None

    page_content = get_page_content(url)
    all_tumb_videos = {'videos': [], 'has_next': False}
    wraps = page_content.findAll('div', {'class': 'wrap'})
    for w in wraps:
        video_info = get_video_tumb_infos(w)

        if video_info:
            if 'channels' in url and video_info['user']:
                continue
            all_tumb_videos['videos'].append(video_info)

    has_next = page_content.find('li', {'class': 'page_next'})
    if has_next:
        all_tumb_videos['has_next'] = True
    return all_tumb_videos


def get_all_channel_tumbs(url):
    def get_channels_tumb_infos(wrap):
        rel_url = wrap.find('a').get('href')
        if rel_url:
            description_container = wrap.find('div', {'class': 'descriptionContainer'})
            description_container_li_elements = description_container.find('ul').findAll('li')
            ch_infos = {
                'rel_url': rel_url,
                'rank': wrap.find('div', {'class': 'rank'}).find('span').get_text().split(' ')[1].replace('\t', ''),
                'img': wrap.find('img').get('data-thumb_url'),
                'username': description_container.find('a').get_text(),
                'subscribers': description_container_li_elements[1].find('span').get_text().replace(',', ''),
                'videos': description_container_li_elements[2].find('span').get_text().replace(',', ''),
                'videos_views': description_container_li_elements[3].find('span').get_text().replace(',', '')
            }
            return ch_infos
        return None

    page_content = get_page_content(url)
    all_tumb_channels = {'videos': [], 'has_next': False}
    wraps = page_content.findAll('div', {'class': 'channelsWrapper'})
    for w in wraps:
        channel_info = get_channels_tumb_infos(w)
        if channel_info:
            all_tumb_channels['videos'].append(channel_info)
    has_next = page_content.find('li', {'class': 'page_next'})
    if has_next:
        all_tumb_channels['has_next'] = True
    return all_tumb_channels


def get_all_video_details(url):
    def get_item_texts(div_items):
        texts = []
        for cat in div_items.find_all('a', {'class': 'item'}):
            texts.append(cat.get_text())
        return texts

    def get_stars_list(div_stars):
        stars = []
        for star in div_stars.find_all('a', {'class': 'pstar-list-btn'}):
            stars.append({
                'name': star.get('data-mxptext'),
                'avatar_url': star.find('img').get('data-src'),
                'rel_url': star.get('href')
            })
        return stars

    page_content = get_page_content(url)

    rating = page_content.find('div', {'class': 'ratingInfo'})
    categories = page_content.find('div', {'class', 'categoriesWrapper'})
    pornstars = page_content.find('div', {'class', 'pornstarsWrapper'})
    tags = page_content.find('div', {'class', 'tagsWrapper'})

    return {'views': rating.find('div', {'class': 'views'}).find('span').get_text(),
            'rating_percent': rating.find('div', {'class': 'ratingPercent'}).find('span').get_text(),
            'published': rating.find('div', {'class': 'videoInfo'}).get_text(),
            'categories': get_item_texts(categories),
            'pornstars': get_stars_list(pornstars),
            'tags': get_item_texts(tags),
            'production': page_content.find('div', {'class': 'productionWrapper'}).find('a').get_text()
            }


def get_all_channel_details(url):
    page_content = get_page_content(url)
    description = page_content.find('div', {'class': 'cdescriptions'}).findAll('p')
    stats = page_content.find('div', {'id': 'stats'}).findAll('div', {'class': 'info'})
    return {'titel': page_content.find('div', {'class': 'titleWrapper'}).find('h1').get_text(),
            'rel_url': url.split('com/')[1],
            'description_text': str(description[0].get_text()).replace('\n', '').replace('\t', '').replace('\r', ''),
            'joined': description[1].findAll('span')[1].get_text(),
            'website': description[2].find('a').get_text().lower(),
            'by': description[3].find('a').get_text(),
            'avatar_url': page_content.find('img', {'id': 'getAvatar'}).get('src'),
            'cover_pic_url': page_content.find('img', {'id': 'coverPictureDefault'}).get('src'),
            'video_views': stats[0].get_text().split(' ')[0].replace(',', ''),
            'subscribers': stats[1].get_text().split(' ')[0].replace(',', ''),
            'videos': stats[2].get_text().split(' ')[0].replace(',', ''),
            'rank': stats[3].get_text().split(' ')[0].replace(',', '')
    }
