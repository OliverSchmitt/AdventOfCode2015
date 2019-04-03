import sys
sys.path.append("..")
import util

WIDTH = 1000

OFF = False
ON = True

def turnOn1(lights, index):
    lights[index] = ON
TURN_ON_1 = turnOn1

def turnOff1(lights, index):
    lights[index] = OFF
TURN_OFF_1 = turnOff1

def toggle1(lights, index):
    lights[index] = not lights[index]
TOGGLE_1 = toggle1

def turnOn2(lights, index):
    lights[index] += 1
TURN_ON_2 = turnOn2

def turnOff2(lights, index):
    lights[index] -= 1
    if lights[index] < 0:
        lights[index] = 0
TURN_OFF_2 = turnOff2

def toggle2(lights, index):
    lights[index] += 2
TOGGLE_2 = toggle2

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Instruction:
    def __init__(self, instructionType, start, end):
        self.type = instructionType
        self.start = start
        self.end = end

def parseLines(lines):
    instructions = []
    for line in lines:
        instructions.append(parseLine(line))
    return instructions

def parseLine(line):
    words = line.split()
    instructionType = (words[0] + " " + words[1]) if len(words) == 5 else words[0]
    pos = words[-3].split(',')
    start = Position(int(pos[0]), int(pos[1]))
    pos = words[-1].split(',')
    end = Position(int(pos[0]), int(pos[1]))
    return Instruction(instructionType, start, end)

def performInstructions(instructions, lights, mode):
    for instruction in instructions:
        performInstruction(instruction, lights, mode)

def getIndex(x, y):
    return y * WIDTH + x

def performInstruction(instruction, lights, mode):
    start = instruction.start
    end = instruction.end
    itype = instruction.type
    for y in range(start.y, end.y + 1):
        for x in range(start.x, end.x + 1):
            index = getIndex(x, y)
            if itype == "turn on":
                if mode == 1:
                    TURN_ON_1(lights, index)
                else:
                    TURN_ON_2(lights, index)
            elif itype == "turn off":
                if mode == 1:
                    TURN_OFF_1(lights, index)
                else:
                    TURN_OFF_2(lights, index)
            elif itype == "toggle":
                if mode == 1:
                    TOGGLE_1(lights, index)
                else:
                    TOGGLE_2(lights, index)

def countLightsTurnedOn(lights):
    count = 0
    for light in lights:
        if light == ON:
            count += 1
    return count

def partOne():
    run(1)

def partTwo():
    run(2)

def sumLightIntensity(lights):
    sum = 0
    for light in lights:
        sum += light
    return sum

def run(mode):
    lines = util.getLines()
    instructions = parseLines(lines)
    if mode == 1:
        lights = [OFF] * WIDTH * WIDTH
    else:
        lights = [0] * WIDTH * WIDTH
    performInstructions(instructions, lights, mode)
    if mode == 1:
        output = countLightsTurnedOn(lights)
    else:
        output = sumLightIntensity(lights)
    print("Output: {}".format(output))

def main():
    # partOne()
    partTwo()

if __name__ == "__main__":
    main()
