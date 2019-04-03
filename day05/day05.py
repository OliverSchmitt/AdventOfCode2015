import sys
sys.path.append("..")
import util

VOWELS = "aeiou"
PROHIBITED = ["ab", "cd", "pq", "xy"]

def partOne():
    lines = util.getLines()
    numberOfNiceStrings = 0
    for line in lines:
        if isNice(line):
            numberOfNiceStrings += 1
    print("Number of nice strings: {}".format(numberOfNiceStrings))

def isNice(string):
    return ((countVowels(string) > 2)
        and containsDoubleLetter(string)
        and not containsProhibited(string))

def countVowels(string):
    count = 0
    for c in string:
        if c in VOWELS:
            count += 1
    return count

def containsDoubleLetter(string):
    n = len(string)
    for i in range(n - 1):
        if string[i] == string[i + 1]:
            return True
    return False

def containsProhibited(string):
    for seq in PROHIBITED:
        if seq in string:
            return True
    return False

def partTwo():
    lines = util.getLines()
    count = 0
    for line in lines:
        if isNice2(line):
            count += 1
    print("Number of nice strings: {}".format(count))

def isNice2(string):
    return containsNonOverlappingPair(string) and containsOneSpaceRepeat(string)

def containsNonOverlappingPair(string):
    n = len(string)
    for i in range(n - 1):
        pair = string[i:i+2]
        index = string.rfind(pair, i+1)
        if index != i+1 and index != -1:
            return True
    return False

def containsOneSpaceRepeat(string):
    n = len(string)
    for i in range(n - 2):
        if string[i] == string[i + 2]:
            return True
    return False

def main():
    partOne()
    partTwo()

if __name__ == "__main__":
    main()
