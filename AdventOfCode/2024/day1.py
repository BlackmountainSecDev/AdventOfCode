import numpy as np

def readTheFile():
    with open('Resources/day1Resource.txt', 'r') as lines:
    #with open('Resources/day1ResourceTraining.txt', 'r') as lines:
        return lines.readlines()


def part1():
    leftside = []
    rightside = []
    theInput = readTheFile()
    for line in theInput:
        l, r = line.split()
        leftside.append(int(l))
        rightside.append(int(r))

    leftside = np.array(sorted(leftside))
    rightside = np.array(sorted(rightside))

    theRest = leftside-rightside
    aha = [a*-1 if a < 0 else a*1 for a in theRest]

    print(sum(aha))


def part2():
    leftside = []
    rightside = []
    theInput = readTheFile()
    for line in theInput:
        l, r = line.split()
        leftside.append(int(l))
        rightside.append(int(r))

    leftside = np.array(leftside)
    rightside = np.array(rightside)

    similarityScore = []

    for val in leftside:
        found = np.where(rightside == val)
        amount = len(found[0])
        similarityScore.append(val*amount)

    print(sum(similarityScore))

if __name__ == '__main__':
    part1()
    part2()