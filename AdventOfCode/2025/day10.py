from functools import reduce
from itertools import combinations
from functools import reduce
import operator

def readTheFile(filename):
    content = []
    with open(filename, 'r') as file:
        lines = file.read().split('\n')

        for line in lines:
            firstPos = line.index(']')
            lastPos  = line.index('{')
            indicatorLightDiagram = [sign for sign in line[1:firstPos]]
            buttonWiringsStr = line[firstPos+2:lastPos-1]
            buttonWirings = [
                [int(num) for num in group.replace('(', '').replace(')', '').split(',')]
                for group in buttonWiringsStr.split(' ')
            ]
            joltagesStr = line[lastPos+1:-1]
            joltages = [int(val) for val in joltagesStr.split(',')]


            content.append([indicatorLightDiagram, buttonWirings, joltages])

    return content


def xor_vec(a, b):
    return [x ^ y for x, y in zip(a, b)]

def part1():
    print('Part 1')

    test = False

    if test:
        content = readTheFile('Resources/day10Training.txt')
    else:
        content = readTheFile('Resources/day10.txt')


    allCombos = 0
    for currentLine in content:
        indicationLightTarget, buttonWirings, joltages = currentLine

        targetBin = [1 if c == '#' else 0 for c in indicationLightTarget]
        currentLen = len(targetBin)
        targetNumber = int(''.join(map(str, targetBin)), 2)


        allWirings = []
        for currentWiring in buttonWirings:
            lst = [0] * currentLen
            for pos in currentWiring:
                lst[pos] = 1

            allWirings.append(int(''.join(map(str, lst)), 2))


        shortestCombo = float('inf')
        # Länge der Kombinationen variieren: 2, 3, ... bis len(numbers)
        for r in range(1, len(allWirings) + 1):
            for combo in combinations(allWirings, r):
                # XOR aller Zahlen in der Kombination
                result = reduce(operator.xor, combo)

                if result == targetNumber:
                    if len(combo) < shortestCombo:
                        print(f"{combo} -> {result}")
                        shortestCombo = len(combo)

        allCombos += shortestCombo

    print(allCombos)

if __name__ == '__main__':
    part1()