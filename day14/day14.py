import sys
sys.path.append("..")
import util

TIME = 2503

FLYING = "flying"
RESTING = "resting"

class Reindeer:
    def __init__(self, name, speed, flyingTime, restTime):
        self.name = name
        self.speed = speed
        self.flyingTime = flyingTime
        self.restTime = restTime

        self.distance = 0
        self.mode = FLYING
        self.currentTime = 0

    def move(self):
        self.currentTime += 1
        if self.mode == FLYING:
            self.distance += self.speed
            if self.currentTime >= self.flyingTime:
                self.currentTime = 0
                self.mode = RESTING
        elif self.mode == RESTING:
            if self.currentTime >= self.restTime:
                self.currentTime = 0
                self.mode = FLYING
        else:
            print("Unknown mode {}".format(self.mode))
            exit(1)
    
    def __lt__(self, other):
        return self.distance < other.distance
    
    def __repr__(self):
        return "Name: {}, Speed: {}, Time: {}, Rest: {}".format(self.name, self.speed, self.flyingTime, self.restTime)

def parseLine(line, reindeers):
    words = line.split()
    name = words[0]
    speed = int(words[3])
    time = int(words[6])
    rest = int(words[13])
    reindeers.append(Reindeer(name, speed, time, rest))

def parseLines(lines):
    reindeers = []
    for line in lines:
        parseLine(line, reindeers)
    return reindeers

def getDistance(reindeer, time):
    speed = reindeer.speed
    flyingTime = reindeer.flyingTime
    restTime = reindeer.restTime
    roundTime = flyingTime + restTime

    rounds = time // roundTime
    residual = time % roundTime

    distance = rounds * speed * flyingTime
    return distance + (min(residual, flyingTime) * speed)

def getDistances(reindeers, time):
    distances = []
    for reindeer in reindeers:
        distances.append(getDistance(reindeer, time))
    return distances

def getReindeers():
    lines = util.getLines()
    return parseLines(lines)

def partOne():
    reindeers = getReindeers()
    distances = getDistances(reindeers, TIME)
    print("Longest distance: {}".format(max(distances)))

def getScores(reindeers, time):
    scores = {}
    for reindeer in reindeers:
        scores[reindeer.name] = 0
    
    currentTime = 0
    while currentTime < time:
        for reindeer in reindeers:
            reindeer.move()
        highestDistance = max(reindeers).distance
        for reindeer in reindeers:
            if reindeer.distance == highestDistance:
                scores[reindeer.name] += 1
        currentTime += 1
    
    return scores.values()

def partTwo():
    reindeers = getReindeers()
    scores = getScores(reindeers, TIME)
    print("Highest score: {}".format(max(scores)))

def main():
    partOne()
    partTwo()

if __name__ == "__main__":
    main()
