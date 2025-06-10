def readTheFile():
    with open('Resources/day11Resource.txt', 'r') as lines:
    #with open('Resources/day11ResourceTraining.txt', 'r') as lines:
        return [int(char) for char in [line.strip() for line in lines.readlines()][0].split()]





def part1():
    initialLine = readTheFile()

    repeat = 25

    currentLine = initialLine.copy()


    for run in range(repeat):
        newLine = []
        for element in currentLine:
            if element == 0:
                newLine.append(1)

            elif len(str(element)) % 2 == 0:

                strElem = str(element)
                theLength = len(strElem)
                theHalf = int(theLength / 2)

                firstHalf = strElem[:theHalf]
                secondHalf = strElem[theHalf:]

                newLine.append(int(firstHalf))
                newLine.append(int(secondHalf))

            else:
                newLine.append(element*2024)

        print(f'{run+1}. {len(newLine)} - {len(currentLine)} = {len(newLine) - len(currentLine)}')
        currentLine = newLine.copy()

    print(len(currentLine))


def blink(currentCounter, maxCounter, theParameter):

    if currentCounter == maxCounter:
        return 1

    currentCounter += 1

    if theParameter == 0:
        return blink(currentCounter, maxCounter, 1)

    elif len(str(theParameter)) % 2 == 0:

        strElem = str(theParameter)
        theLength = len(strElem)
        theHalf = int(theLength / 2)

        firstHalf = int(strElem[:theHalf])
        secondHalf = int(strElem[theHalf:])

        return blink(currentCounter, maxCounter, firstHalf) + blink(currentCounter, maxCounter, secondHalf)

    else:
        return blink(currentCounter, maxCounter, theParameter * 2024)


def count_elements(tup):
    count = 0
    for elem in tup:
        if isinstance(elem, (tuple, list)):  # Prüfen, ob es ein verschachteltes Tuple oder eine Liste ist
            count += count_elements(elem)  # Rekursiver Aufruf
        else:
            count += 1  # Einfaches Element zählen
    return count




from functools import cache

@cache
def count(stone, steps):

    if steps == 0:
        return 1

    if stone == 0:
        return count(1, steps-1)

    string = str(stone)
    length = len(string)

    if length % 2 == 0:
        return count(int(string[:length // 2]), steps - 1) + count(int(string[length // 2:]), steps - 1)

    return count(stone*2024, steps - 1)


def part2():
    stones = readTheFile()
    print(sum(count(stone, 75) for stone in stones))


if __name__ == '__main__':
    part1()
    part2()