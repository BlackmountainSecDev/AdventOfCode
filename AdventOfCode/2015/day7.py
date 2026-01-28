
import re

assignments = {}

def readTheFile(filename):
    with open(filename, 'r') as lines:
        return lines.read().split('\n')


def dissolve(input):
    wholestuff = input.split(' ')
    #print(wholestuff)

    if len(wholestuff) > 1:

        if wholestuff[0] == 'NOT':
            #print('NOT')

            if type(assignments[wholestuff[1]]) == str:
                assignments[wholestuff[1]] = dissolve(assignments[wholestuff[1]])


            return ~assignments[wholestuff[1]] & 65535

        elif wholestuff[1] == 'RSHIFT':
            #print('RSHIFT')
            if type(assignments[wholestuff[0]]) == str:
                assignments[wholestuff[0]] = dissolve(assignments[wholestuff[0]])

            return  assignments[wholestuff[0]] >> int(wholestuff[2])

        elif wholestuff[1] == 'LSHIFT':
            #print('LSHIFT')
            if type(assignments[wholestuff[0]]) == str:
                assignments[wholestuff[0]] = dissolve(assignments[wholestuff[0]])

            return assignments[wholestuff[0]] << int(wholestuff[2])

        elif wholestuff[1] == 'AND':
            #print('AND')
            if wholestuff[0].isdigit():
                val1 = int(wholestuff[0])
            elif type(assignments[wholestuff[0]]) == str:
                assignments[wholestuff[0]] = dissolve(assignments[wholestuff[0]])
                val1 = assignments[wholestuff[0]]
            else:
                val1 = assignments[wholestuff[0]]

            if wholestuff[2].isdigit():
                val2 = int(wholestuff[2])
            elif type(assignments[wholestuff[2]]) == str:
                assignments[wholestuff[2]] = dissolve(assignments[wholestuff[2]])
                val2 = assignments[wholestuff[2]]
            else:
                val2 = assignments[wholestuff[2]]

            return val1 & val2

        elif wholestuff[1] == 'OR':
            #print('OR')
            if wholestuff[0].isdigit():
                val1 = int(wholestuff[0])
            elif type(assignments[wholestuff[0]]) == str:
                assignments[wholestuff[0]]  = dissolve(assignments[wholestuff[0]])
                val1 = assignments[wholestuff[0]]
            else:
                val1 = assignments[wholestuff[0]]

            if wholestuff[2].isdigit():
                val2 = int(wholestuff[2])
            elif type(assignments[wholestuff[2]]) == str:
                assignments[wholestuff[2]] = dissolve(assignments[wholestuff[2]])
                val2 = assignments[wholestuff[2]]
            else:
                val2 = assignments[wholestuff[2]]


            return val1 | val2
    else:
        if assignments[wholestuff[0]].isdigit():
            return assignments[wholestuff[0]]
        else:
            return dissolve(assignments[wholestuff[0]])




def part1():

    test = False

    if test:
        content = readTheFile('Resources/day7Training.txt')
    else:
        content = readTheFile('Resources/day7.txt')

    instructions = []

    for enty in content:
        splittedEntry = enty.split(' -> ')
        if splittedEntry[0].isdigit():
            assignments[splittedEntry[1]] = int(splittedEntry[0])

        else:
            assignments[splittedEntry[1]] = splittedEntry[0]



    for key, value in assignments.items():
        if type(value) == str:
            assignments[key] = dissolve(value)

    print(assignments['a'])


def part2():

    test = False

    if test:
        content = readTheFile('Resources/day7Training.txt')
    else:
        content = readTheFile('Resources/day7.txt')

    instructions = []

    for enty in content:
        splittedEntry = enty.split(' -> ')
        if splittedEntry[0].isdigit():
            if splittedEntry[1]  == 'b':
                assignments[splittedEntry[1]] = 46065
            else:
                assignments[splittedEntry[1]] = int(splittedEntry[0])

        else:
            assignments[splittedEntry[1]] = splittedEntry[0]



    for key, value in assignments.items():
        if type(value) == str:
            assignments[key] = dissolve(value)

    print(assignments['a'])


if __name__ == '__main__':
    #part1()
    part2()