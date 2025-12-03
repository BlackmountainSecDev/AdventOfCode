


def readTheFile(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

        content = []
        for line in lines:
            line = line.replace('\n','')
            #content.append(line)
            content.append([int(ziffer) for ziffer in line])

    return content


def findHighestPossibleValue(batteryRow, lenghtOfValue):


    wholeValue = 0

    while lenghtOfValue:
        lastallowdPos = len(batteryRow) - lenghtOfValue + 1
        highestValue = max(batteryRow[:lastallowdPos])
        indexOfHighestValue = batteryRow.index(highestValue)
        highestValue *= (10 ** (lenghtOfValue - 1))
        wholeValue += highestValue
        batteryRow = batteryRow[indexOfHighestValue+1:]
        lenghtOfValue -= 1

    return wholeValue


def part1And2():
    test = False


    if test:
        content = readTheFile('Resources/day3Training.txt')
    else:
        content = readTheFile('Resources/day3.txt')


    allValuesPar1 = 0
    allValuesPar2 = 0
    for row in content:
        allValuesPar1 += findHighestPossibleValue(row, 2)
        allValuesPar2 += findHighestPossibleValue(row, 12)

    print(allValuesPar1)
    print(allValuesPar2)



if __name__ == '__main__':
    part1And2()