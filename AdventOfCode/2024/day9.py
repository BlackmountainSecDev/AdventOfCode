def readTheFile():
    with open('Resources/day9Resource.txt', 'r') as lines:
    #with open('Resources/day9ResourceTraining.txt', 'r') as lines:
        return lines.readlines()
    #[ lines]



def part1():
    '''
    **************************************
    *                                    *
    * Solution: 6301895872542            *
    *                                    *
    **************************************
    '''
    print('Part 1')

    values = [int(x) for x in readTheFile()[0]]
    #print(values)
    #print()

    newList = []
    isValue = True
    idCounter = 0
    for theLength in values:

        if isValue:
            toAdd = idCounter
            idCounter +=1
            isValue = False

        else:
            toAdd = '.'
            isValue = True

        for counter in range(0, theLength):
            newList.append(toAdd)

    #print(newList)

    reachedTheEnd = False
    theIndex = 0

    while reachedTheEnd == False:
        if newList[theIndex] == '.':
            valToAdd = '.'
            while valToAdd == '.':
                valToAdd = newList.pop(-1)


            if theIndex >= len(newList):
                newList.append(valToAdd)
            else:
                newList[theIndex] = valToAdd


        theIndex += 1
        if theIndex >= len(newList):
            reachedTheEnd = True

    #print(newList)

    wholeValue = 0
    for index, value in enumerate(newList):
        wholeValue += index*value

    print(wholeValue)



def part2():
    '''
    **************************************
    *                                    *
    * Solution: 6431472344710            *
    *                                    *
    **************************************
    '''
    print('Part 2')

    #content = readfile('Resources/day9.txt')
    content = [int(x) for x in readTheFile()[0]]

    counter = 0
    Dot = False
    newContent = []
    for length in content:
        if Dot:
            for pos in range(length):
                newContent.append('.')

            Dot = False
        else:
            for pos in range(length):
                newContent.append(counter)

            counter += 1
            Dot = True

    #print(newContent)

    alreadyMoved = set()
    DOT = '.'
    lastPosOfValue = len(newContent) - 1
    theMaxLenght = len(newContent)
    while lastPosOfValue > 0:
        if newContent[lastPosOfValue] != DOT and newContent[lastPosOfValue] not in alreadyMoved:
            theValue = newContent[lastPosOfValue]
            firstPosOfValue = newContent.index(theValue)

            alreadyMoved.add(theValue)

            lenghtOfValue = lastPosOfValue - firstPosOfValue + 1

            firstPosOfDot = newContent.index(DOT)

            while firstPosOfDot < theMaxLenght and firstPosOfDot < firstPosOfValue:
                #find last Pos of Dot
                currentPosOfDot = firstPosOfDot +1

                StopIt = False
                while newContent[currentPosOfDot] == DOT:
                    currentPosOfDot += 1

                    if currentPosOfDot >= theMaxLenght:
                        StopIt = True
                        break

                if StopIt:
                    break

                lenghtOfDot = currentPosOfDot - firstPosOfDot

                if lenghtOfDot >= lenghtOfValue:

                    for counter in range(lenghtOfValue):
                        newContent[firstPosOfDot+counter] = newContent[lastPosOfValue-counter]
                        newContent[lastPosOfValue-counter] = DOT

                    break

                firstPosOfDot = newContent.index(DOT, firstPosOfDot+1)

            lastPosOfValue = firstPosOfValue - 1

        else:
            lastPosOfValue -= 1


    #print(newContent)

    aggregated = 0
    for currentPosition in range(len(newContent)):
        if newContent[currentPosition] != DOT:
            aggregated += currentPosition * newContent[currentPosition]

    print(aggregated)

if __name__ == '__main__':
    part1()
    part2()