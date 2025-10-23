from collections import deque
from itertools import groupby

def readTheFile():
    with open('Resources/day12Resource.txt', 'r') as lines:
    #with open('Resources/day12ResourceTraining1.txt', 'r') as lines:
    #with open('Resources/day12ResourceTraining2.txt', 'r') as lines:
    #with open('Resources/day12ResourceTraining3.txt', 'r') as lines:
    #with open('Resources/day12ResourceTraining4.txt', 'r') as lines:
        return [line.strip() for line in lines.readlines()]



DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
TOP = 0
BOTTOM = 1
LEFT = 2
RIGHT = 3

ROW = 0
COLUMN = 1


MinRow = 0
MinColumn = 0
MaxRow = 0
MaxColumn = 0


def neighbors(r, c):
    global MaxRow
    global MaxColumn

    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < MaxRow and 0 <= nc < MaxColumn:
            yield nr, nc


def countPerimenter(aGroup):
    char, coords = aGroup
    perimeter = []
    perimeterCount = 0

    for coord in coords:
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = coord[0] + dr, coord[1] + dc
            if (nr, nc) not in coords:
                perimeterCount += 1
                #perimeter.append((nr, nc))

    return perimeterCount #len(perimeter)


def countSides(aGroup):
    char, coords = aGroup

    coords = sorted(coords, key=lambda tupel: (tupel[0], tupel[1]))


    allSides = []
    topSide = {}
    rightSide = {}
    bottomSide = {}
    leftSide = {}


    for coord in coords:

        #top side
        nr, nc = coord[0] - 1, coord[1] + 0
        if (nr, nc) not in coords:
            if nr in topSide:
                content = topSide[nr]
                content = sorted(content, key=lambda tupel: tupel[1])

                tempElement = content[-1]

                if tempElement[1] + 1 == nc:# or  tempElement[1] - 1 == nc:
                    content.append((nr, nc))
                    topSide[nr] = content
                else:
                    allSides.append(topSide[nr])
                    topSide[nr]  = [(nr, nc)]
            else:
                topSide[nr] = [(nr, nc)]

        #right side
        nr, nc = coord[0] + 0, coord[1] + 1
        if (nr, nc) not in coords:
            if nc in rightSide:
                content = rightSide[nc]
                content = sorted(content, key=lambda tupel: tupel[0])

                tempElement = content[-1]

                if tempElement[0] + 1 == nr:# or tempElement[0] - 1 == nr:
                    content.append((nr, nc))
                    rightSide[nc] = content
                else:
                    allSides.append(rightSide[nc])
                    rightSide[nc] = [(nr, nc)]
            else:
                rightSide[nc] = [(nr, nc)]


        #bottom side
        nr, nc = coord[0] + 1, coord[1] + 0
        if (nr, nc) not in coords:
            if nr in bottomSide:
                content = bottomSide[nr]
                content = sorted(content, key=lambda tupel: tupel[1])

                tempElement = content[-1]

                if tempElement[1] + 1 == nc:# or  tempElement[1] - 1 == nc:
                    content.append((nr, nc))
                    bottomSide[nr] = content
                else:
                    allSides.append(bottomSide[nr])
                    bottomSide[nr]  = [(nr, nc)]

            else:
                bottomSide[nr] = [(nr, nc)]

        # left side
        nr, nc = coord[0] + 0, coord[1] - 1
        if (nr, nc) not in coords:
            if nc in leftSide:
                content = leftSide[nc]
                content = sorted(content, key=lambda tupel: tupel[0])

                tempElement = content[-1]

                if tempElement[0] + 1 == nr:# or tempElement[0] - 1 == nr:
                    content.append((nr, nc))
                    leftSide[nc] = content
                else:
                    allSides.append(leftSide[nc])
                    leftSide[nc] = [(nr, nc)]
            else:
                leftSide[nc] = [(nr, nc)]



    for value in list(topSide.values()):
        allSides.append(value)

    for value in list(rightSide.values()):
        allSides.append(value)

    for value in list(bottomSide.values()):
        allSides.append(value)

    for value in list(leftSide.values()):
        allSides.append(value)


    return len(allSides) #len(perimeter)


def part1():
    global MaxRow
    global MaxColumn

    theMap = readTheFile()

    #get all possible values
    #possibleValues = [x for x in set(''.join(theMap))]


    MaxRow = len(theMap)
    MaxColumn = len(theMap[0])
    visited = [[False]*MaxColumn for _ in range(MaxRow)]

    allGroups = []

    for r in range(MaxRow):
        for c in range(MaxColumn):
            if not visited[r][c]:
                char = theMap[r][c]
                cluster = []
                q = deque([(r, c)])
                visited[r][c] = True
                while q:
                    cr, cc = q.popleft()
                    cluster.append((cr, cc))
                    for nr, nc in neighbors(cr, cc):
                        if not visited[nr][nc] and theMap[nr][nc] == char:
                            visited[nr][nc] = True
                            q.append((nr, nc))
                allGroups.append((char, cluster))

    char, coords = allGroups[0]
    print(char)
    print(len(coords))
    print('')

    wholeValue = 0
    for aGroup in allGroups:
        perimeterVal = countPerimenter(aGroup)
        wholeValue += len(aGroup[1])*perimeterVal
        print(f'{aGroup[0]}: {len(aGroup[1])*perimeterVal}')

    print(wholeValue)


def part2():
    global MaxRow
    global MaxColumn

    theMap = readTheFile()

    MaxRow = len(theMap)
    MaxColumn = len(theMap[0])
    visited = [[False]*MaxColumn for _ in range(MaxRow)]

    allGroups = []

    for r in range(MaxRow):
        for c in range(MaxColumn):
            if not visited[r][c]:
                char = theMap[r][c]
                cluster = []
                q = deque([(r, c)])
                visited[r][c] = True
                while q:
                    cr, cc = q.popleft()
                    cluster.append((cr, cc))
                    for nr, nc in neighbors(cr, cc):
                        if not visited[nr][nc] and theMap[nr][nc] == char:
                            visited[nr][nc] = True
                            q.append((nr, nc))
                allGroups.append((char, cluster))

    wholeValue = 0
    for aGroup in allGroups:
        sides = countSides(aGroup)
        wholeValue += len(aGroup[1])*sides
        print(f'{aGroup[0]}: {len(aGroup[1])} * {sides} = {len(aGroup[1])*sides}')

    print(wholeValue)


if __name__ == '__main__':
    #part1()
    part2()