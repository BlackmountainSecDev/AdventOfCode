import heapq


def readTheFile(filename):
    with open(filename, 'r') as file:
        maze_str = file.read()

    return [list(line) for line in maze_str.strip().split('\n')]


def findAllCheatingPosition(maze):
    startRow = 1
    startCol = 1
    endRow = len(maze)-1
    endCol = len(maze[0])-1
    allPossibleCheatingPositions = []
    allowedSigns = ('.', 'S', 'E')
    for currentRow in range(startRow, endRow):
        for currentCol in range(startCol, endCol):
            #check if #
            if maze[currentRow][currentCol] == '#':
                #check if left and right a dot is
                if maze[currentRow][currentCol-1] in allowedSigns and maze[currentRow][currentCol+1] in allowedSigns or maze[currentRow-1][currentCol] in allowedSigns and maze[currentRow+1][currentCol] in allowedSigns:
                    allPossibleCheatingPositions += [[currentRow, currentCol]]

    return  allPossibleCheatingPositions


# helperfunction
def neighbors(r, c, maze, rows, cols):
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] in ('.', 'E'):
            yield (nr, nc)

# Dijkstra-Algorithm
def dijkstra(start, end, maze, rows, cols):
    heap = [(0, start)]
    visited = set()
    dist = {start: 0}
    prev = {}

    while heap:
        current_dist, current = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)

        if current == end:
            break

        for neighbor in neighbors(*current, maze, rows, cols):
            if neighbor in visited:
                continue
            tentative_dist = current_dist + 1
            if tentative_dist < dist.get(neighbor, float('inf')):
                dist[neighbor] = tentative_dist
                prev[neighbor] = current
                heapq.heappush(heap, (tentative_dist, neighbor))

    # Pfad rekonstruieren
    path = []
    node = end
    while node != start:
        path.append(node)
        node = prev.get(node)
        if node is None:
            return []  # kein Pfad gefunden
    path.append(start)
    path.reverse()
    return path


def part1():
    maze = readTheFile('Resources/day20Resource.txt')
    #maze = readTheFile('Resources/day20ResourceTraining.txt')

    # Umwandeln in 2D-Liste
    #maze = [list(line) for line in maze_str.strip().split('\n')]
    rows, cols = len(maze), len(maze[0])

    # Position von Start (S) und Ziel (E) finden
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)

    allPossibleCheatingPositions = findAllCheatingPosition(maze)
    #finde alle zwischenMauern
    findAllCheatingPosition(maze)


    # Pfad
    path = dijkstra(start, end, maze, rows, cols)
    regularCost = len(path) - 1


    allCosts  = []
    for possbileCheatingPos in allPossibleCheatingPositions:
        maze[possbileCheatingPos[0]][possbileCheatingPos[1]]='.'
        path = dijkstra(start, end, maze, rows, cols)
        cost = len(path)-1
        maze[possbileCheatingPos[0]][possbileCheatingPos[1]] = '#'
        allCosts.append(regularCost-cost)




    # Ausgabe mit Pfad markiert
    for r, c in path:
        if maze[r][c] == '.':
            maze[r][c] = '*'

    # Karte anzeigen
    #for row in maze:
    #    print(''.join(row))
    '''
    for row in range(len(maze)):
        colored_row = ''
        for ch in range(len(maze[0])):
            if[row,ch] in allPossibleCheatingPositions:
            #if ch == '*':
                colored_row += '\033[91m#\033[0m'  # rot
            else:
                colored_row += maze[row][ch]
        print(colored_row)
    '''
    print(f'Regular Cost: {regularCost}')
    print(len(allCosts))
    print(sorted(allCosts))

    higherAndEqual100 = [x for x in allCosts if x >= 100]
    print(higherAndEqual100)
    print(len(higherAndEqual100))

if __name__ == '__main__':
    part1()