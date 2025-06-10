

def readTheFile():
    with open('Resources/day5Resource.txt', 'r') as lines:
        return [line.strip() for line in lines.readlines()]


def part1():
    content = readTheFile()

    map =[]

    theOrderDict = {}

    while content[0] != '':
        map.append(content.pop(0))
        first, second = map[len(map)-1].split('|')

        first = int(first)
        second = int(second)

        if first in theOrderDict.keys():
            theOrderDict[first].append(second)
        else:
            theOrderDict[first] = [second]

    content.pop(0)
    wholeNumber = 0

    while len(content) > 0:
        currentLine = [int(x) for x in content.pop(0).split(',')]
        inList = True

        for outerIndex in range(0, len(currentLine)-1):
            if currentLine[outerIndex] in theOrderDict.keys():
                currentValues = theOrderDict[currentLine[outerIndex]]
                for innerIndex in range(outerIndex+1, len(currentLine)):
                    if currentLine[innerIndex] not in currentValues:
                        inList = False
                        break
            else:
                inList = False

        if inList:
            middleIndex = int((len(currentLine)-1)/2)
            wholeNumber += currentLine[middleIndex]


    print(wholeNumber)




def checkIfItsRight(paraCurrentLine, paratheOrderDict):

    for outerIndex in range(0, len(paraCurrentLine) - 1):
        if paraCurrentLine[outerIndex] in paratheOrderDict.keys():
            currentValues = paratheOrderDict[paraCurrentLine[outerIndex]]
            for innerIndex in range(outerIndex + 1, len(paraCurrentLine)):
                if paraCurrentLine[innerIndex] not in currentValues:
                    return outerIndex#paraCurrentLine[outerIndex]

        else:
            return outerIndex#paraCurrentLine[outerIndex]

    return -1


def part2():
    content = readTheFile()

    map = []

    theOrderDict = {}

    while content[0] != '':
        map.append(content.pop(0))
        first, second = map[len(map) - 1].split('|')

        first = int(first)
        second = int(second)

        if first in theOrderDict.keys():
            theOrderDict[first].append(second)
        else:
            theOrderDict[first] = [second]

    content.pop(0)
    fixedOnes = []
    wholeNumber = 0

    while len(content) > 0:
        currentLine = [int(x) for x in content.pop(0).split(',')]


        index = checkIfItsRight(currentLine, theOrderDict)
        if index != -1:
            result = currentLine[index]


            maxLength = len(currentLine)
            currentLine.pop(index)


            isRight = False
            while isRight == False:

                foundTemporaryRightPos = False

                newIndex = 0
                while foundTemporaryRightPos == False and newIndex < maxLength:
                    foundTemporaryRightPos = True
                    newline = currentLine.copy()
                    newline.insert(newIndex, result)


                    if newline[newIndex] in theOrderDict.keys():
                        currentValues = theOrderDict[newline[newIndex] ]
                        for innerIndex in range(newIndex+1, len(newline)):
                            if newline[innerIndex] not in currentValues:
                                foundTemporaryRightPos = False
                                break
                    else:
                        foundTemporaryRightPos = False


                    newIndex += 1


                index = checkIfItsRight(newline, theOrderDict)
                if index != -1:
                    currentLine = newline.copy()
                    result = currentLine[index]
                    maxLength = len(currentLine)
                    currentLine.pop(index)
                    isRight = False
                else:
                    isRight = True
                    fixedOnes.append(newline)
                    middleIndex = int((len(newline) - 1) / 2)
                    wholeNumber += newline[middleIndex]



    print(wholeNumber)




if __name__ == '__main__':
    part1()
    part2()