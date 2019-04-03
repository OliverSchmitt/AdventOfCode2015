import hashlib

INPUT = "ckczppom"

def findHash(length, compare):
    hash = "11111"
    number = 1
    while hash[:length] != compare:
        input = INPUT + str(number)
        hash = hashlib.md5(input.encode("utf-8")).hexdigest()
        number += 1
    print("Input: '{}' + '{}' produces '{}'".format(INPUT, number - 1, hash))

def partOne():
    findHash(5, "00000")

def partTwo():
    findHash(6, "000000")

def main():
    partOne()
    partTwo()

if __name__ == "__main__":
    main()
