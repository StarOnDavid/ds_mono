import os
from pathlib import Path

from easy_insta_api import api_loggin_settings as log
from easy_insta_api import filehandler as file
from easy_insta_api import item
from easy_insta_api.connection import Connection
from easy_insta_api.json_helper import read_json, write_json

module_path = Path(os.path.dirname(os.path.abspath(__file__)))
insta_example_path = module_path / 'insta_examples'

con = Connection('star.on.david', 'KOD59-insta', module_path / 'credentials' / 'david.json')
media_path = module_path / 'media' / con.api.username

# get own feed and download item files #######################
rank_token = con.api.generate_uuid()
user_id = con.api.authenticated_user_id

feed = con.api.usertag_feed('419892679')

write_json(feed, insta_example_path / 'usertag_feed_2.json')

# print(feed)
# for elem in feed:
#     # print(item.get_media_candidates(elem))
#     if elem['media_type'] == 2:
#         print(elem)
#     file.download_item(item.get_media_candidates(elem), media_path)

# item.get_media_candidates(item)
# following_user_names_ids = {}
# for user in results['users']:
#     print('********* USER ********')
#     print(user['username'] + ' {}'.format(user['pk']))
#     print()
#     following_user_names_ids[user['username']] = user['pk']
#     # for user in users:
#     #     print('USER ' + user)
#
# user_feed = client.user_feed(following_user_names_ids['jandammpictures'])
# picture_urls = []
# for elem in user_feed['items']:
#     print('\n **************** Element *****************')
#     print(elem)
#     if elem['media_type'] == 8:
#         for car_m in elem['carousel_media']:
#             for e in car_m['image_versions2']['candidates']:
#                 print(e)
#             picture_urls.append(car_m['image_versions2']['candidates'][0]['url'])
#
#     if elem['media_type'] == 1:
#         for e in elem['image_versions2']['candidates']:
#             print(e)
#         picture_urls.append(elem['image_versions2']['candidates'][0]['url'])
#
# for pic_url in picture_urls:
#     print(pic_url)
