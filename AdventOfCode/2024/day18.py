import heapq
from collections import deque
import time


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
def breadthFirstSearch(start, goal, maze):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    queue = deque([(start[0], start[1], 0)])  # r, c, steps

    while queue:
        r, c, steps = queue.popleft()
        if [r, c] == goal:
            return steps
        if (r, c) in visited:
            continue
        visited.add((r, c))

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] in ('.'):
                queue.append((nr, nc, steps + 1))
    return float('inf')



def neighbors(r, c, maze):
    rows, cols = len(maze), len(maze[0])
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] in ('.'):
            yield (nr, nc)


def dijkstra(start, goal, maze):
    heap = [(0, start)]

    visited = set()
    dist = {start: 0}
    prev = {}

    while heap:
        current_dist, current = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            break

        for neighbor in neighbors(*current, maze):
            if neighbor in visited:
                continue
            tentative_dist = current_dist + 1
            if tentative_dist < dist.get(neighbor, float('inf')):
                dist[neighbor] = tentative_dist
                prev[neighbor] = current
                heapq.heappush(heap, (tentative_dist, neighbor))


    #if you want to have the path    
    path = []
    node = goal   
    while node != start:
        path.append(node)
        node = prev.get(node)
        if node is None:
            return float('inf')  # kein Pfad gefunden
    path.append(start)
    path.reverse()
    return path


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(start, goal, maze):
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start))

    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current_cost, current = heapq.heappop(open_set)

        if current == goal:
            # path reconstruction
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # backwards to forwards

        for neighbor in neighbors(*current, maze):
            tentative_g = g_score[current] + 1
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))

    return None


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

    startTimeBFS = time.time()
    resultBFS = breadthFirstSearch(start, end, map_2d)
    endTimeBFS = time.time()

    startTimeDijkstra = time.time()
    resultDijkstraPath = dijkstra((start[0], start[1]), (end[0], end[1]), map_2d)
    endTimeDijkstra = time.time()

    startTimeAStar = time.time()
    resutlAStarPath = a_star((start[0], start[1]), (end[0], end[1]), map_2d)
    endTimeAStar = time.time()

    print(resultBFS)
    print("BFS:  %s seconds" % (endTimeBFS - startTimeBFS))

    print(len(resultDijkstraPath)-1) #startpoint doesn't count
    print("Dijkstra: %s seconds" % (endTimeDijkstra - startTimeDijkstra))

    #print(resultAStarCameFrom)  # startpoint doesn't count
    print(len(resutlAStarPath)-1)
    print("AStarSearch: %s seconds" % (endTimeAStar - startTimeAStar))



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
    startTime = time.time()
    while result != float('inf'):
        for pos in range(0, amountOfBytes):
            x, y = theBytes[pos]
            map_2d[y][x] = '#'

        #result = breadthFirstSearch(start, end, map_2d)
        #result = dijkstra((start[0], start[1]), (end[0], end[1]), map_2d)
        result = a_star((start[0], start[1]), (end[0], end[1]), map_2d)

        amountOfBytes += 1
        if amountOfBytes >= len(theBytes):
            result = float('inf')

    endTime = time.time()

    print(theBytes[amountOfBytes-2])
    print("Time: %s seconds" % (endTime - startTime))



if __name__ == '__main__':
    #part1()
    part2()