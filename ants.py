from random import randint

def pheremoneUpdate(tour):
	"""
	updates pheramone level for a given ant after one tour. tour is probs a list 
	"""

def nextLocations(visitedPoints, points):
	"""
	moves a given ant to a new point from remaining points
	"""
	for i in range(len(points)):
		if points[i] not in visitedPoints:
			possiblePoint = points[i]
			lastPoint = visitedPoints[-1]
			distance = sqrt((possiblePoint[0] - lastPoint[0])**2 + (possiblePoint[1] - lastPoint[1])**2)
			pheramoneLevel = pheramone[i]


def takeATour(alpha,beta,points):
	"""
	take all points and make a given ant move to that point 
	"""
	startPointIndex = randint(0,len(points)-1)
	visitedPoints = points[:startPointIndex] + points[startPointIndex:]
	for i in range(len(points)-1):
		newLocation = nextLocation(visitedPoints)
		visitedPoints.append(newLocation)




if __name__ == "__main__":
	numberAnts = 20;


