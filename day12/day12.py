import sys
sys.path.append("..")
import util

import json

def sumJson(data, part):
    t = type(data)

    if t == int:
        return data

    if t == str:
        return 0

    if t == dict:
        if part == 2 and ('red' in data.keys() or 'red' in data.values()):
            return 0

        s = 0
        for d in data.values():
            if d == "red" and part == 2:
                return 0
            s += sumJson(d, part)
        return s

    if t == list:
        s = 0
        for d in data:
            s += sumJson(d, part)
        return s

    print("Unknown data type {}".format(t))

def loadJson():
    return json.load(open(util.FILENAME))

dataa = loadJson()
def main():
    for part in range(1, 3):
        print("Sum: {}".format(sumJson(dataa, part)))

if __name__ == "__main__":
    main()
