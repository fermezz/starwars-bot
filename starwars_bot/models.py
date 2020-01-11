from functools import cached_property

import requests

from starwars_bot.utils import make_title_if_unknown


class Planet:

    def __init__(self, **kwargs):

        self.name = kwargs["name"]
        self.rotation_period = kwargs["rotation_period"]
        self.orbital_period = kwargs["orbital_period"]
        self.diameter = kwargs["diameter"]
        self.climate = kwargs["climate"]
        self.gravity = kwargs["gravity"]
        self.terrain = kwargs["terrain"]
        self.surface_water = kwargs["surface_water"]
        self.population = kwargs["population"]
        self.residents = kwargs["residents"]
        self.films = kwargs["films"]


    def __str__(self):
        return f"""- Planet -\n
Name: {self.name.title()}
Climate: {make_title_if_unknown(self.climate)}
Diameter: {make_title_if_unknown(self.diameter)}
Terrain: {make_title_if_unknown(self.terrain)}
Surface Water: {make_title_if_unknown(self.surface_water)}
Population: {make_title_if_unknown(self.population)}
Residents: {", ".join(self.residents_names) if self.residents_names else "Unknown"}
"""

    @cached_property
    def residents_names(self):
        return [requests.get(url=resident).json()["name"] for resident in self.residents]


class Person:

    def __init__(self, **kwargs):

        self.name = kwargs["name"]
        self.height = kwargs["height"]
        self.mass = kwargs["mass"]
        self.hair_color = kwargs["hair_color"]
        self.skin_color = kwargs["skin_color"]
        self.eye_color = kwargs["eye_color"]
        self.birth_year = kwargs["birth_year"]
        self.gender = kwargs["gender"]
        self.homeworld = kwargs["homeworld"]
        # films = kwargs["films"]
        # species = kwargs["species"]
        # vehicles = kwargs["vehicles"]
        # starships = kwargs["starships"]

    def __str__(self):
        return f"""- Character -\n
Name: {self.name.title()}
Height: {self.height}cm
Mass: {self.mass}{"kg" if self.mass != "unknown" else ""}
Gender: {make_title_if_unknown(self.gender)}
Hair Color: {make_title_if_unknown(self.hair_color)}
Eye Color: {make_title_if_unknown(self.eye_color)}
Birth Year: {make_title_if_unknown(self.birth_year)}
Homeworld: {self.homeworld_name.title()}
"""

    @property
    def homeworld_name(self):
        return requests.get(url=self.homeworld).json()["name"]
