import json
from collections import defaultdict
from pathlib import Path
from pprint import pprint

from ph_scraper_api.ph_scraper_api.ph_page import get_video_details, get_channel_details
from ph_scraper_api.ph_scraper_api.ph_scraper import search_videos

OUT_PATH = Path().cwd() / 'out'


def main():
    with open('in/ph.json') as json_file:
        ph_search = json.load(json_file)

    results = {'channels': [], 'models': []}
    # for ch in ph_search['channels']:
    #     result = {'channel': get_channel_details(ch),
    #               'videos': filter_free_premium(search_videos(channel=ch, pages='all'))}
    #     # for v in result['videos']:
    #     #     v['details'] = get_video_details(v['video']['rel_url'])
    #     pprint(result['channel'])
    #     results['channels'].append(result)
    # pprint(res)

    for model in ph_search['models']:
        from ph_scraper_api.ph_scraper_api.ph_helper.filter import filter_duration
        result = {'model': None,  # TODO create function to get model infos
                  'videos': filter_duration(search_videos(model=model['name'], pages='all', subdomain='de'),
                                            min_duration=model['min_duration'])}
        # for v in result['videos']:
        #     v['details'] = get_video_details(v['video']['rel_url'])
        pprint(result['videos'])
        results['models'].append(result)

    with open(OUT_PATH / 'free_premium.json', 'w', encoding="utf-8") as f:
        json.dump(results, f, indent=2)


if __name__ == '__main__':
    main()
