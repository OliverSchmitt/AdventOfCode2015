import sys
sys.path.append("..")
import util

class City:
    def __init__(self, name):
        self.name = name
        self.to = {}
        self.visited = False

    def addConnection(self, to, distance):
        self.to[to] = distance

def parseLine(line, cities):
    words = line.split()

    name1 = words[0]
    name2 = words[2]
    if name1 not in cities:
        cities[name1] = City(name1)
    if name2 not in cities:
        cities[name2] = City(name2)

    distance = int(words[-1])
    cities[name1].addConnection(name2, distance)
    cities[name2].addConnection(name1, distance)

def parseLines(lines):
    cities = {}
    for line in lines:
        parseLine(line, cities)
    return cities

def resetCities(cities):
    for city in cities.values():
        city.visited = False

def allVisited(cities):
    for city in cities.values():
        if not city.visited:
            return False
    return True

def findRouteDistances(cities, name, distances, distance):
    current = cities[name]
    current.visited = True

    for cityName in current.to.keys():
        city = cities[cityName]
        if not city.visited:
            findRouteDistances(cities, cityName, distances, [distance[0] + current.to[cityName]])
            city.visited = False
    
    if allVisited(cities):
        distances.append(distance[0])

def findShortestRouteDistance(cities, func):
    allDistances = []
    for name in cities.keys():
        resetCities(cities)
        distances = []
        findRouteDistances(cities, name, distances, [0])
        allDistances = allDistances + distances
    return func(allDistances)

def run(func):
    lines = util.getLines()
    cities = parseLines(lines)
    distance = findShortestRouteDistance(cities, func)
    print("Distance: {}".format(distance))

def partOne():
    run(min)

def partTwo():
    run(max)

def main():
    partOne()
    partTwo()

if __name__ == "__main__":
    main()
