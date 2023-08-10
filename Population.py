from Chromosome import Tour, TourManager
from City import City

class Population:
    def __init__(self, tourmanager, populationSize, initialise):
        self.tours = []
        for i in range(0, populationSize):
            self.tours.append(None)

        if initialise:
            for i in range(0, populationSize):
                newTour = Tour(tourmanager)
                newTour.generate_individual()
                self.saveTour(i, newTour)

    def __setitem__(self, key, value):
        self.tours[key] = value

    def __getitem__(self, index):
        return self.tours[index]

    def saveTour(self, index, tour):
        self.tours[index] = tour

    def getTour(self, index):
        return self.tours[index]

    def getFittestDistance(self):
        fittest = self.tours[0]
        for i in range(0, self.populationSize()):
            if fittest.get_fitnessDistance() <= self.getTour(i).get_fitnessDistance():
                fittest = self.getTour(i)
        return fittest

    def getFittestCost(self):
        fittest = self.tours[0]
        for i in range (0, self.populationSize()):
            if fittest.get_fitnessCost() <= self.getTour(i).get_fitnessCost():
                fittest = self.getTour(i)
        return fittest

    def getFittestCoorDistance(self):
        fittest = self.tours[0]
        for i in range(0, self.populationSize()):
            if fittest.get_fitnessCoorDistance() <= self.getTour(i).get_fitnessCoorDistance():
                fittest = self.getTour(i)
        return fittest

    def populationSize(self):
        return len(self.tours)