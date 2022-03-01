import logging

from requests_oauthlib import OAuth1Session

logger = logging.getLogger(__name__)


class Client(object):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.session = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)

    def search_tweets(self, word, count, result_type='recent', lang='ja'):
        res = self.session.get(
            url='https://api.twitter.com/1.1/search/tweets.json',
            params={
                'q': word.encode('utf-8'),
                'lang': lang,
                'result_type': result_type,
                'count': str(count)
            }
        )

        if res.status_code != 200:
            logger.error(f"action=search_tweets status_code={res.status_code} text={res.text}")

        return res

    def show_user(self, user_id):
        res = self.session.get(
            url='https://api.twitter.com/1.1/users/show.json',
            params={
                'user_id': user_id
            }
        )

        if res.status_code != 200:
            logger.error(f"action=show_user status_code={res.status_code} text={res.text}")

        return res

    def home_timeline(self, count):

        res = self.session.get(
            url='https://api.twitter.com/1.1/statuses/home_timeline.json',
            params={
                'count': str(count)
            }
        )

        if res.status_code != 200:
            logger.error(f"action=home_timeline status_code={res.status_code} text={res.text}")

        return res

    def followers(self, user_id):

        res = self.session.get(
            url='https://api.twitter.com/1.1/followers/ids.json',
            params={
                'user_id': user_id
            }
        )

        if res.status_code != 200:
            logger.error(f"action=followers status_code={res.status_code} text={res.text}")

        return res

    def friends(self, user_id):

        res = self.session.get(
            url='https://api.twitter.com/1.1/friends/ids.json',
            params={
                'user_id': user_id
            }
        )

        if res.status_code != 200:
            logger.error(f"action=friends status_code={res.status_code} text={res.text}")

        return res

    def create_friendships(self, user_id):

        res = self.session.post(
            url='https://api.twitter.com/1.1/friendships/create.json',
            params={
                'user_id': user_id
            }
        )

        if res.status_code != 200:
            logger.error(f"action=create_friendships status_code={res.status_code} text={res.text}")

        return res

    def destroy_friendships(self, user_id):

        res = self.session.post(
            url='https://api.twitter.com/1.1/friendships/destroy.json',
            params={
                'user_id': user_id
            }
        )

        if res.status_code != 200:
            logger.error(f"action=destroy_friendships status_code={res.status_code} text={res.text}")

        return res

    def verify_credentials(self):

        res = self.session.get(
            url='https://api.twitter.com/1.1/account/verify_credentials.json'
        )

        if res.status_code != 200:
            logger.error(f"action=verify_credentials status_code={res.status_code} text={res.text}")

        return res

    def favorites(self, tweet_id):

        res = self.session.post(
            url='https://api.twitter.com/1.1/favorites/create.json',
            params={
                "id": tweet_id,
            }
        )

        if res.status_code != 200:
            logger.error(f"action=favorites status_code={res.status_code} text={res.text}")

        return res
