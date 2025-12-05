

def readTheFile(filename):
    with open(filename, 'r') as file:
        lines = file.read()
        ranges, ids = lines.split('\n\n')

        ranges = [theRange.split('-') for theRange in ranges.split('\n')]

        ranges = [
            [int(item) for item in sublist]  # Innere List Comp: Wandelt '1', '10' in 1, 10 um
            for sublist in ranges  # Äußere List Comp: Iteriert über die äußere Liste
        ]

        ids = [int(theID) for theID in  ids.split('\n')]

        return ids, ranges


def part1():
    print('Part 1')

    test = False

    if test:
        ids, ranges = content = readTheFile('Resources/day5Training.txt')
    else:
        ids,ranges = content = readTheFile('Resources/day5.txt')

    freshCounter = 0
    for theID in ids:
        for theRange in ranges:
            x, y = theRange
            if x <= theID <= y:
                freshCounter += 1
                break


    print(f'freshCounter: {freshCounter}')




def part2():
    print('Part 2')

    test = False

    if test:
        ids, ranges = content = readTheFile('Resources/day5Training.txt')
    else:
        ids,ranges = content = readTheFile('Resources/day5.txt')

    ranges = sorted(ranges, key=lambda x: x[0])

    currentRange = ranges.pop(0)
    rangeAmount = 0
    while ranges:
        nextRange = ranges.pop(0)
        if currentRange[1] < nextRange[0]:
            rangeAmount += currentRange[1] - currentRange[0] + 1
            currentRange = nextRange
        else:
            currentRange[1] = max(currentRange[1], nextRange[1])

    rangeAmount += currentRange[1] - currentRange[0] + 1

    print(f'rangeAmount: {rangeAmount}')


if __name__ == '__main__':
    part1()
    part2()