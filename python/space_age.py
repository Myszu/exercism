class SpaceAge:
    def __init__(self, seconds):
        self.earth_year = 31557600
        self.seconds = seconds

    def on_mercury(self):
        correction = 0.2408467
        return round(self.seconds / (self.earth_year * correction), 2)

    def on_venus(self):
        correction = 0.61519726
        return round(self.seconds / (self.earth_year * correction), 2)

    def on_earth(self):
        correction = 1
        return round(self.seconds / (self.earth_year * correction), 2)

    def on_mars(self):
        correction = 1.8808158
        return round(self.seconds / (self.earth_year * correction), 2)

    def on_jupiter(self):
        correction = 11.862615
        return round(self.seconds / (self.earth_year * correction), 2)

    def on_saturn(self):
        correction = 29.447498
        return round(self.seconds / (self.earth_year * correction), 2)

    def on_uranus(self):
        correction = 84.016846
        return round(self.seconds / (self.earth_year * correction), 2)

    def on_neptune(self):
        correction = 164.79132
        return round(self.seconds / (self.earth_year * correction), 2)
