import math

class City:
    def __init__(self, id, name = None, longitude=None, latitude=None):
        self.id = id
        if name is not None:
            self.name = name
        else:
            self.name = None
        self.longitude = longitude
        self.latitude = latitude
        self.matrix = []

    def __repr__(self):
        return str(self.getID()) + ', ' + self.name + f": ({str(self.getLatitude())}, {str(self.getLongitude())})"

    def getID(self):
        return str(self.id)

    def getName(self):
        return str(self.name)
    
    def getLatitude(self):
        return self.latitude

    def getLongitude(self):
        return self.longitude

    def get_coordinates(self):
        return [self.latitude, self.longitude]

    def get_cost_matrix(self):
        return self.matrix

    def distanceTo(self, city):
        xDistance = abs(self.getLongitude() - city.getLongitude())
        yDistance = abs(self.getLatitude() - city.getLatitude())
        distance = math.sqrt((xDistance * xDistance) + (yDistance * yDistance))
        return distance