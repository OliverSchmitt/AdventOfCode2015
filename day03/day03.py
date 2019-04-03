FILENAME = "./input.txt"

NORTH = "^"
EAST = ">"
SOUTH = "v"
WEST = "<"

def partOne():
    houses = {}
    pos = (0, 0)
    updatePresentCount(houses, pos)
    directions = open(FILENAME, 'r').read()
    for dir in directions:
        pos = move(pos, dir)
        updatePresentCount(houses, pos)
    print("Number of houeses with atleast 1 present: ", len(houses))

def move(pos, dir):
    pos = list(pos)
    if dir == NORTH:
        pos[1] -= 1
    elif dir == EAST:
        pos[0] += 1
    elif dir == SOUTH:
        pos[1] += 1
    elif dir == WEST:
        pos[0] -= 1
    else:
        print("Unknown direction '{}'".format(dir))
        exit(1)
    return tuple(pos)

def updatePresentCount(houses, pos):
    if pos in houses:
        houses[pos] += 1
    else:
        houses[pos] = 1

def partTwo():
    directions = open(FILENAME, 'r').read()
    n = len(directions)
    assert n % 2 == 0
    houses = {}
    santaPos = (0, 0)
    roboPos = (0, 0)
    updatePresentCount(houses, santaPos)
    updatePresentCount(houses, roboPos)
    for i in range(0, n, 2):
        santaDir = directions[i]
        roboDir = directions[i + 1]
        santaPos = move(santaPos, santaDir)
        roboPos = move(roboPos, roboDir)
        updatePresentCount(houses, santaPos)
        updatePresentCount(houses, roboPos)
    print("Number of houeses with atleast 1 present: ", len(houses))


def main():
    partOne()
    partTwo()

if __name__ == "__main__":
    main()
