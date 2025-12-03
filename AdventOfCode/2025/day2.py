



def readTheFile(filename):
    with open(filename, 'r') as lines:
        content = lines.read().split(',')
        return content


def checkifRepeatsItSelf(aValue):
    aValueStr = str(aValue)

    if len(aValueStr) % 2 == 0:
        theMiddle = int(len(aValueStr) / 2)
        partOne = aValueStr[:theMiddle]
        partTwo = aValueStr[theMiddle:]

        if partOne == partTwo:
            return aValue

    return 0


def part1():
    print('Part 1')

    test = False

    if test:
        content = readTheFile('Resources/day2Training.txt')
    else:
        content = readTheFile('Resources/day2.txt')

    invalidIDs = 0
    for theRange in content:
        startStr, lastStr = theRange.split('-')
        startID = int(startStr)
        lastID = int(lastStr)
        for value in range(startID, lastID+1):
            #print(value)
            invalidIDs += checkifRepeatsItSelf(value)

    print(invalidIDs)


def checkifRepeatsItSelfPart2(aValue):
    aValueStr = str(aValue)

    #check if all digits the same, if longer than one
    if len(aValueStr) > 1 and len(set(aValueStr)) == 1:
        return aValue

    if len(aValueStr) % 2 == 0:
        theMiddle = int(len(aValueStr) / 2)
        partOne = aValueStr[:theMiddle]
        partTwo = aValueStr[theMiddle:]

        if partOne == partTwo:
            return aValue
        elif len(aValueStr) > 2:
            #do check two by two
            firstTwoSigns = aValueStr[:2]

            for seconds in range(2, len(aValueStr), 2):
                if firstTwoSigns != aValueStr[seconds:seconds + 2]:
                    return 0
            return aValue

    elif len(aValueStr) % 3 == 0:
        #if they are not even we have to check, part by part

        aThird = int(len(aValueStr) / 3)
        firstThird = aValueStr[:aThird]

        for thirds in range(aThird, len(aValueStr), 3):
            if firstThird != aValueStr[thirds:thirds+3]:
                return 0

        return aValue
    return 0

def part2():
    print('Part 2')

    test = False

    if test:
        content = readTheFile('Resources/day2Training.txt')
    else:
        content = readTheFile('Resources/day2.txt')

    invalidIDs = 0
    for theRange in content:
        startStr, lastStr = theRange.split('-')
        startID = int(startStr)
        lastID = int(lastStr)
        for value in range(startID, lastID+1):
            #print(value)
            invalidIDs += checkifRepeatsItSelfPart2(value)

    print(invalidIDs)

if __name__ == '__main__':
    #part1()
    #checkifRepeatsItSelfPart2(2121212121)
    part2()