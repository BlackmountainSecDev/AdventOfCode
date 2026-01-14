import numpy as np



def readTheFile(filename):
    with open(filename, 'r') as lines:
        return lines.read()




def part1():
    content = readTheFile('Resources/day3.txt')
    print(content)

    north = np.array([-1 , 0])
    south = np.array([1, 0])
    west  = np.array([0, -1])
    eaast = np.array([0, 1])

    currentPos = np.array([0, 0])

    theDict = {}
    theDict[tuple(currentPos)] = 1

    for currentDir in content:
        if currentDir == '^':
            currentPos += north
        elif currentDir == 'v':
            currentPos += south
        elif currentDir == '>':
            currentPos += eaast
        else:
            currentPos += west

        if tuple(currentPos) in theDict.keys():
            theDict[tuple(currentPos)] += 1
        else:
            theDict[tuple(currentPos)] = 1

    print(len(theDict.values()))


def part2():
    content = readTheFile('Resources/day3.txt')
    print(content)

    north = np.array([-1 , 0])
    south = np.array([1, 0])
    west  = np.array([0, -1])
    eaast = np.array([0, 1])

    currentPosSanta = np.array([0, 0])
    currentPosRobo = np.array([0, 0])

  
    theDict = {}
    theDict[tuple(currentPosSanta)] = 1

    for index, currentDir in enumerate(content):

        if index%2 == 0:
            currentPos = currentPosSanta
        else:
            currentPos = currentPosRobo


        if currentDir == '^':
            currentPos += north
        elif currentDir == 'v':
            currentPos += south
        elif currentDir == '>':
            currentPos += eaast
        else:
            currentPos += west

        if tuple(currentPos) in theDict.keys():
            theDict[tuple(currentPos)] += 1
        else:
            theDict[tuple(currentPos)] = 1

        if index%2 == 0:
            currentPosSanta = currentPos
        else:
            currentPosRobo = currentPos

    print(len(theDict.values()))


if __name__ == '__main__':
    part1()
    part2()