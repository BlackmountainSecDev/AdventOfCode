



def readTheFile(filename):
    with open(filename, 'r') as file:
        lines = file.read()

        grid = [line for line in lines.split('\n')]


    return grid


START = 'S'

def part1():

    test = False

    if test:
        grid = readTheFile('Resources/day7Training.txt')
    else:
        grid = readTheFile('Resources/day7.txt')

    #find startPos
    #currentRow = 0
    startCol = grid[0].find(START)
    currentCols =  set()
    currentCols.add(startCol)



    minCol = 0
    maxCol = len(grid[0])

    maxRow = len(grid)
    splitCounter = 0
    for row in range(1, maxRow):
        nextCols = set()
        while currentCols:
            col = currentCols.pop()
            if grid[row][col] == '.':
                nextCols.add(col)
            else:
                splitCounter += 1
                leftCol = col - 1
                if minCol <= leftCol:
                    nextCols.add(leftCol)
                rightCol = col + 1
                if rightCol < maxCol:
                    nextCols.add(rightCol)

        currentCols = nextCols

    print(splitCounter)


def part2():

    test = True

    if test:
        grid = readTheFile('Resources/day7Training.txt')
    else:
        grid = readTheFile('Resources/day7.txt')

    startCol = grid[0].find(START)
    # Dictionary: Spalte -> Anzahl der Wege zu dieser Spalte
    colCounts = {startCol: 1}

    maxCol = len(grid[0])
    maxRow = len(grid)

    for row in range(1, maxRow):
        nextColCounts = {}

        for col, count in colCounts.items():
            if grid[row][col] == '.':
                nextColCounts[col] = nextColCounts.get(col, 0) + count
            else:
                # Links
                if col - 1 >= 0:
                    nextColCounts[col - 1] = nextColCounts.get(col - 1, 0) + count
                # Rechts
                if col + 1 < maxCol:
                    nextColCounts[col + 1] = nextColCounts.get(col + 1, 0) + count

        colCounts = nextColCounts

    total = sum(colCounts.values())
    print(total)


if __name__ == '__main__':
    #part1()
    part2()