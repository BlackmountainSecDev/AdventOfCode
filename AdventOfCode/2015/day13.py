from itertools import permutations


def readTheFile(filename):
    try:
        with open(filename, 'r') as lines:
            return lines.read().split('\n')

    except FileNotFoundError:
        return []


def part1():
    print('Part 1')

    wholeContent = {}

    test = False

    if test:
        content = readTheFile('Resources/day13Training.txt')

    else:
        content = readTheFile('Resources/day13.txt')

    for line in content:
        allinLine = line.split()
        allinLine[0]

        if allinLine[0] not in wholeContent.keys():
            wholeContent[allinLine[0]] = {}

        if allinLine[2] == 'gain':
            wholeContent[allinLine[0]][allinLine[-1][:-1]] = int(allinLine[3])
        else:
            wholeContent[allinLine[0]][allinLine[-1][:-1]] = int(allinLine[3]) * -1


        #print(wholeContent)

    allKeys = wholeContent.keys()
    maxLength = len(allKeys)-1

    wholeSum = 0
    bestCombination = 0
    for currentCombination in permutations(allKeys):
        currentSum = 0

        for index, name in enumerate(currentCombination):

            if index == maxLength:
                afterName = currentCombination[0]
            else:
                afterName = currentCombination[index+1]


            currentSum += wholeContent[name][afterName]
            currentSum += wholeContent[afterName][name]

        if currentSum > wholeSum:
            wholeSum = currentSum
            bestCombination = currentCombination

    print(bestCombination)
    print(wholeSum)


def part2():
    print('Part 2')

    wholeContent = {'You': {}}

    test = False

    if test:
        content = readTheFile('Resources/day13Training.txt')

    else:
        content = readTheFile('Resources/day13.txt')

    for line in content:
        allinLine = line.split()
        allinLine[0]

        if allinLine[0] not in wholeContent.keys():
            wholeContent[allinLine[0]] = {'You':0}
            wholeContent['You'][allinLine[0]] = 0

        if allinLine[2] == 'gain':
            wholeContent[allinLine[0]][allinLine[-1][:-1]] = int(allinLine[3])
        else:
            wholeContent[allinLine[0]][allinLine[-1][:-1]] = int(allinLine[3]) * -1


        #print(wholeContent)

    allKeys = wholeContent.keys()
    maxLength = len(allKeys)-1

    wholeSum = 0
    bestCombination = 0
    for currentCombination in permutations(allKeys):
        currentSum = 0

        for index, name in enumerate(currentCombination):

            if index == maxLength:
                afterName = currentCombination[0]
            else:
                afterName = currentCombination[index+1]


            currentSum += wholeContent[name][afterName]
            currentSum += wholeContent[afterName][name]

        if currentSum > wholeSum:
            wholeSum = currentSum
            bestCombination = currentCombination

    print(bestCombination)
    print(wholeSum)

if __name__ == '__main__':
    #part1()
    part2()