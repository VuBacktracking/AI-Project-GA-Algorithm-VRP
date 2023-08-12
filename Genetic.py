import random
from Chromosome import TourManager, Tour
from Population import Population

class Genetic:
    def __init__(self, tourmanager, num_generations):
        self.tourmanager = tourmanager
        self.num_generations = num_generations
        self.mutationRate = 0.01
        self.tournamentSize = 5
        self.elitism = True

    def evolveCostPopulation(self, pop: Population):
        best_population = self.NaturalCostSelection(pop)
        for i in range(0, self.num_generations):
            best_population = self.NaturalCostSelection(best_population)
        return best_population

    def NaturalCostSelection(self, pop: Population):
        newPopulation = Population(self.tourmanager, pop.populationSize(), False)
        elitismOffset = 0
        if self.elitism:
            newPopulation.saveTour(0, pop.getFittestCost())
            elitismOffset = 1

        for i in range(elitismOffset, newPopulation.populationSize()):
            parent1 = self.tournamentCostSelection(pop)
            parent2 = self.tournamentCostSelection(pop)
            offspring = self.crossover(parent1, parent2)
            newPopulation.saveTour(i, offspring)

        for i in range(elitismOffset, newPopulation.populationSize()):
            self.mutate(newPopulation.getTour(i))

        return newPopulation

    def evolveCoorDistancePopulation(self, pop: Population):
        best_population = self.NaturalCoorDistanceSelection(pop)
        for i in range(0, self.num_generations):
            best_population = self.NaturalCoorDistanceSelection(best_population)
        return best_population

    def NaturalCoorDistanceSelection(self, pop: Population):
        newPopulation = Population(self.tourmanager, pop.populationSize(), False)
        elitismOffset = 0
        if self.elitism:
            newPopulation.saveTour(0, pop.getFittestCoorDistance())
            elitismOffset = 1

        for i in range(elitismOffset, newPopulation.populationSize()):
            parent1 = self.tournamentCoorDistanceSelection(pop)
            parent2 = self.tournamentCoorDistanceSelection(pop)
            offspring = self.crossover(parent1, parent2)
            newPopulation.saveTour(i, offspring)

        for i in range(elitismOffset, newPopulation.populationSize()):
            self.mutate(newPopulation.getTour(i))

        return newPopulation

    def crossover(self, parent1, parent2):
        offspring = Tour(self.tourmanager)

        startPos, endPos = sorted(random.sample(range(parent1.tour_size()), 2))
        for i in range(startPos, endPos):
            offspring.set_city(i, parent1.get_city(i))

        for i in range(0, parent2.tour_size()):
            if not offspring.contains_city(parent2.get_city(i)):
                for j in range(0, offspring.tour_size()):
                    if offspring.get_city(j) == None:
                        offspring.set_city(j, parent2.get_city(i))
                        break
        return offspring

    def mutate(self, tour):
        for tourPos1 in range(0, tour.tour_size()):
            if random.random() < self.mutationRate:
                tourPos2 = int(tour.tour_size() * random.random())

                city1 = tour.get_city(tourPos1)
                city2 = tour.get_city(tourPos2)

                tour.set_city(tourPos2, city1)
                tour.set_city(tourPos1, city2)

    def tournamentCostSelection(self, pop : Population):
        tournament = Population(self.tourmanager, self.tournamentSize, False)
        for i in range (0, self.tournamentSize):
            randomId = int(random.random() * pop.populationSize())
            tournament.saveTour(i, pop.getTour(randomId))
        fittest = tournament.getFittestCost()
        return fittest

    def tournamentCoorDistanceSelection(self, pop: Population):
        tournament = Population(self.tourmanager, self.tournamentSize, False)
        for i in range(0, self.tournamentSize):
            randomId = int(random.random() * pop.populationSize())
            tournament.saveTour(i, pop.getTour(randomId))
        fittest = tournament.getFittestCoorDistance()
        return fittest