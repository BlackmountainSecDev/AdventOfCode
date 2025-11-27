import heapq
from collections import deque



def readTheFile(filename):
    with open(filename, 'r') as file:
        maze_str = file.read()

    return [list(line) for line in maze_str.strip().split('\n')]



# helperfunction
def neighbors(r, c, maze, rows, cols):
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] in ('.', 'E'):
            yield (nr, nc), (dr, dc)





# Dijkstra-Algorithm
def dijkstraCost(start, end, maze, rows, cols, startDir):
    heap = [(0, start, startDir)]
    visited = set()
    dist = {start: 0}
    prev = {}

    while heap:
        current_dist, current, currentDir = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)

        if current == end:
            break

        for neighbor, neighborDir in neighbors(*current, maze, rows, cols):
            if neighbor in visited:
                continue

            if neighborDir == currentDir:
                tentative_dist = current_dist + 1
            else:
                tentative_dist = current_dist + 1001


            if tentative_dist < dist.get(neighbor, float('inf')):
                dist[neighbor] = tentative_dist
                prev[neighbor] = current
                heapq.heappush(heap, (tentative_dist, neighbor, neighborDir))

    #send costs
    return dist[end]


class customHeap:
    def __init__(self, start, startDir):
        self.current = start
        self.distance = 0
        self.direction = startDir
        self.visited = set()
        self.dist = {start: 0}
        self.prev = {}


    def initWithAll(self, theDistance, theVisited, theDist, thePrev):
        self.distance = theDistance
        self.visited = theVisited
        self.dist = theDist
        self.prev = thePrev


def dijkstraAllPossWays(start, end, maze, rows, cols, startDir):
    currentHeap = customHeap(start, startDir)
    allHeaps = [currentHeap]
    finalHeaps = []
    #currentHeap = allHeaps[0]
    #visited = set()
    #dist = {start: 0}
    #prev = {}

    while allHeaps:
        currentHeap = allHeaps.pop(0)
        #while currentHeap:
            #current_dist, current, currentDir, visited = heapq.heappop(currentHeap)


        if currentHeap.current in currentHeap.visited:
            continue

        currentHeap.visited.add(currentHeap.current)

        if currentHeap.current == end:
            #newHeap = customHeap(neighbor, neighborDir)
            #newHeap.initWithAll(tentative_dist, currentHeap.visited.copy(), currentHeap.dist.copy(),
            #                    currentHeap.prev.copy())
            #newHeap.dist[neighbor] = tentative_dist
            #newHeap.prev[neighbor] = currentHeap.current
            #print(f'currentHeap.distance : {currentHeap.distance }')
            if len(finalHeaps) == 0 or currentHeap.distance == finalHeaps[0].distance:
                finalHeaps.append(currentHeap)
            elif currentHeap.distance < finalHeaps[0].distance:
                finalHeaps = []
                finalHeaps.append(currentHeap)



            #break
        else:
            for neighbor, neighborDir in neighbors(*currentHeap.current, maze, rows, cols):
                if neighbor in currentHeap.visited:
                    continue

                if neighborDir == currentHeap.direction:
                    tentative_dist = currentHeap.distance + 1
                else:
                    tentative_dist = currentHeap.distance + 1001


                if tentative_dist < currentHeap.dist.get(neighbor, float('inf')):
                    newHeap = customHeap(neighbor, neighborDir)
                    newHeap.initWithAll(tentative_dist, currentHeap.visited.copy(), currentHeap.dist.copy(),
                                        currentHeap.prev.copy())

                    newHeap.dist[neighbor] = tentative_dist
                    newHeap.prev[neighbor] = currentHeap.current

                    allHeaps.append(newHeap)
                else:
                    print('ahaha ')

        #send costs
    return finalHeaps
#    print(finalHeaps)

# Finden von Start (S) und Ende (E)
def find_pos(char, theMap):
    for r in range(len(theMap)):
        for c in range(len(theMap[0])):
            if theMap[r][c] == char:
                return r, c
    return None


def part1():
    print('Part 1')

    TEST = False

    MINROW, MINCOL = 0, 0

    if TEST:
        maze = readTheFile('Resources/day16ResourceTraining.txt')
    else:
        maze = readTheFile('Resources/day16Resource.txt')

    MAXROW = len(maze)
    MAXCOL = len(maze[0])



    start = find_pos('S', maze)
    end = find_pos('E', maze)

    costs = dijkstraCost(start, end, maze, MAXROW, MAXCOL, (0, 1))

    print(costs)




def part2():
    print('Part 2')

    TEST = False

    MINROW, MINCOL = 0, 0

    if TEST:
        maze = readTheFile('Resources/day16ResourceTraining.txt')
    else:
        maze = readTheFile('Resources/day16Resource.txt')

    MAXROW = len(maze)
    MAXCOL = len(maze[0])



    start = find_pos('S', maze)
    end = find_pos('E', maze)

    all_paths = dijkstraAllPossWays(start, end, maze, MAXROW, MAXCOL, (0, 1))

    allPoints = set()


    for path in all_paths:
        for point in path.visited:
            allPoints.add(point)

    print(len(allPoints))



if __name__ == '__main__':
    print('day 16')
    #part1()
    part2()