def readTheFile(filename):
    with open(filename, 'r') as file:
        data = file.read()

        theBytes = data.split('\n')

        theBytes = [[int(num) for num in aByte.split(',')] for aByte in theBytes]

    return theBytes



def part1():

    isTraining = True

    print('Part 1')
    start= [0, 0]

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    if isTraining:
        theBytes = readTheFile('Resources/day18ResourceTraining.txt')
        rows = 7  # Training
        cols = 7  # Training
        amountOfBytes = 12
    else:
        theBytes = readTheFile('Resources/day18Resource.txt')
        rows = 71
        cols = 71
        amountOfBytes = 1024

    end = [rows, cols]


    map_1d = ['.'] * (rows * cols)
    map_2d = []

    '''
    #as for loop
    for i in range(rows):
        row = map_1d[i * cols: (i + 1) * cols]
        map_2d.append(row)
    '''

    # as comprehension
    map_2d = [map_1d[i * cols: (i + 1) * cols] for i in range(rows)]
    #print(theBytes)



    for pos in range(0, amountOfBytes):
        x, y = theBytes[pos]
        map_2d[y][x] = '#'


    for i in range (0, len(map_2d)):
        print(map_2d[i])




if __name__ == '__main__':
    part1()