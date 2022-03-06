import json
from pathlib import Path

DATA_PATH = Path().cwd() / 'ph_data'


def create_url(search_page):

    def create_option_entry(opt_val):
        with open(DATA_PATH / 'option.json', "r", encoding="utf-8") as f:
            opt_vals = json.load(f)

        if 'channels/' in search_page['search']:
            return 'o', opt_vals['channels/xy'][opt_val]
        if search_page['search'] == 'channels':
            return 'o', opt_vals['channels'][opt_val]
        else:
            return 'o', opt_vals['video'][opt_val]

    def create_country_entry(opt_val):
        with open(DATA_PATH / 'country.json', "r", encoding="utf-8") as f:
            cc_vals = json.load(f)

        return 'cc', cc_vals[opt_val]

    def create_category_entry(opt_val):
        with open(DATA_PATH / 'category.json', "r", encoding="utf-8") as f:
            c_vals = json.load(f)
        category = c_vals[opt_val]

        if category['id'] is None:
            search_page['search'] = category['search']
            return None, None
        else:
            return 'c', category['id']

    def create_query():
        query_string = ''
        for q_key, q_val in search_page['query'].items():
            if q_val:
                if q_key == 'option':
                    q_key, q_val = create_option_entry(q_val)
                if q_key == 'country':
                    q_key, q_val = create_country_entry(q_val)
                if q_key == 'category':
                    q_key, q_val = create_category_entry(q_val)

                if q_key == 'letter':
                    q_key = 'l'
                if q_key == 'video_type':
                    q_key = 'p'
                if q_key == 'search' and 'channels' in search_page['search']:
                    q_key = 'channelSearch'

                if q_key is None or q_val is None:
                    continue

                if query_string != '':
                    query_string = query_string + '&' + q_key + '=' + str(q_val)
                else:
                    query_string = '?' + q_key + '=' + str(q_val)
        return query_string

    if type(search_page) is dict:
        # has side effects
        query = create_query()

        base_url = 'https://pornhub.com/' + search_page['search']
        if search_page['subdomain']:
            base_url = 'https://' + search_page['subdomain'] + '.pornhub.com/' + search_page['search']
        url = base_url + query
    if type(search_page) is str:
        url = 'https://pornhub.com/' + search_page
    print('SEARCH URL', url)
    return url
