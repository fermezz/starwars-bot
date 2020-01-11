import os

import tweepy


def update_status(text):
    auth = tweepy.OAuthHandler(
        os.environ["CONSUMER_API_KEY"],
        os.environ["CONSUMER_API_SECRET_KEY"],
    )
    auth.set_access_token(
        os.environ["ACCESS_TOKEN"],
        os.environ["ACCESS_TOKEN_SECRET"],
    )

    api = tweepy.API(auth)
    api.update_status(text)
