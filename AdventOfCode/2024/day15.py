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
    print(f'{'#'*(MAXX+5)}')
    for line in paraTheMap:
        #print(f'#{''.join(line)}#') #part 1
        print(f'##{''.join(line)}##')  #part 2

    print(f'{'#' * (MAXX+5)}')


MINX = 0
MAXX = 0
MINY = 0
MAXY = 0

LEFT = np.array([0, -1])
RIGHT = np.array([0, 1])
UP = np. array([-1, 0])
DOWN = np.array([1, 0])

ROBOT = '@'
WALL = '#'
BOX = 'O'
FREE = '.'
BOX_LEFT = '['
BOX_RIGHT = ']'


def part1():
    global MAXX
    global MAXY

    TRAIN = True
    #TRAIN = False

    if TRAIN:
        theMap, theDirections = readFile('Resources/day15ResourceTraining.txt')

    else:
        theMap, theDirections = readFile('Resources/day15Resource.txt')


    MAXX = len(theMap[0])-1
    MAXY = len(theMap)-1


    #find the robot @
    currentPositionRobot = np.array([0, 0])
    for indexY, line in enumerate(theMap):
        for indexX, char in enumerate(line):
            if ROBOT == char:
                currentPositionRobot = np.array([indexY, indexX])
                break


    for direction in theDirections:
        if direction == '^':
            nextDirection = UP

        elif direction == '<':
            nextDirection = LEFT

        elif direction == '>':
            nextDirection = RIGHT

        else:
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



def justCheckMoveability(currentPositionY, currentPositionX, nextDirectionY, paraTheMap, elemToMove):

    nextPositionY = currentPositionY + nextDirectionY

    thePointOnMap = paraTheMap[nextPositionY][currentPositionX]
    if thePointOnMap == FREE:
        return True
    elif thePointOnMap == BOX_LEFT:
        print('Box_Left')
        #check other part
        #check own part and move
        justCheckMoveability(nextPositionY, currentPositionX, nextDirectionY, paraTheMap, thePointOnMap)

    elif thePointOnMap == BOX_RIGHT:
        print('Box_Right')


    else:
        return False

def checkAllBoxesMoveability(currentPositionY, currentPositionX, nextDirectionY, paraTheMap):

    nextPositionY = currentPositionY + nextDirectionY

    if MINY <= nextPositionY <= MAXY:
        # 1. find neighbor
        if paraTheMap[currentPositionY][currentPositionX] == BOX_LEFT:
            # position of box right
            currentPositionXOfNeighbhor = currentPositionX + 1
        else:
            currentPositionXOfNeighbhor = currentPositionX - 1


        elemsToMove = set()
        # 2. check own way
        myElem = paraTheMap[nextPositionY][currentPositionX]
        isMyWayFree = False

        if myElem == WALL:
            isMyWayFree = False
        elif myElem == FREE:
            isMyWayFree = True
            elemsToMove.add((currentPositionY, currentPositionX))
        else:
            isMyWayFree, upperElems = checkAllBoxesMoveability(nextPositionY, currentPositionX, nextDirectionY, paraTheMap)
            if isMyWayFree:
                [elemsToMove.add(uperElem) for uperElem in upperElems]
                elemsToMove.add((currentPositionY, currentPositionX))



        neigborElem = paraTheMap[nextPositionY][currentPositionXOfNeighbhor]
        isNeigborWayFree = False
        if neigborElem == WALL:
            isNeigborWayFree = False
        elif neigborElem == FREE:
            isNeigborWayFree = True
            elemsToMove.add((currentPositionY, currentPositionXOfNeighbhor))
        else:
            isNeigborWayFree, upperElems = checkAllBoxesMoveability(nextPositionY, currentPositionXOfNeighbhor, nextDirectionY, paraTheMap)
            if isNeigborWayFree:
                [elemsToMove.add(uperElem) for uperElem in upperElems]
                elemsToMove.add((currentPositionY, currentPositionXOfNeighbhor))

        return isMyWayFree & isNeigborWayFree, elemsToMove

    return False, []


def checkAndMovePart2(currentPositionY, currentPositionX, nextDirectionY, nextDirectionX, paraTheMap, elemToMove):

    nextPositionY = currentPositionY + nextDirectionY
    nextPositionX = currentPositionX + nextDirectionX

    if MINY <= nextPositionY <= MAXY and MINX <= nextPositionX <= MAXX:

        thePointOnMap = paraTheMap[nextPositionY][nextPositionX]

        if thePointOnMap == FREE:
            if nextPositionY != currentPositionY:
                paraTheMap[currentPositionY][currentPositionX] = FREE
                paraTheMap[nextPositionY][nextPositionX] = elemToMove

                return True, nextPositionY, nextPositionX, paraTheMap


            else:
                paraTheMap[currentPositionY][currentPositionX] = FREE
                paraTheMap[nextPositionY][nextPositionX] = elemToMove

                return True, nextPositionY, nextPositionX, paraTheMap

        elif thePointOnMap == BOX_LEFT or thePointOnMap == BOX_RIGHT:

            if currentPositionY != nextPositionY:
                moveable, listToMove = checkAllBoxesMoveability(nextPositionY, nextPositionX, nextDirectionY, paraTheMap)

                if moveable:
                    listToMove = sorted(listToMove, key=lambda x: x[0])

                    if nextDirectionY == -1:
                        for currentElem in listToMove:
                            posY, posX = currentElem
                            nextPosY = posY + nextDirectionY

                            paraTheMap[nextPosY][posX] = paraTheMap[posY][posX]
                            paraTheMap[posY][posX] = FREE
                    else:
                        for currentElem in listToMove[::-1]:
                            posY, posX = currentElem
                            nextPosY = posY + nextDirectionY

                            paraTheMap[nextPosY][posX] = paraTheMap[posY][posX]
                            paraTheMap[posY][posX] = FREE


                    paraTheMap[currentPositionY][currentPositionX] = FREE
                    paraTheMap[nextPositionY][nextPositionX] = elemToMove

                    return True, nextPositionY, nextPositionX, paraTheMap

                else:
                    return False, currentPositionY, currentPositionX, paraTheMap

            else:
                moved, _, _, paraTheMap = checkAndMovePart2(nextPositionY, nextPositionX, nextDirectionY,
                                                        nextDirectionX, paraTheMap, thePointOnMap)

                if moved:
                    paraTheMap[currentPositionY][currentPositionX] = FREE
                    paraTheMap[nextPositionY][nextPositionX] = elemToMove

                    return True, nextPositionY, nextPositionX, paraTheMap

    return False, currentPositionY, currentPositionX, paraTheMap


def part2():
    global MAXX
    global MAXY

    #TRAIN = True
    TRAIN = False

    if TRAIN:
        theOldMap, theDirections = readFile('Resources/day15ResourceTraining.txt')
        #theOldMap, theDirections = readFile('Resources/day15ResourceTraining3.txt')

    else:
        theOldMap, theDirections = readFile('Resources/day15Resource.txt')

    # build the new map and find the startPoint of the robot
    theMap = []
    currentPositionRobot = np.array([0, 0])

    for indexY, line in enumerate(theOldMap):
        newLine = []
        for indexX, char in enumerate(line):
            if char == WALL:
                newLine.append(WALL)
                newLine.append(WALL)

            elif char == FREE:
                newLine.append(FREE)
                newLine.append(FREE)

            elif char == BOX:
                newLine.append(BOX_LEFT)
                newLine.append(BOX_RIGHT)

            elif ROBOT == char:
                newLine.append(ROBOT)
                currentPositionRobot = np.array([len(theMap), len(newLine) - 1])
                newLine.append(FREE)

        theMap.append(newLine)

    MAXX = len(theMap[0]) - 1
    MAXY = len(theMap) - 1

    printTheMap(theMap)

    for direction in theDirections:
        if direction == '^':
            nextDirection = UP
            #print('UP')

        elif direction == '<':
            nextDirection = LEFT
            #print('LEFT')

        elif direction == '>':
            nextDirection = RIGHT
            #print('RIGHT')

        else:
            nextDirection = DOWN
            #print('DOWN')

        moved, newPositionY, newPositionX, paraTheMap = checkAndMovePart2(currentPositionRobot[0],
                                                                          currentPositionRobot[1],
                                                                          nextDirection[0], nextDirection[1],
                                                                          theMap, ROBOT)

        if moved:
            theMap = paraTheMap
            currentPositionRobot[0] = newPositionY
            currentPositionRobot[1] = newPositionX


        #printTheMap(theMap)
        #printTheMap('\n')

    printTheMap(theMap)

    theSum = 0
    for y, line in enumerate(theMap):
        for x, char in enumerate(line):
            if char == BOX_LEFT:
                theSum += 100 * (y + 1) + (x + 2)

    print(theSum)


if __name__ == '__main__':
    #part1()
    part2()


