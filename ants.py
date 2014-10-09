#! /bin.env python
import numpy as np
from random import randint, choice
from math import sqrt

class ant(object):
    
    def __init__(self, points, alpha, beta):
        """
        points must be a list of lists of points
        alpha and beta are the respective scaling factors for J and d
        """
        self.startpointIndex = randint(0, len(points)-1)
        self.points = points
        self.alpha = alpha
        self.beta = beta
        pharamones = []
        for i in range(len(points)-1):
            row = []
            for j in range(len(points)-1):
                 row.append(0)
            pharamones.append(row)
        self.pharamones = pharamones

    def pheremoneUpdate(tour):
        """
        updates pheramone level for a given ant after one tour. tour is probs a list 
        """

    def nextLocations(visitedPoints):
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
                pheramoneLevel = self.pheramone[self.points.index(possiblePoint)][self.points.index(lastPoint)]
                numerator = self.alpha*pheramoneLevel + self.beta*(1/distance)
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

    def takeATour():
        """
        take all points and make a given ant move to that point 
        """
        visitedPoints = self.points[:self.startPointIndex] + self.points[self.startPointIndex+1:]
        for i in range(len(self.points)-1):
            newLocation = nextLocation(visitedPoints)
            visitedPoints.append(newLocation)

if __name__ == "__main__":
	numberAnts = 20;


