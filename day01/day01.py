FILENAME = "./input.txt"

def partOne():
    floor = 0
    with open(FILENAME, 'r') as f:
        while True:
            c = f.read(1)
            if not c:
                break
            elif c == "(":
                floor += 1
            elif c == ")":
                floor -= 1
            else:
                print("Unknown character {}".format(c))
                exit(1)
        f.close()
    print("Floor: {}".format(floor))

def partTwo():
    with open(FILENAME, 'r') as f:
        floor = 0
        pos = 1
        while True:
            c = f.read(1)
            if not c:
                break
            elif c == "(":
                floor += 1
            elif c == ")":
                floor -= 1
            else:
                print("Unknown character {}".format(c))
                exit(1)
            if floor < 0:
                break
            pos += 1
        f.close()
    print("Pos: {}".format(pos))

def main():
    partOne()
    partTwo()

if __name__ == "__main__":
    main()