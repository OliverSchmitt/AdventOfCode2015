import sys
sys.path.append("..")
import util

import codecs
import re

def removeEscapeCharacters(text):
    return codecs.getdecoder("unicode_escape")(text)[0]
    
def partOne():
    text = open(util.FILENAME, 'r').read()
    numChars = len(text.replace('\n', ''))

    text = text.replace("\"\n\"", "")[1:-1]
    escapedText = removeEscapeCharacters(text)

    print("code - escaped: {}".format(numChars - len(escapedText)))

def partTwo():
    print(sum(2+s.count('\\')+s.count('"') for s in open(util.FILENAME)))

def main():
    partOne()
    partTwo()

if __name__ == "__main__":
    main()
