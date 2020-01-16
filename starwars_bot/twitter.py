import tweepy


class Twitter:

    def __init__(
        self,
        consumer_api_key,
        consumer_api_secret_key,
        access_token,
        access_token_secret,
    ):
        auth = tweepy.OAuthHandler(consumer_api_key, consumer_api_secret_key)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth)

    def update_status(text):
        self.api.update_status(text)
