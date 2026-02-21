"""Given an age in seconds, calculate how old someone would be on a planet in our Solar System"""

class SpaceAge:
    __earth_year = 31_557_600 # in seconds
    __planets = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132
    }

    def __init__(self, seconds):
        self.seconds = seconds

    def planet_age(self, planet):
        return round(self.seconds / (SpaceAge.__earth_year * SpaceAge.__planets[planet]), 2)

    def on_mercury(self):
        return self.planet_age("mercury")

    def on_venus(self):
        return self.planet_age("venus")

    def on_earth(self):
        return self.planet_age("earth")

    def on_mars(self):
        return self.planet_age("mars")

    def on_jupiter(self):
        return self.planet_age("jupiter")

    def on_saturn(self):
        return self.planet_age("saturn")

    def on_uranus(self):
        return self.planet_age("uranus")

    def on_neptune(self):
        return self.planet_age("neptune")