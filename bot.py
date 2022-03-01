import logging

from api_client import Client

logger = logging.getLogger(__name__)


class Bot(object):
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.api_client = Client(consumer_key, consumer_secret, access_token, access_token_secret)

    def get_my_id(self):
        logger.info('action=get_my_id run')
        my_id = None
        res = self.api_client.verify_credentials()

        if res.status_code == 200:
            data = res.json()
            my_id = data['id']
            logger.info(f"action=get_my_id my_id={my_id}")

        logger.info('action=get_my_id end')
        return my_id

    def get_my_followers(self):
        logger.info('action=get_my_followers run')

        ids = None
        my_id = self.get_my_id()

        if my_id is not None:

            res = self.api_client.followers(my_id)

            if res.status_code == 200:
                data = res.json()
                ids = data['ids']
                logger.info(f"action=get_my_followers ids_size={len(ids)}")

        logger.info('action=get_my_followers end')
        return ids

    def get_my_friends(self):
        logger.info('action=get_my_friends run')

        ids = None
        my_id = self.get_my_id()

        if my_id is not None:

            res = self.api_client.friends(my_id)

            if res.status_code == 200:
                data = res.json()
                ids = data['ids']
                logger.info(f"action=get_my_friends ids_size={len(ids)}")

        logger.info('action=get_my_friends end')
        return ids

    def favorite_tweets_by_keyword(self, keyword, max_count=None):
        logger.info('action=favorite_tweets_by_keyword run')

        count = 0
        result = []

        logger.info(f"action=favorite_tweets_by_keyword search_keyword={keyword}")
        res = self.api_client.search_tweets(keyword, 100)

        if res.status_code == 200:

            data = res.json()
            tweet_ids = [status['id'] for status in data['statuses']]
            logger.info(f"action=favorite_tweets_by_keyword get_tweet_count={len(tweet_ids)}")

            for tweet_id in tweet_ids:

                res = self.api_client.favorites(tweet_id)

                if res.status_code == 200:
                    count += 1
                    result.append(tweet_id)

                if res.status_code == 429:
                    logger.warning('action=favorite_tweets_by_keyword Unable to favorite more tweets at this time.')
                    break

                if max_count is not None and max_count <= count:
                    break

        logger.info(f"action=favorite_tweets_by_keyword favorite_count={count}")
        logger.info('action=favorite_tweets_by_keyword end')

        return result

    def destroy_friendships_unfollower(self, max_count=None):
        logger.info('action=destroy_friendships_unfollower run')

        count = 0
        result = []

        follower_ids = self.get_my_followers()
        friend_ids = self.get_my_friends()

        if follower_ids is not None or friend_ids is not None:

            user_ids = list(set(friend_ids) - set(follower_ids))

            for user_id in user_ids:
                res = self.api_client.destroy_friendships(user_id)

                if res.status_code == 200:
                    count += 1
                    result.append(user_id)

                if max_count is not None and max_count <= count:
                    break

        logger.info(f"action=destroy_friendships_unfollower destroy_count={count}")
        logger.info('action=destroy_friendships_unfollower end')
        return result

    def create_friendships_follower(self, max_count=None):
        logger.info('action=create_friendships_follower run')

        count = 0
        result = []

        follower_ids = self.get_my_followers()
        friend_ids = self.get_my_friends()

        if follower_ids is not None or friend_ids is not None:

            user_ids = list(set(follower_ids) - set(friend_ids))

            for user_id in user_ids:
                res = self.api_client.create_friendships(user_id)

                if res.status_code == 200:
                    count += 1
                    result.append(user_id)

                if res.status_code == 161:
                    logger.warning('action=create_friendships_follower Unable to follow more people at this time.')
                    break

                if max_count is not None and max_count <= count:
                    break

        logger.info(f"action=create_friendships_follower create_count={count}")
        logger.info('action=create_friendships_follower end')
        return result
