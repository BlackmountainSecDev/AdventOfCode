import numpy as np



def readfile(filename):
    with open(filename, 'r') as datei:
        localContent = datei.read()
        localContent = localContent.split('\n')

        theContent = np.zeros((len(localContent), len(localContent[0])), dtype=int)

        maxLen = len(localContent)
        for y in range(maxLen):
            for x in range(maxLen):
                if localContent[y][x] == '#':
                    theContent[y][x] = 1
                else:
                    theContent[y][x] = 0

    return theContent



def part1():

    test = False

    if test:
        content = readfile('Resources/day18Test.txt')
        rounds = 4
    else:
        content = readfile('Resources/day18.txt')
        rounds = 100


    neigbhours = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    #print(content)

    min = 0
    maxLen = len(content)
    for round in range(rounds):
        theCopy = np.zeros(content.shape, dtype=int)
        for y in range(maxLen):
            for x in range(maxLen):
                localHelper = []
                for neigbhour in neigbhours:
                    ny = y + neigbhour[0]
                    nx = x + neigbhour[1]
                    if ny >= 0 and ny < maxLen and nx >= 0 and nx < maxLen:
                        localHelper.append(content[ny][nx])

                neigbhourValues = sum(localHelper)


                if content[y][x] == 1:
                    if neigbhourValues == 2 or neigbhourValues == 3:
                        theCopy[y][x] = 1
                    else:
                        theCopy[y][x] = 0

                else:
                    if neigbhourValues == 3:
                        theCopy[y][x] = 1

        content = np.copy(theCopy)


    print(np.sum(content))



def part2():

    test = False

    if test:
        content = readfile('Resources/day18Test.txt')
        rounds = 4
    else:
        content = readfile('Resources/day18.txt')
        rounds = 100


    neigbhours = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    #print(content)

    min = 0
    maxLen = len(content)
    for round in range(rounds):
        theCopy = np.zeros(content.shape, dtype=int)
        for y in range(maxLen):
            for x in range(maxLen):
                localHelper = []
                for neigbhour in neigbhours:
                    ny = y + neigbhour[0]
                    nx = x + neigbhour[1]
                    if ny >= 0 and ny < maxLen and nx >= 0 and nx < maxLen:
                        localHelper.append(content[ny][nx])

                neigbhourValues = sum(localHelper)


                if content[y][x] == 1:
                    if neigbhourValues == 2 or neigbhourValues == 3:
                        theCopy[y][x] = 1
                    else:
                        theCopy[y][x] = 0

                else:
                    if neigbhourValues == 3:
                        theCopy[y][x] = 1

        content = np.copy(theCopy)
        content[0][0] = 1
        content[0][maxLen-1] = 1
        content[maxLen-1][0] = 1
        content[maxLen-1][maxLen-1] = 1


    print(np.sum(content))

if __name__ == '__main__':
    part1()
    part2()