import numpy as np
import re


def readTheFile(filename):
    pattern = r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)'

    with open(filename, 'r') as lines:
        content = lines.read().split('\n')


        instructions = [
            [action, (int(x1), int(y1)), (int(x2), int(y2))]
            for action, x1, y1, x2, y2 in [re.match(pattern, line).groups() for line in content]
        ]

        return instructions




def part1():

    instructions = readTheFile('Resources/day6.txt')
    grid = np.zeros((1000, 1000), dtype=int)

    for oneInstruction in instructions:
        ins, startTuple, endTuple = oneInstruction
        yS, xS = startTuple
        yE, xE = endTuple

        if ins == 'toggle':
            for rowCounter in range(yS, yE+1):
                for columnCounter in range(xS, xE+1):
                    grid[rowCounter][columnCounter] = 1 - grid[rowCounter][columnCounter]
        else:
            val = 0
            if ins == 'turn on':
                val = 1

            for rowCounter in range(yS, yE+1):
                for columnCounter in range(xS, xE+1):
                    grid[rowCounter][columnCounter] = val

    print(np.sum(grid))


def part2():

    instructions = readTheFile('Resources/day6.txt')
    grid = np.zeros((1000, 1000), dtype=int)

    for oneInstruction in instructions:
        ins, startTuple, endTuple = oneInstruction
        yS, xS = startTuple
        yE, xE = endTuple

        if ins == 'turn off':
            for rowCounter in range(yS, yE+1):
                for columnCounter in range(xS, xE+1):
                    if grid[rowCounter][columnCounter] > 0:
                        grid[rowCounter][columnCounter] -= 1
        else:
            val = 2
            if ins == 'turn on':
                val = 1

            for rowCounter in range(yS, yE+1):
                for columnCounter in range(xS, xE+1):
                    grid[rowCounter][columnCounter] += val

    print(np.sum(grid))


if __name__ == '__main__':
    part1()
    part2()
