import os
import tweepy
import logging

logger = logging.getLogger()

def main():
    CONSUMER_API_KEY = os.environ["CONSUMER_API_KEY"]
    CONSUMER_API_SECRET = os.environ["CONSUMER_API_SECRET"]
    ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]

    try:
        auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

        api = tweepy.API(auth)
        api.verify_credentials()
        logger.info('Twitter Authenticated')
    except Exception as e:
        logger.error('Error in credentials', exc_info=True)
        raise err


    api.update_status()

if __name__ == "__main__":
    main()
