import time

from starwars_bot.models import Planet, Person
from starwars_bot.swapi import fetch_random_element
from starwars_bot.twitter import update_status


if __name__ == "__main__":
    elements = [Planet, Person]
    while True:
        element = fetch_random_element(elements)
        update_status(str(element))
        print("Sleeping six hours...")
        time.sleep(21600)  # Tweet every six hours.
