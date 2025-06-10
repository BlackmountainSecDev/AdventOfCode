def readTheFile():
    with open('Resources/day9Resource.txt', 'r') as lines:
    #with open('Resources/day9ResourceTraining.txt', 'r') as lines:
        return lines.readlines()
    #[ lines]



def part1():
    '''
    **************************************
    * Did everything right               *
    * at the first try                   *
    *                                    *
    * Solution: 6301895872542            *
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






if __name__ == '__main__':
    part1()