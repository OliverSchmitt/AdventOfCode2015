import sys
sys.path.append("..")
import util

import operator

class Neighbor:
    def __init__(self, name, mode, amount):
        self.name = name
        self.mode = mode
        self.amount = amount

    def __repr__(self):
        return "Neighbor: {}, Mode: {}, Amount: {}".format(self.name, self.mode, self.amount)

class Attendee:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.numNeighbors = 0
        self.set = False
    
    def add(self, words):
        name = words[-1][:-1]
        mode = words[2]
        amount = int(words[3])

        self.neighbors[name] = Neighbor(name, mode, amount)
    
    def incrementNumNeighbors(self):
        if self.numNeighbors == 2:
            print("{} already has 2 neighbors".format(self.name))
            return
        self.numNeighbors += 1
    
    def decrementNumNeighbors(self):
        if self.numNeighbors == 0:
            print("{} has no neighbors".format(self.name))
            return
        self.numNeighbors -= 1

    def __repr__(self):
        return "Attendee: {}, Set: {}, NumNeighbors: {}".format(self.name, self.set, self.numNeighbors)

def parseLine(line, attendees):
    words = line.split()
    name1 = words[0]

    if name1 not in attendees:
        attendees[name1] = Attendee(name1)
    
    attendees[name1].add(words)

def parseLines(lines):
    attendees = {}
    for line in lines:
        parseLine(line, attendees)
    return attendees

def allSet(attendees):
    for attendee in attendees.values():
        if not attendee.set:
            return False
    return True

def getModeFunc(neighbor):
    if neighbor.mode == "gain":
        return operator.__add__
    elif neighbor.mode == "lose":
        return operator.__sub__
    else:
        print("Unknown mode {}".format(neighbor.mode))
        exit(1)

def findHappinessChanges(attendees, name, changes, happiness):
    current = attendees[name]
    current.set = True

    for neighbor in current.neighbors.values():
        nextAttendee = attendees[neighbor.name]
        if not nextAttendee.set:
            fromNeighbor = nextAttendee.neighbors[name]
            funcTo = getModeFunc(neighbor)
            funcFrom = getModeFunc(fromNeighbor)

            newHappiness = funcFrom(funcTo(happiness, neighbor.amount), fromNeighbor.amount)

            current.incrementNumNeighbors()
            nextAttendee.incrementNumNeighbors()

            findHappinessChanges(attendees, neighbor.name, changes, newHappiness)

            current.decrementNumNeighbors()
            nextAttendee.decrementNumNeighbors()
            nextAttendee.set = False

    if not allSet(attendees):
        return
    
    lastName = ""
    for attendee in attendees.values():
        if attendee != current and attendee.numNeighbors == 1:
            lastName = attendee.name
            break

    if lastName == "":
        print("!")
        pass
    
    lastNeighbor = current.neighbors[lastName]
    funcTo = getModeFunc(lastNeighbor)
    fromNeighbor = attendees[lastNeighbor.name].neighbors[name]
    funcFrom = getModeFunc(fromNeighbor)

    newHappiness = funcFrom(funcTo(happiness, lastNeighbor.amount), fromNeighbor.amount)
    
    changes.append(newHappiness)
    pass

def findMaxHappinessChange(attendees):
    changes = []
    happiness = 0
    findHappinessChanges(attendees, "Alice", changes, happiness)
    return max(changes)

def partOne():
    lines = util.getLines()
    attendees = parseLines(lines)
    happinessChange = findMaxHappinessChange(attendees)
    print("Max happiness Change: {}".format(happinessChange))
    pass

def partTwo():
    lines = util.getLines("./input_with_me.txt")
    attendees = parseLines(lines)
    happinessChange = findMaxHappinessChange(attendees)
    print("Max happiness Change: {}".format(happinessChange))
    pass

def main():
    partOne()
    partTwo()

if __name__ == "__main__":
    main()
