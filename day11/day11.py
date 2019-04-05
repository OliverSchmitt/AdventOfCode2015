INPUT = "hepxcrrq"

LETTERS = "abcdefghijklmnopqrstuvwxyz"
N = len(LETTERS)
PROHIBITED = ['i', 'o', 'l']
DOUBLES = [c+c for c in LETTERS]
INCREMENTS = [LETTERS[i] + LETTERS[i+1] + LETTERS[i+2] for i in range(N - 2)]

def increment(string):
    i = len(string) - 1
    while i >= 0:
        index = LETTERS.find(string[i])
        c = LETTERS[(index + 1) % N]
        string = string[:i] + c + string[i+1:]
        if c != 'a':
            break
        i -= 1
    return string

def isValid(string):
    for c in PROHIBITED:
        if c in string:
            return False

    if sum([string.count(d) for d in DOUBLES]) < 2:
        return False

    if sum([string.count(inc) for inc in INCREMENTS]) < 1:
        return False
    
    return True

def partOne():
    password = increment(INPUT)
    while not isValid(password):
        password = increment(password)
    print("Password: {}".format(password))

    password = increment(password)
    while not isValid(password):
        password = increment(password)
    print("Password: {}".format(password))

def partTwo():
    pass

def main():
    partOne()
    partTwo()

if __name__ == "__main__":
    main()
