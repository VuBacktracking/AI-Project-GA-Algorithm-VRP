from City import City
import random

class Tour:
    def __init__(self, tourmanager, tour=None):
        self.tourmanager = tourmanager
        self.tour = []
        self.fitness_distance = 0.0
        self.distance = 0.0
        self.cost = 0.0
        self.fitness_cost = 0.0
        self.fitness_coordistance = 0.0
        self.coordistance = 0.0

        if tour is not None:
            self.tour = tour
        else:
            for i in range(0, self.tourmanager.numberOfCities()):
                self.tour.append(None)

    def __len__(self):
        return len(self.tour)

    def __getitem__(self, index):
        return self.tour[index]

    def __setitem__(self, key, value):
        self.tour[key] = value

    def __repr__(self):
        id_list = [city.getID() for city in self.tour]
        answer = ' -> '.join(id_list)
        return answer

    def get_city(self, tourPosition):
        return self.tour[tourPosition]

    def set_city(self, tourPosition, city):
        self.tour[tourPosition] = city
        self.fitness_distance = 0.0
        self.distance = 0.0
        self.fitness_cost = 0.0
        self.cost = 0.0
        self.fitness_coordistance = 0.0
        self.coordistance = 0.0

    def generate_individual(self):
        for cityIndex in range(0, self.tourmanager.numberOfCities()):
            self.set_city(cityIndex, self.tourmanager.get_city(cityIndex))
        random.shuffle(self.tour)

    def get_fitnessCost(self):
        if self.fitness_cost == 0:
            self.fitness_cost = 1 / float(self.getCost())
        return self.fitness_cost

    def getCost(self):
        if self.cost == 0:
            tourCost = 0
            for cityIndex in range(0, self.tour_size() - 1):
                fromCity = self.get_city(cityIndex)
                indexDestination = self.get_city(cityIndex + 1).id - 1
                tourCost += fromCity.cost_matrix[indexDestination]
            fromCity = self.get_city(-1)
            indexDestination = self.get_city(0).id - 1
            tourCost += fromCity.cost_matrix[indexDestination]
            self.cost = tourCost * 1000
        return self.cost
    
    def get_fitnessCoorDistance(self):
        if self.fitness_coordistance == 0:
            self.fitness_coordistance = 1 / float(self.getCoorDistance())
        return self.fitness_coordistance

    def getCoorDistance(self):
        if self.distance == 0:
            tourDistance = 0
            for cityIndex in range(0, self.tour_size() - 1):
                fromCity = self.get_city(cityIndex)
                destinationCity = self.get_city(cityIndex + 1)
                tourDistance += fromCity.distanceTo(destinationCity)
            fromCity = self.get_city(self.tour_size()-1)
            destinationCity = self.get_city(0)
            tourDistance += fromCity.distanceTo(destinationCity)
            self.distance = tourDistance
        return self.distance

    def tour_size(self):
        return len(self.tour)

    def contains_city(self, city):
        return city in self.tour

    def get_answer_for_coord(self):
        id_list = [str(city.getID()) for city in self.tour]
        answer = ' -> '.join(id_list)
        return answer

    def get_answer_for_apply(self):
        name_list = [str(city.getName()) for city in self.tour]
        answer = ' -> '.join(name_list)
        return answer

class TourManager:
    destinationCities = []

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.destinationCities):
            result = self.destinationCities[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration

    def add_city(self, city):
        self.destinationCities.append(city)

    def get_city(self, index):
        return self.destinationCities[index]

    def get_city_name(self, name):
        for cityIndex in range(len(self.destinationCities)):
            if self.get_city(cityIndex).name == name:
                return self.get_city(cityIndex)

    def numberOfCities(self):
        return len(self.destinationCities)

    def read_file_coor_tour(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                city_data = line.strip().split(" ")
                city_id = int(city_data[0])
                longitude = float(city_data[1])
                latitude = float(city_data[2])
                city = City(city_id, longitude=longitude, latitude=latitude)
                self.add_city(city)

    def read_file_tour(self, filename):
        f = open(filename, encoding = "utf8")
        for i in f.readlines():
            node_city_val = i.split("\t")
            id, name, x, y = int(node_city_val[0]), node_city_val[1], float(node_city_val[2]), float(node_city_val[3])
            self.add_city(City(id, name, x, y))

    def read_file_matrix(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        for i in range(len(lines)):
            values = lines[i].split("\t")
            costs = [float(cost) for cost in values]
            self.get_city(i).cost_matrix = costs

    def reset_tour(self):
        return self.destinationCities.clear()