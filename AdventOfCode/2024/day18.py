def readTheFile(filename):
    with open(filename, 'r') as file:
        data = file.read()

        theBytes = data.split('\n')

        theBytes = [[int(num) for num in aByte.split(',')] for aByte in theBytes]

    return theBytes


'''
# adds every possible node (including the steps into the node, even it has already been visited) to the "queue"
# afterwards takes the node checks if it is the end or it has been already visited
# if none of them check the nodes around
'''
def breadthFirstSearch(start, end, maze):
    from collections import deque
    rows, cols = len(maze), len(maze[0])
    visited = set()
    queue = deque([(start[0], start[1], 0)])  # r, c, steps

    while queue:
        r, c, steps = queue.popleft()
        if [r, c] == end:
            return steps
        if (r, c) in visited:
            continue
        visited.add((r, c))

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] in ('.'):
                queue.append((nr, nc, steps + 1))
    return float('inf')


def part1():

    isTraining = False

    print('Part 1')

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

    start = [0, 0]
    end = [rows-1, cols-1]

    map_1d = ['.'] * (rows * cols)

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


    #for i in range (0, len(map_2d)):
    #    print(map_2d[i])

    result = breadthFirstSearch(start, end, map_2d)

    print(result)




def part2():

    isTraining = False

    print('Part 2')


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

    start = [0, 0]
    end = [rows-1, cols-1]

    map_1d = ['.'] * (rows * cols)

    '''
    #as for loop
    for i in range(rows):
        row = map_1d[i * cols: (i + 1) * cols]
        map_2d.append(row)
    '''

    # as comprehension
    map_2d = [map_1d[i * cols: (i + 1) * cols] for i in range(rows)]
    #print(theBytes)


    result = 0
    while result != float('inf'):
        for pos in range(0, amountOfBytes):
            x, y = theBytes[pos]
            map_2d[y][x] = '#'

        result = breadthFirstSearch(start, end, map_2d)

        amountOfBytes += 1
        if amountOfBytes >= len(theBytes):
            result = float('inf')

    print(theBytes[amountOfBytes-2])



if __name__ == '__main__':
    part1()
    part2()