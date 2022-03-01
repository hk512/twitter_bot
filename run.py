import logging
import sys
import time

from bot import Bot
import settings

logging.basicConfig(level=logging.INFO, stream=sys.stdout, format='[%(levelname)s][%(asctime)s] %(message)s')
logger = logging.getLogger(__name__)


def main():
    bot = Bot(
        consumer_key=settings.consumer_key,
        consumer_secret=settings.consumer_secret,
        access_token=settings.access_token,
        access_token_secret=settings.access_token_secret
    )

    while True:
        if settings.favorite_enable:

            total_favorite_count = 0

            for word in settings.favorite_words:

                favorite_count = settings.favorite_max_count - total_favorite_count

                if favorite_count <= 0:
                    break

                result = bot.favorite_tweets_by_keyword(word, max_count=favorite_count)
                total_favorite_count += len(result)

        if settings.create_friendships_enable:
            _ = bot.create_friendships_follower(max_count=settings.create_friendships_max_count)

        if settings.destroy_friendships_enable:
            _ = bot.destroy_friendships_unfollower(max_count=settings.destroy_friendships_max_count)

        time.sleep(settings.interval_min * 60)


if __name__ == '__main__':
    main()
