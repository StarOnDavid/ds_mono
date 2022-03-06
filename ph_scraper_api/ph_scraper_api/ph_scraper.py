from collections import defaultdict

from ph_scraper_api.ph_scraper_api.ph_page import get_videos


def search_videos(
        subdomain=None,
        pages=None,
        hd=None,
        min_duration=None,
        max_duration=None,
        option=None,
        country=None,
        category=None,
        letter=None,
        video_type=None,
        search=None,
        channel=None
):
    # get_videos(subdomain=subdomain, page=page, hd=hd, min_duration=min_duration, max_duration=max_duration,
    #            option=option, country=country, category=category, letter=letter, video_type=video_type, search=search,
    #            rel_url=None, channel=None)
    videos = []
    if pages == 'all':
        has_next = True
        page = 1
        while has_next:
            page_result = get_videos(subdomain=subdomain, page=page, hd=hd, min_duration=min_duration,
                                     max_duration=max_duration, option=option, country=country, category=category,
                                     letter=letter, video_type=video_type, search=search, rel_url=None, channel=channel)
            has_next = page_result['has_next']
            videos.extend(page_result['videos'])
            page += 1
    if '-' in pages:
        pages = str(pages).split('-')
        start_page = int(pages[0])
        end_page = int(pages[1]) + 1
        for page in range(start_page, end_page):
            page_result = get_videos(subdomain=subdomain, page=page, hd=hd, min_duration=min_duration,
                                     max_duration=max_duration, option=option, country=country, category=category,
                                     letter=letter, video_type=video_type, search=search, rel_url=None, channel=channel)
            videos.extend(page_result['videos'])
    return videos
