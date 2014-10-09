#! /bin/env python
import numpy as np
from random import randint, choice
from math import sqrt

class Ant(object):
    
    def __init__(self, points, alpha, beta):
        """
        points must be a list of lists of points
        alpha and beta are the respective scaling factors for J and d
        """
        self.startPointIndex = randint(0, len(points)-1)
        self.points = points
        self.alpha = alpha
        self.beta = beta
        
    def nextLocations(visitedPoints, pheromones):
        """
        moves a given ant to a new point from remaining points
        """
        numerators = []
        notVisitedPoints = []
        for i in range(len(self.points)):
            if self.points[i] not in visitedPoints:
                possiblePoint = self.points[i]
                lastPoint = visitedPoints[-1]
                distance = sqrt((possiblePoint[0] - lastPoint[0])**2 + (possiblePoint[1] - lastPoint[1])**2)
                pheromoneLevel = pheromone[self.points.index(possiblePoint)][self.points.index(lastPoint)]
                numerator = self.alpha*pheromoneLevel + self.beta*(1/distance)
                numerators.append(numerator)
                notVisitedPoints.append(self.points[i])
        denominator = np.cumcum(numerators)
        probabilities = []
        for numerator in numerators:
            probabilities.append(100.*numerator/demoninator)
        weightedIndexes = []
        for i in range(len(notVisitedPoints)):
            index = self.points.index(notVisitedPoints[i])
            weightedIndexes += [index]*probabilities[i]
        newPoint = self.points[choice(weightedIndexes)]
        return newPoint

    def takeATour(pheromones):
        """
        take all points and make a given ant move to that point 
        """
        visitedPoints = self.points[self.startPointIndex]
        for i in range(len(self.points)-1):
            newLocation = nextLocation(visitedPoints, pheromones)
            visitedPoints.append(newLocation)
        return visitedPoints.append(self.points[startPointIndex])

class AntWorld(object):

    def __init__(self, points, alpha, beta, ants, evaporation):
        self.points = points
        self.alpha = alpha
        self.beta = beta
        self.evaporation = evaporation
        self.ants = []
        '''make empty pheromones'''
        pheromones = []
        for i in range(len(points)-1):
            row = []
            for j in range(len(points)-1):
                 row.append(0)
            pheromones.append(row)
        self.pheromones = pheromones
        '''create list of ant instances'''
        for i in range(ants):
            self.ants.append(Ant(points, alpha, beta))
    
    def updatePheromones(tours):
        """
        update pheromone levels in world
        """
        for tour in tours:
            distance = 0
            for i in range(len(tour)-2):
                distance += sqrt((tour[i][0]-tour[i+1][0])**2 + (tour[i][1]-tour[i+1][1])**2)
            for i in range(len(tour)-2):
                self.pheromones[self.points.index(tour[i])][self.points.index(tour[i+1])] = 1/distance + self.evaporation*self.pheromones[self.points.index(tour[i])][self.points.index(tour[i+1])]
                self.pheromones[self.points.index(tour[i+1])][self.points.index(tour[i])] = 1/distance + self.evaporation*self.pheromones[self.points.index(tour[i+1])][self.points.index(tour[i])] 
        
    def antTours():
        tourPoints = []
        for ant in self.ants:
            tourPoints.append(ant.takeATour(self.pheromones))
        updatePheromones(tourPoints) 

    def generateTours(generations):
        for i in range(generations):
            antTours()
    
if __name__ == "__main__":
	
    alpha = 1.
    beta = 1.
    evaporation = .75
    points = [[1.,2.], [3.,2.], [5.,10.], [1.5, .3], [0.,0.]]
    ants = 20
    generations = 5
    antworld = AntWorld(points, alpha, beta, ants, evaporation)
    antworld.generateTours(1)


