import sys
sys.path.append("..")
import util

import operator

AND = "AND"
OR = "OR"
NOT = "NOT"
RSHIFT = "RSHIFT"
LSHIFT = "LSHIFT"

class Wire:
    def __init__(self, name, source):
        self.name = name
        self.value = 0
        # Number, Wire or Gate
        self.source = source

class Gate:
    def __init__(self, op, left, right):
        self.op = op
        # Nmber or Gate
        self.left = left
        self.right = right
    
    def __repr__(self):
        return "{} {} {}".format(self.left, self.op, self.right)

def parseLines(lines):
    tree = {}
    for line in lines:
        name = line.split()[-1]
        wire = Wire(name, getSource(tree, line))
        tree[name] = wire
    return tree


def getSource(tree, line):
    name = line.split()[-1]
    if name in tree:
        return tree[name]
    
    words = line.split()[:-2]
    n = len(words)
    if n == 1:
        return words[0]
    elif n == 2:
        return Gate(words[0], words[1], None)
    elif n == 3:
        return Gate(words[1], words[0], words[2])

def getValue(source, tree):
    t = type(source)
    if t == str:
        return getStrValue(source, tree)
    elif t == Gate:
        return getGateValue(source, tree)

def getStrValue(source, tree):
    if source.isdigit():
        return int(source)
    else:
        if tree[source].value == 0:
            tree[source].value = getValue(tree[source].source, tree)
        return tree[source].value

def getGateValue(source, tree):
        if source.right == None:
            return ~getValue(source.left, tree)
        else:
            op = source.op
            if op == AND:
                func = operator.__and__
            elif op == OR:
                func = operator.__or__
            elif op == RSHIFT:
                func = operator.__rshift__
            elif op == LSHIFT:
                func = operator.__lshift__
            else:
                print("Unknown gate operation: {}".format(op))
                exit(1)
            return func(getValue(source.left, tree), getValue(source.right, tree))

def partOne():
    lines = util.getLines()
    op = parseLines(lines)
    name = "a"
    print("{}: {}".format(name, getValue(name, op) % (2**16)))

def partTwo():
    pass

def main():
    partOne()
    partTwo()

if __name__ == "__main__":
    main()
