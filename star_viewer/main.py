from pathlib import Path

from star_viewer.insta_api.connection import Connection
from star_viewer.insta_api.json_helper import write_json

PACKAGE_PATH = Path.cwd()
DATA_PATH = PACKAGE_PATH / 'data'

def main():
    con = Connection('star.on.david', 'KOD59-insta', PACKAGE_PATH / 'insta_api' / 'insta_credentials' / 'david.json')

    user_id = con.api.authenticated_user_id
    rank_token = con.api.generate_uuid()
    print("user id ", user_id)

    users_following = con.get_following()


    users_real_media = []
    for user in users_following:
        real_media = con.api.user_reel_media(user['pk'])
        print(real_media)
        if real_media['latest_reel_media']:
            users_real_media.append(real_media)
        if len(users_real_media) == 20:
            break

    sorted_users_real_media = {'real_media': sorted(users_real_media, key=lambda d: d['latest_reel_media'])}
    for rm in users_real_media:
        print("-"*30 + "NEXT" + "-"*30 +"\n")
        print(rm)
        print("\n\n\n")

    write_json(sorted_users_real_media, DATA_PATH / 'sorted_users_real_media.json')

    # user_story_feed = con.api.user_reel_media(2017121878)
    # folrian uid 254648062
    # dasyi uid 2017121878
    # user_story_feed = con.api.user_story_feed(254648062)
    # print("story_feed", user_story_feed)


if __name__ == "__main__":
    main()