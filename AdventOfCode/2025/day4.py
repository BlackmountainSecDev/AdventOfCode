



def readTheFile(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        content = []
        for line in lines:
            line = line.replace('\n','')
            #content.append(line)
            content.append([sign for sign in line])

        return content





def part1():
    print('Part 1')

    test = False

    if test:
        content = readTheFile('Resources/day4Training.txt')
    else:
        content = readTheFile('Resources/day4.txt')

    minRow = 0
    minCol = 0
    maxRow = len(content)
    maxCol = len(content[0])


    neighbours =  [(-1,0), (-1, -1), (-1, 1), (1,0), (1, -1), (1, 1), (0,-1), (0,1)]
    #

    removable = 0
    for currentRow in range(0, maxRow):
        for currentCol in range(0, maxCol):
            if content[currentRow][currentCol] == '@':
                #check neighbours
                neighbourCounter = 0
                for dr, dc in neighbours:
                    nr, nc = currentRow + dr, currentCol + dc
                    if 0 <= nr < maxRow and 0 <= nc < maxCol and content[nr][nc] in ('@'):
                        neighbourCounter += 1

                if neighbourCounter < 4:
                    removable += 1

    print(removable)



def part2():
    print('Part 2')

    test = False

    if test:
        content = readTheFile('Resources/day4Training.txt')
    else:
        content = readTheFile('Resources/day4.txt')

    minRow = 0
    minCol = 0
    maxRow = len(content)
    maxCol = len(content[0])


    neighbours =  [(-1,0), (-1, -1), (-1, 1), (1,0), (1, -1), (1, 1), (0,-1), (0,1)]
    #



    removedall = 0
    removed = True
    while removed:
        removedinRound = 0
        toRemove = []
        for currentRow in range(0, maxRow):
            for currentCol in range(0, maxCol):
                if content[currentRow][currentCol] == '@':
                    #check neighbours
                    neighbourCounter = 0
                    for dr, dc in neighbours:
                        nr, nc = currentRow + dr, currentCol + dc
                        if 0 <= nr < maxRow and 0 <= nc < maxCol and content[nr][nc] in ('@'):
                            neighbourCounter += 1

                    if neighbourCounter < 4:
                        removedinRound += 1
                        toRemove.append((currentRow, currentCol))


        removedall += removedinRound

        for pos in toRemove:
            content[pos[0]][pos[1]] = '.'

        if removedinRound == 0:
            removed = False

    print(removedall)


if __name__ == '__main__':
    part1()
    part2()