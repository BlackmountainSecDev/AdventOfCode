def readTheFile():
    with open('Resources/day7Resource.txt', 'r') as lines:
    #with open('Resources/day7ResourceTraining.txt', 'r') as lines:
        return [line.strip() for line in lines.readlines()]
    #[ lines]


allCombinations = {}
def getPossibleCombinations(paraNumber):

    if paraNumber in allCombinations.keys():
        return allCombinations[paraNumber]

    possibleCombinations = 2 ** paraNumber
    allCombinations[paraNumber] = possibleCombinations
    return  possibleCombinations

allZerosAndOnes = {}
def getZerosAndOnes(parameter):

    if parameter in allZerosAndOnes.keys():
        return allZerosAndOnes[parameter].copy()

    a, binzahl = bin(parameter).split('b')
    allZerosAndOnes[parameter] = [int(x) for x in binzahl][::-1]
    return allZerosAndOnes[parameter].copy()


def part1():
    allLines = readTheFile()

    theRightOnes = []
    for line in allLines:
        res, numbersStr = line.split(':')
        res = int(res)
        originalNumbers = list(map(int, numbersStr.split()))

        possibleCombinations = getPossibleCombinations((len(originalNumbers)-1))


        #if res == 292:
        #    print('aha')
        for aTry in range(0, possibleCombinations):
            numbers = originalNumbers.copy()
            zerosAndOnes = getZerosAndOnes(aTry)
            #a, binzahl = bin(aTry).split('b')
            #zerosAndOnes = [int(x) for x in binzahl][::-1]

            countedNumber = numbers.pop(0)

            for op in zerosAndOnes:
                if op == 0:
                    countedNumber = countedNumber + numbers.pop(0)
                else:
                    countedNumber = countedNumber * numbers.pop(0)

            countedNumber += sum(numbers)

            if res == countedNumber:
                theRightOnes.append(countedNumber)
                break



    print(theRightOnes)
    print(sum(theRightOnes))

def getPossibleCombinationsBase3(paraNumber):
    if paraNumber in allCombinations.keys():
        return allCombinations[paraNumber]

    possibleCombinations = 3 ** paraNumber
    allCombinations[paraNumber] = possibleCombinations
    return  possibleCombinations


def generateOperatorSequence(number, length):
    sequence = []
    for _ in range(length):
        sequence.append(number % 3)
        number //= 3 # Ganzzahldivision durch 3 ohne Rest
    return sequence


def part2():
    allLines = readTheFile()

    theRightOnes = []
    for line in allLines:
        res, numbersStr = line.split(':')
        res = int(res)
        originalNumbers = list(map(int, numbersStr.split()))

        possibleCombinations = getPossibleCombinationsBase3((len(originalNumbers)-1))


        #if res == 292:
        #    print('aha')
        for aTry in range(0, possibleCombinations):
            numbers = originalNumbers.copy()
            zerosOnesAndTwos = generateOperatorSequence(aTry, len(originalNumbers) - 1)

            countedNumber = numbers.pop(0)

            for op in zerosOnesAndTwos:
                if op == 0:
                    countedNumber = countedNumber + numbers.pop(0)
                elif op == 1:
                    countedNumber = countedNumber * numbers.pop(0)
                else:
                    countedNumber = int(str(countedNumber)+str(numbers.pop(0)))

            countedNumber += sum(numbers)

            if res == countedNumber:
                theRightOnes.append(countedNumber)
                break



    print(theRightOnes)
    print(sum(theRightOnes))

if __name__ == '__main__':
    #part1()
    part2()