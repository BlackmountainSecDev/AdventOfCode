import numpy as np



def readFile(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        wholeContent = file.read().split('\n\n')
        theMap = wholeContent[0].split('\n')
        theMap.pop(len(theMap)-1)
        theMap.pop(0)
        theMap = [list(line[1:len(line) - 1]) for line in theMap]
        theDirections = [direction for direction in wholeContent[1].strip() if direction in '^<>v']

    return theMap, theDirections


'''
#maybe recursive
def checkAndMove(currentPosition, nextDirection, paraTheMap, elemToMove):
    nextPosition = currentPosition + nextDirection
    
    if not (MINY <= nextPosition[0] <= MAXY and MINX <= nextPosition[1] <= MAXX):
        return False, currentPosition, paraTheMap

    target_cell = paraTheMap[nextPosition[0]][nextPosition[1]]

    if target_cell == WALL:
        return False, currentPosition, paraTheMap

    if target_cell == FREE:
        paraTheMap[currentPosition[0]][currentPosition[1]] = FREE
        paraTheMap[nextPosition[0]][nextPosition[1]] = elemToMove

        return True, nextPosition, paraTheMap

    elif paraTheMap[nextPosition[0]][nextPosition[1]] == BOX:
        moved, _, paraTheMap = checkAndMove(nextPosition, nextDirection, paraTheMap, BOX)

        if moved:     
            paraTheMap[currentPosition[0]][currentPosition[1]] = FREE
            paraTheMap[nextPosition[0]][nextPosition[1]] = elemToMove

            return True, nextPosition, paraTheMap

    return False, currentPosition, paraTheMap
'''

#maybe recursive
def checkAndMove(currentPositionY, currentPositionX, nextDirectionY, nextDirectionX, paraTheMap, elemToMove):

    nextPositionY = currentPositionY + nextDirectionY
    nextPositionX = currentPositionX + nextDirectionX


    if MINY <= nextPositionY <= MAXY and MINX <= nextPositionX <= MAXX:

        thePointOnMap = paraTheMap[nextPositionY][nextPositionX]

        if thePointOnMap == FREE:
            paraTheMap[currentPositionY][currentPositionX] = FREE
            paraTheMap[nextPositionY][nextPositionX] = elemToMove

            return True, nextPositionY, nextPositionX, paraTheMap

        elif thePointOnMap == BOX:
            moved, _, _, paraTheMap = checkAndMove(nextPositionY, nextPositionX, nextDirectionY, nextDirectionX, paraTheMap, BOX)

            if moved:
                paraTheMap[currentPositionY][currentPositionX] = FREE
                paraTheMap[nextPositionY][nextPositionX] = elemToMove

                return True, nextPositionY, nextPositionX, paraTheMap

    return False, currentPositionY, currentPositionX, paraTheMap


def printTheMap(paraTheMap):
    print(f'{'#'*(MAXX+2)}')
    for line in paraTheMap:
        print(f'#{''.join(line)}#')

    print(f'{'#' * (MAXX+2)}')


MINX = 0
MAXX = 0
MINY = 0
MAXY = 0

ROBOT = '@'
WALL = '#'
BOX = 'O'
FREE = '.'


def part1():
    global MAXX
    global MAXY

    #TRAIN = True
    TRAIN = False

    if TRAIN:
        theMap, theDirections = readFile('Resources/day15ResourceTraining.txt')

    else:
        theMap, theDirections = readFile('Resources/day15Resource.txt')


    MAXX = len(theMap[0])-1
    MAXY = len(theMap)-1


    #find the robot @
    startPointRobot = (0, 0)
    for indexY, line in enumerate(theMap):
        for indexX, char in enumerate(line):
            if ROBOT == char:
                startPointRobot = (indexY, indexX)
                break



    currentPositionRobot = np.array([startPointRobot[0], startPointRobot[1]])
    LEFT = np.array([0, -1])
    RIGHT = np.array([0, 1])
    UP = np. array([-1, 0])
    DOWN = np.array([1, 0])


    #for direction in theDirections:
    for counter, direction in enumerate(theDirections):
        if direction == '^':
            #print(f'{counter}. Up')
            nextDirection = UP

        elif direction == '<':
            #print(f'{counter}. Left')
            nextDirection = LEFT

        elif direction == '>':
            #print(f'{counter}. Right')
            nextDirection = RIGHT

        else:
            #print(f'{counter}. DOWN')
            nextDirection = DOWN

        moved, newPositionY, newPositionX, paraTheMap = checkAndMove(currentPositionRobot[0], currentPositionRobot[1], nextDirection[0], nextDirection[1], theMap, ROBOT)

        if moved:
            theMap = paraTheMap
            currentPositionRobot[0] = newPositionY
            currentPositionRobot[1] = newPositionX

    printTheMap(theMap)

    theSum = 0
    for y, line in enumerate(theMap):
        for x, char in enumerate(line):
            if char == BOX:
                theSum += 100 * (y+1) + (x+1)

    print(theSum)
    #count the value


if __name__ == '__main__':
    part1()