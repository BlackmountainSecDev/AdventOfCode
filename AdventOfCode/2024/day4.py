import re

def readTheFile():
    with open('Resources/day4Resource.txt', 'r') as lines:
        return [line.strip() for line in lines.readlines()]

SEARCHWORD = 'XMAS'
SEARCHWORDREVERSE = 'SAMX'


def part1():
    originalLines = readTheFile()

    #reversedLines = [line[::-1] for line in originalLines]

    #building top down
    topDownLines = []
    #downTopLines = []

    maxAmountofColumns = len(originalLines[0])
    maxAmountOfRows = len(originalLines)
    for theColumnIndex in range(0, maxAmountofColumns):
        helperLine = ''
        for theRowIndex in range(0, maxAmountOfRows):
            helperLine += originalLines[theRowIndex][theColumnIndex]
        topDownLines.append(helperLine)
        #downTopLines.append(helperLine[::-1])

    # building diagonal left to right
    diagLeftToDown = []
    outerColumnIndex = 0

    while outerColumnIndex < maxAmountofColumns:
        helperLine = ''
        theRowIndex = 0
        for innerColumnIndex in range(outerColumnIndex, maxAmountofColumns):
            if theRowIndex < maxAmountOfRows:
                helperLine += originalLines[theRowIndex][innerColumnIndex]
                theRowIndex += 1
                #print(helperLine)

        diagLeftToDown.append(helperLine)
        outerColumnIndex += 1


    outerRowIndex = 1
    while outerRowIndex < maxAmountOfRows:
        helperLine = ''
        theColumnIndex = 0
        for innerRowIndex in range(outerRowIndex, maxAmountOfRows):
            if theColumnIndex < maxAmountofColumns:
                helperLine += originalLines[innerRowIndex][theColumnIndex]
                theColumnIndex += 1
                #print(helperLine)


        diagLeftToDown.append(helperLine)
        outerRowIndex +=1


    # building diagonal left to right
    diagRightToDown = []
    outerColumnIndex = maxAmountofColumns - 1

    while outerColumnIndex >= 0:
        helperLine = ''
        theRowIndex = 0
        for innerColumnIndex in range(outerColumnIndex, -1, -1):
            if theRowIndex < maxAmountOfRows:
                helperLine += originalLines[theRowIndex][innerColumnIndex]
                theRowIndex += 1
                #print(helperLine)

        diagRightToDown.append(helperLine)
        outerColumnIndex -= 1

    outerRowIndex = 1
    while outerRowIndex < maxAmountOfRows:
        helperLine = ''
        theColumnIndex = maxAmountofColumns-1
        for innerRowIndex in range(outerRowIndex, maxAmountOfRows):
            if theColumnIndex >= 0:
                helperLine += originalLines[innerRowIndex][theColumnIndex]
                theColumnIndex -= 1
                #print(helperLine)

        diagRightToDown.append(helperLine)
        outerRowIndex +=1


    #building diagonal left to right
    allAppearances = 0

    for line in originalLines:
        allAppearances += len(re.findall(SEARCHWORD, line))
        allAppearances += len(re.findall(SEARCHWORDREVERSE, line))

    for line in topDownLines:
        allAppearances += len(re.findall(SEARCHWORD, line))
        allAppearances += len(re.findall(SEARCHWORDREVERSE, line))

    for line in diagLeftToDown:
        allAppearances += len(re.findall(SEARCHWORD, line))
        allAppearances += len(re.findall(SEARCHWORDREVERSE, line))

    for line in diagRightToDown:
        allAppearances += len(re.findall(SEARCHWORD, line))
        allAppearances += len(re.findall(SEARCHWORDREVERSE, line))

    print(allAppearances)



def part2():
    originalLines = readTheFile()
    maxAmountofColumns = len(originalLines[0])
    maxAmountOfRows = len(originalLines)

    counter = 0
    for rowCounter in range(1, maxAmountOfRows-1):
        for columCounter in range (1, maxAmountofColumns-1):
            if originalLines[rowCounter][columCounter] == 'A':
                if (((originalLines[rowCounter-1][columCounter-1] == 'M' and originalLines[rowCounter+1][columCounter+1] == 'S')
                or (originalLines[rowCounter-1][columCounter-1] == 'S' and originalLines[rowCounter+1][columCounter+1] == 'M'))
                and
                ((originalLines[rowCounter+1][columCounter-1] == 'M' and originalLines[rowCounter-1][columCounter+1] == 'S')
                or (originalLines[rowCounter+1][columCounter-1] == 'S' and originalLines[rowCounter-1][columCounter+1] == 'M'))):
                    counter += 1

    print(counter)


if __name__ == '__main__':
    part1()
    part2()