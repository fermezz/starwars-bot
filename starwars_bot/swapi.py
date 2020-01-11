import random

import requests

from starwars_bot.models import Person, Planet


resource_name_translation_map = {
    Person: "people",
    Planet: "planets",
}

max_quantity_of_resource_translation_map = {
    Person: 88,
    Planet: 61,
}


def fetch_random_element(elements):

	random.shuffle(elements)
	element = elements[0]

	number = random.randint(1, max_quantity_of_resource_translation_map[element])
	resource_name = resource_name_translation_map[element]

	url = f"https://swapi.co/api/{resource_name}/{number}/"

	return element(**requests.get(url=url).json())
