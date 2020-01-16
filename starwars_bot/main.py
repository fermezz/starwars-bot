import os
import time

from starwars_bot.models import Planet, Person
from starwars_bot.swapi import fetch_random_element
from starwars_bot.twitter import Twitter


class StarWarsBot:

    def __init__(self, resources):
        self.resources = resources
        self.twitter = Twitter(
            os.environ["CONSUMER_API_KEY"],
            os.environ["CONSUMER_API_SECRET_KEY"],
            os.environ["ACCESS_TOKEN"],
            os.environ["ACCESS_TOKEN_SECRET"],
        )

    def run(self):
        while True:
            resource = fetch_random_resource(resources)
            self.twitter.update_status(str(resource))
            print("Sleeping six hours...")
            time.sleep(21600)  # Tweet every six hours.



if __name__ == "__main__":
    StarWarsBot([Planet, Person])
