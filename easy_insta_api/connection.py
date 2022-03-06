from easy_insta_api import api_loggin_settings as logger
from easy_insta_api import connection_to_instagram_private_api

log = logger.get(__name__)


class Connection:
    def __init__(self, username, pw, cr_file_path):
        log.info('Setup connection')
        self.api = connection_to_instagram_private_api.get(username, pw, cr_file_path)
        self.rank_token = self.api.generate_uuid()
        self.user_id = self.api.authenticated_user_id

    def get_own_feed(self):
        log.info('Get own feed of: ' + self.api.username)
        feed = self.api.self_feed()
        feed_items = []
        feed_items.extend(feed['items'])
        while feed['more_available']:
            log.debug('Feed content')
            log.debug(feed)
            feed = self.api.self_feed(max_id=feed['next_max_id'])
            feed_items.extend(feed['items'])
        return feed_items

    def get_followers(self):
        log.info('Get followers of: ' + self.api.username)
        following = self.api.user_followers(self.user_id, self.rank_token)
        following_users = []
        following_users.extend(following['users'])
        while following['big_list']:
            following = self.api.user_followers(self.user_id, self.rank_token, max_id=following['next_max_id'])
            following_users.extend(following['users'])
        return following_users

    def get_following(self):
        log.info('Get following of: ' + self.api.username)
        following = self.api.user_following(self.user_id, self.rank_token)
        following_users = []
        following_users.extend(following['users'])
        while following['big_list']:
            following = self.api.user_following(self.user_id, self.rank_token, max_id=following['next_max_id'])
            following_users.extend(following['users'])
        return following_users
