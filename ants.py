#! /bin/env python
import numpy as np
from random import randint, choice
from math import sqrt
import matplotlib.pyplot as plt
import networkx as nx

class Ant(object):
    
    def __init__(self, points, alpha, beta):
        """
        points must be a list of lists of points
        alpha and beta are the respective scaling factors for J and d
        """
        #self.startPointIndex = randint(0, len(points)-1)
        self.startPointIndex = 0
        self.points = points
        self.alpha = alpha
        self.beta = beta
        
    def nextLocation(self, visitedPoints, pheromones):
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
                indexI = self.points.index(possiblePoint)
                indexJ = self.points.index(lastPoint)
                pheromoneLevel = pheromones[indexI][indexJ]
                numerator = self.alpha*pheromoneLevel + self.beta*(1/distance)
                numerators.append(numerator)
                notVisitedPoints.append(self.points[i])
        denominator = sum(numerators)
        probabilities = []
        for numerator in numerators:
            probabilities.append(int(100*numerator/denominator))
        weightedIndexes = []
        for i in range(len(notVisitedPoints)):
            index = self.points.index(notVisitedPoints[i])
            weightedIndexes += [index]*probabilities[i]
        newPoint = self.points[choice(weightedIndexes)]
        return newPoint

    def takeATour(self, pheromones):
        """
        take all points and make a given ant move to that point 
        """
        visitedPoints = [self.points[self.startPointIndex]]
        for i in range(len(self.points)-1):
            newLocation = self.nextLocation(visitedPoints, pheromones)
            visitedPoints.append(newLocation)
        visitedPoints.append(self.points[self.startPointIndex])
        return visitedPoints

class AntWorld(object):

    def __init__(self, points, alpha, beta, ants, evaporation):
        self.points = points
        self.alpha = alpha
        self.beta = beta
        self.evaporation = evaporation
        self.pheromones = np.zeros([len(self.points), len(self.points)])
        np.fill_diagonal(self.pheromones, -1)
        self.ants = [Ant(points, alpha, beta) for a in range(ants)]
    
    def updatePheromones(self,tours):
        """
        update pheromone levels in world
        """
        for tour in tours:
            distance = 0
            '''not sure about the -1... might be -2?'''
            for i in range(len(tour)-1):
                distance += sqrt(
                        (tour[i][0]-tour[i+1][0])**2 
                        + (tour[i][1]-tour[i+1][1])**2
                        )
            for i in range(len(tour)-1):
                self.pheromones[self.points.index(tour[i])][self.points.index(tour[i+1])] = (
                        1/distance 
                        + self.evaporation
                        * self.pheromones[self.points.index(tour[i])][self.points.index(tour[i+1])]
                        )
                self.pheromones[self.points.index(tour[i+1])][self.points.index(tour[i])] = (
                        1/distance 
                        + self.evaporation
                        * self.pheromones[self.points.index(tour[i+1])][self.points.index(tour[i])]
                        )
        
    def antTours(self):
        tourPoints = []
        for ant in self.ants:
            tourPoints.append(ant.takeATour(self.pheromones))
        self.updatePheromones(tourPoints) 

    def generateTours(self, generations):
        for i in range(generations):
            self.antTours()

    def draw(self):
        G = nx.Graph()
        edge_colors = list()
        min_pher = np.ma.masked_equal(self.pheromones, -1, copy=False).min()
        max_pher = np.max(self.pheromones)
        for i in range(len(self.points)):
            G.add_node(i, posxy=(points[i]))
            for j in range(i):
                G.add_edge(i, j)
                edge_color = tuple((1-(self.pheromones[i][j])/(max_pher-min_pher) for c in range(len('rgb'))))
                edge_colors.append(edge_color)
        pos = nx.get_node_attributes(G, 'posxy')
        nx.draw(
                G,
                pos,
                node_size=200,
                edge_color=edge_colors,
                width=3,
                )
        plt.show()
    
if __name__ == "__main__":
	
    alpha = 1 
    beta = 1
    evaporation = .75
    points = [[0., 0.], [3.,0.], [4., 2.], [3, 3.], [2., 2.]]
    ants = 1
    generations = 2
    antworld = AntWorld(points, alpha, beta, ants, evaporation)
    antworld.generateTours(generations)
    antworld.draw()
