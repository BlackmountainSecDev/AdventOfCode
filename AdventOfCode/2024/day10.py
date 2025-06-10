import numpy as np


def readTheFile():
    with open('Resources/day10Resource.txt', 'r') as lines:
        lines = lines.readlines()
        return [[int(char) for char in line.strip()] for line in lines if line.strip()]



STARTVALUE = 0
ENDVALUE = 9

DIRECTIONS = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])


def findPath(initialWay, map):
    minRow = 0
    minColumn = 0
    maxRow = len(map)
    maxColumn = len(map[0])

    finishedWays = []

    possibleWays = []
    possibleWays.append(initialWay)

    alreadyreachedNines = []

    while len(possibleWays) > 0:

        currentWay = possibleWays.pop()
        currentPositionIndex = len(currentWay) - 1
        currentPosition = np.array(currentWay[currentPositionIndex])
        possibleNextValue = map[currentPosition[0]][currentPosition[1]] + 1

        for direction in DIRECTIONS:
            newPosition = currentPosition + direction

            if (newPosition[0] >= minColumn and newPosition[0] < maxColumn) and (
                    newPosition[1] >= minRow and newPosition[1] < maxRow):
                newValue = map[newPosition[0]][newPosition[1]]

                if newValue == possibleNextValue:
                    possibleNewWay = currentWay.copy()
                    newPosition = newPosition.reshape(1, -1)
                    possibleNewWay = np.vstack((possibleNewWay, newPosition))

                    if possibleNextValue == ENDVALUE:

                        # part1
                        '''
                         if [newPosition[0][0], newPosition[0][1]] not in alreadyreachedNines:
                             alreadyreachedNines.append([newPosition[0][0], newPosition[0][1]])
                             finishedWays.append(possibleNewWay)

                        '''
                        # part2
                        finishedWays.append(possibleNewWay)

                    else:
                        possibleWays.append(possibleNewWay)

    return finishedWays


def part1And2():
    theMap = readTheFile()
    allLength = 0

    for startYPos, line in enumerate(theMap):

        startXPos = 0
        while startXPos != -1:
            try:
                startXPos = line.index(STARTVALUE, startXPos)
            except ValueError:
                startXPos = -1

            if startXPos != -1:
                allLength += len(findPath(np.array([[startYPos, startXPos]]), theMap))
                startXPos += 1

    print(allLength)


if __name__ == '__main__':
    part1And2()
