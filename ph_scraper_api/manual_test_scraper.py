import json
from collections import defaultdict
from pathlib import Path
from pprint import pprint

from ph_scraper_api.ph_scraper_api.ph_helper.filter import filter_free_premium
from ph_scraper_api.ph_scraper_api.ph_page import get_video_details, get_channel_details
from ph_scraper_api.ph_scraper_api.ph_scraper import search_videos

SEARCH_CHANNELS = ['babes', 'bratty-sis', 'step-siblings-caught', 'the-white-boxxx', 'property-sex', 'my-family-pies',
                   'letsdoeit', 'nubilefilms', 'princess-cum', 'momsteachsex', 'dad-crush', 'exxxtrasmall',
                   'step-siblings-caught', 'digitalplayground', 'newsensations', 'familyxxx',
                   'spy-fam', 'hot-wife-xxx', 'pornpros', 'fitness-rooms', 'girl-cum', 'momsteachsex',
                   'mylf', 'sis-loves-me', 'nanny-spy', 'daughter-swap', 'baeb', 'passion-hd', 'creepy-pa',
                   'horny-hostel', 'skeet-society']
OUT_PATH = Path().cwd() / 'out'


def main():
    results = {'porn_hub': []}
    for ch in SEARCH_CHANNELS:
        result = {'channel': get_channel_details(ch),
                  'videos': filter_free_premium(search_videos(channel=ch, pages='all'))}
        # for v in result['videos']:
        #     v['details'] = get_video_details(v['video']['rel_url'])
        pprint(result['channel'])
        results['porn_hub'].append(result)
    # pprint(res)

    with open(OUT_PATH / 'free_premium.json', 'w', encoding="utf-8") as f:
        json.dump(results, f, indent=2)


if __name__ == '__main__':
    main()
