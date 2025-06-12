import re

def readTheFile(filename):
    with open(filename, 'r') as file:
        content = file.read()
    blocks = content.split('\n\n')

    splitedBlocks = [x.split('\n') for x in blocks]

    return splitedBlocks


def part1():
    numbers, functions = readTheFile('Resources/day24Resource.txt')
    #numbers, functions = readTheFile('Resources/day24ResourceTraining.txt')

    print(numbers)

    theDict = {}
    for aVal in numbers:
        k, v = aVal.split(':')
        theDict[k] = int(v)


    functions = sorted(functions, reverse=True)

    #print(functions)

    while len(functions) > 0:
        currentFuntion = functions.pop(0)
        val1, op, val2, waste, result  = currentFuntion.split()
        #print('aahaha')
        if val1 in theDict.keys() and val2 in theDict.keys():
            if op == 'AND':
                theDict[result] = theDict[val1] and theDict[val2]
            elif op == 'OR':
                theDict[result] = theDict[val1] or theDict[val2]
            else:
                theDict[result] = theDict[val1] ^ theDict[val2]
        else:
            functions.append(currentFuntion)


    aha =  [akey for akey in theDict.keys() if akey.startswith('z')]
    allZZZs = sorted(aha, reverse=True)

    aString = ''
    for aZ in allZZZs:
        aString += str(theDict[aZ])

    print(aString)
    print(int(aString, 2))


def part2():
    numbers, functions = readTheFile('Resources/day24Resource.txt')
    #numbers, functions = readTheFile('Resources/day24ResourceTraining.txt')

    print(numbers)

    theDict = {}
    for aVal in numbers:
        k, v = aVal.split(':')
        theDict[k] = int(v)


    functions = sorted(functions, reverse=True)


    while len(functions) > 0:
        currentFuntion = functions.pop(0)
        val1, op, val2, waste, result  = currentFuntion.split()
        #print('aahaha')
        if val1 in theDict.keys() and val2 in theDict.keys():
            if op == 'AND':
                theDict[result] = theDict[val1] and theDict[val2]
            elif op == 'OR':
                theDict[result] = theDict[val1] or theDict[val2]
            else:
                theDict[result] = theDict[val1] ^ theDict[val2]
        else:
            functions.append(currentFuntion)

    allXXXs = [akey for akey in theDict.keys() if akey.startswith('x')]
    allXXXs = sorted(allXXXs, reverse=True)

    allYYYs = [akey for akey in theDict.keys() if akey.startswith('y')]
    allYYYs = sorted(allYYYs, reverse=True)

    allZZZs =  [akey for akey in theDict.keys() if akey.startswith('z')]
    allZZZs = sorted(allZZZs, reverse=True)


    aXString = ''
    for aX in allXXXs:
        aXString += str(theDict[aX])

    aYString = ''
    for aY in allYYYs:
        aYString += str(theDict[aY])

    aZString = ''
    for aZ in allZZZs:
        aZString += str(theDict[aZ])


    print(aXString)
    aXInt = int(aXString, 2)
    print(aXInt)

    print(aYString)
    aYInt = int(aYString, 2)
    print(aYInt)

    newZInt = aXInt + aYInt
    print(newZInt)
    newZString = str(bin(newZInt))
    print(newZString[2:])

    print(aZString)
    print(int(aZString, 2))


if __name__ == '__main__':
    print('day24')
    #part1()
    part2()