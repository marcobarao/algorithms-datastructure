class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds
    
    def on_earth(self):
        years = self.seconds / 60 / 60 / 24 / 365.25
        return round(years, 2)

    def on_mercury(self):
        years = self.on_earth() / 0.2408467
        return round(years, 2)

    def on_venus(self):
        years = self.on_earth() / 0.61519726
        return round(years, 2)
    
    def on_mars(self):
        years = self.on_earth() / 1.8808158
        return round(years, 2)

    def on_jupiter(self):
        years = self.on_earth() / 11.862615
        return round(years, 2)

    def on_saturn(self):
        years = self.on_earth() / 29.447498
        return round(years, 2)

    def on_uranus(self):
        years = self.on_earth() / 84.016846
        return round(years, 2)

    def on_neptune(self):
        years = self.on_earth() / 164.79132
        return round(years, 2)
