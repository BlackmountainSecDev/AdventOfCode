import numpy as np
import itertools


def readTheFile():
    with open('Resources/day6Resource.txt', 'r') as lines:
    #with open('Resources/day6ResourceTraining.txt', 'r') as lines:
        return [list(line.strip()) for line in lines.readlines()]  # list(line.strip) is important for numpy


UP = '^' # also the start sign
DOWN = 'v'
LEFT = '<'
RIGHT = '>'
OBSTACLE = '#'

def part1():
    karte = np.array(readTheFile())
    current_position = np.argwhere(karte == UP)[0]
    current_row, current_col = current_position

    next_position = current_position
    next_row = current_row
    next_col = current_col

    currentDirection = UP
    minRow, minCol = 0, 0
    maxRow, maxCol = karte.shape

    visitedPosition = {}

    RUN = True

    visitedPosition = set()
    visitedPosition.add((current_row, current_col))

    while RUN:
        if currentDirection == UP:
            column = karte[:current_row, current_col]
            next_sharp_index = np.where(column == '#')[0]

            if next_sharp_index.size > 0:
                next_sharp_row = next_sharp_index[-1]  # Das letzte '#' in der Spalte (am nächsten oben)

                for rowPos in range(current_row - 1, next_sharp_row, -1):
                    visitedPosition.add((rowPos, current_col))

                next_row = next_sharp_row + 1
                current_row = next_row
                currentDirection = RIGHT

            else:
                for rowPos in range(current_row - 1, minRow - 1, -1):
                    visitedPosition.add((rowPos, current_col))

                RUN = False

        elif currentDirection == RIGHT:
            # print('RIGHT')
            row = karte[current_row, current_col:]
            next_sharp_index = np.where(row == '#')[0]

            if next_sharp_index.size > 0:
                next_sharp_col = next_sharp_index[0] + current_col

                for colPos in range(current_col + 1, next_sharp_col):
                    visitedPosition.add((current_row, colPos))

                next_col = next_sharp_col - 1

                current_col = next_col
                currentDirection = DOWN

            else:
                for colPos in range(current_col + 1, maxCol):
                    visitedPosition.add((current_row, colPos))

                RUN = False

        elif currentDirection == LEFT:
            row = karte[current_row, :current_col]
            next_sharp_index = np.where(row == '#')[0]

            if next_sharp_index.size > 0:
                next_sharp_col = next_sharp_index[-1]

                for colPos in range(current_col - 1, next_sharp_col, - 1):
                    visitedPosition.add((current_row, colPos))

                next_col = next_sharp_col + 1

                current_col = next_col
                currentDirection = UP

            else:

                for colPos in range(current_col - 1, minCol - 1, - 1):
                    visitedPosition.add((current_row, colPos))

                RUN = False
        else:
            column = karte[current_row:, current_col]
            next_sharp_index = np.where(column == '#')[0]

            if next_sharp_index.size > 0:
                next_sharp_row = next_sharp_index[0] + current_row  # Das letzte '#' in der Spalte (am nächsten oben)

                for rowPos in range(current_row + 1, next_sharp_row):
                    visitedPosition.add((rowPos, current_col))

                next_row = next_sharp_row - 1

                current_row = next_row
                currentDirection = LEFT

            else:

                for rowPos in range(current_row + 1, maxRow):
                    visitedPosition.add((rowPos, current_col))

                RUN = False

    print(len(visitedPosition))





def part2():
    '''
    ********************************
    * works, but                   *
    * takes too long for the       *
    * real data                    *
    ********************************
    '''
    print('Part 2')
    theMap = readTheFile()

    row = 0
    currentRow = -1
    currentCol = -1

    # UP, Right, Down, Left
    directions = np.array([[-1, 0], [0, 1], [1, 0], [0, -1]])

    minROW = 0
    minCOL = 0
    maxROW = len(theMap)
    maxCOL = len(theMap[0])

    # find the startPosition
    while currentRow == -1:
        for col in range(0, len(theMap[row])):
            count = theMap[row].count(UP)
            if count == 1:
                currentRow = row
                currentCol = theMap[row].index(UP)
                break
        row += 1

    startRow = currentRow
    startCol = currentCol
    currentDirection = 0
    currentPosition = np.array([currentRow, currentCol])

    visitedPositions = set()
    visitedPositions.add((currentPosition[0], currentPosition[1]))

    RUN = True

    while RUN:
        nextPosition = currentPosition + directions[currentDirection]

        if ((nextPosition[0] >= minROW and nextPosition[0] < maxROW) and
                (nextPosition[1] >= minCOL and nextPosition[1] < maxCOL)):

            if theMap[nextPosition[0]][nextPosition[1]] == OBSTACLE:
                currentDirection += 1
                if currentDirection > 3:
                    currentDirection = 0
            else:
                currentPosition = nextPosition
                visitedPositions.add((currentPosition[0], currentPosition[1]))
        else:
            RUN = False

    print(len(visitedPositions))


    #find possible Obstacle position
    lastPosition = visitedPositions.copy()
    lastPosition.remove((startRow, startCol))

    runCounter = 0
    loopCounter = 0
    for obstaclePos in lastPosition:
        runCounter += 1
        print(f'{runCounter} in {len(lastPosition)}')
        manipulatedMap = []
        for el in theMap:
            manipulatedMap.append(el.copy())

        manipulatedMap[obstaclePos[0]][obstaclePos[1]] = OBSTACLE
        currentRow = startRow
        currentCol = startCol
        currentDirection = 0
        currentPosition = np.array([currentRow, currentCol])
        visitedPositionsArray = []
        visitedPositionsArray.append([currentPosition[0], currentPosition[1], currentDirection]) # adding start point

        RUN = True

        while RUN:
            nextPosition = currentPosition + directions[currentDirection]
            #if nextPosition[0] == 6 and nextPosition[1] == 4:
            #    print('aha')

            if ((nextPosition[0] >= minROW and nextPosition[0] < maxROW) and
                    (nextPosition[1] >= minCOL and nextPosition[1] < maxCOL)):

                if manipulatedMap[nextPosition[0]][nextPosition[1]] == OBSTACLE:
                    currentDirection += 1
                    if currentDirection > 3:
                        currentDirection = 0
                else:
                    currentPosition = nextPosition
                    if [currentPosition[0], currentPosition[1], currentDirection] in visitedPositionsArray:
                        loopCounter += 1
                        RUN = False
                        #loop
                    else:
                        visitedPositionsArray.append([currentPosition[0], currentPosition[1], currentDirection])
            else:
                RUN = False


    print(loopCounter)


import time

if __name__ == '__main__':


    start1 = time.time()
    part1()
    end1 = time.time()
    print(f"Time taken to run the code was {end1 - start1} seconds")



    start1 = time.time()
    part2()
    end1 = time.time()
    print(f"Time taken to run the code was {end1 - start1} seconds")



