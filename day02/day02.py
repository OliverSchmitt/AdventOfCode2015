import copy

FILENAME = "input.txt"
SEPARATOR = 'x'

def parseLine(line):
    li = line.find(SEPARATOR)
    ri = line.rfind(SEPARATOR)
    l = int(line[:li])
    w = int(line[li+1:ri])
    h = int(line[ri+1:])
    return [l, w, h]

def readBoxes():
    boxes = []
    with open(FILENAME, 'r') as f:
        line = f.readline()
        while line:
            box = parseLine(line)
            boxes.append(box)
            line = f.readline()
        f.close()
    return boxes

def computePaper(boxes):
    paper = 0
    for box in boxes:
        paper += computeSurface(box)
        paper += computeSmallestSide(box)
    return paper

def computeSurface(box):
    l = box[0]
    w = box[1]
    h = box[2]
    return 2*l*w + 2*l*h + 2*h*w

def computeSmallestSide(box):
    l = box[0]
    w = box[1]
    h = box[2]
    return min(l*w, min(l*h, h*w))

def partOne():
    boxes = readBoxes()
    print("Paper: {}".format(computePaper(boxes)))

def partTwo():
    boxes = readBoxes()
    print("Ribbon: {}".format(computeRibbon(boxes)))

def computeRibbon(boxes):
    ribbon = 0
    for box in boxes:
        ribbon += computeRibbonBox(box)
    return ribbon

def computeRibbonBox(box):
    ribbon = computeSmallestPerimeter(box)
    ribbon += computeVolume(box)
    return ribbon

def computeSmallestPerimeter(box):
    s1, s2 = findTwoSmallestSides(box)
    return 2 * (s1 + s2)

def findTwoSmallestSides(box):
    square = copy.deepcopy(box)
    square.remove(max(box))
    return square[0], square[1]

def computeVolume(box):
    return box[0] * box[1] * box[2]

def main():
    partOne()
    partTwo()

if __name__ == "__main__":
    main()