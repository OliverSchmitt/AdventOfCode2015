INPUT = "1113122113"

def step(seq):
    count = 1
    new = ""
    i = 1
    while i < len(seq):
        if seq[i] == seq[i-1]:
            count += 1
        else:
            new += str(count) + seq[i-1]
            count = 1
        i += 1
    new += str(count) + seq[i-1]
    return new

def run(times):
    seq = INPUT
    for i in range(times):
        seq = step(seq)
    print("Length: {}".format(len(seq)))

def partOne():
    run(40)

def partTwo():
    run(50)

def main():
    partOne()
    partTwo()

if __name__ == "__main__":
    main()
