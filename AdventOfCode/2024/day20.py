import heapq
from collections import deque
import time

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

def bfs_no_cheat(start, end, maze):
    from collections import deque
    rows, cols = len(maze), len(maze[0])
    visited = set()
    queue = deque([(start[0], start[1], 0)])  # r, c, steps

    while queue:
        r, c, steps = queue.popleft()
        if (r, c) == end:
            return steps
        if (r, c) in visited:
            continue
        visited.add((r, c))

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] in ('.', 'S', 'E'):
                queue.append((nr, nc, steps + 1))
    return float('inf')

def bfs_with_one_cheat(start, end, maze, cheat_start, cheat_end, cheat_path):
    from collections import deque
    rows, cols = len(maze), len(maze[0])
    visited = set()
    queue = deque([(start[0], start[1], False, 0)])  # r, c, used_cheat, steps

    while queue:
        r, c, used_cheat, steps = queue.popleft()
        if (r, c, used_cheat) in visited:
            continue
        visited.add((r, c, used_cheat))

        if (r, c) == end:
            return steps

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                cell = maze[nr][nc]
                if cell in ('.', 'S', 'E'):
                    queue.append((nr, nc, used_cheat, steps + 1))
                elif not used_cheat and (r, c) == cheat_start and (nr, nc) == cheat_path[0]:
                    # Begin des Cheats
                    # Cheat-Pfad vollständig durchlaufen?
                    if all(maze[x][y] == '#' for x, y in cheat_path[:-1]) and maze[cheat_path[-1][0]][cheat_path[-1][1]] in ('.', 'E'):
                        queue.append((cheat_end[0], cheat_end[1], True, steps + len(cheat_path)))
    return float('inf')

def generate_cheat_paths(maze, max_cheat_length=20):
    rows, cols = len(maze), len(maze[0])
    track_positions = [(r, c) for r in range(rows) for c in range(cols) if maze[r][c] in ('.', 'S', 'E')]
    cheat_paths = []

    for r, c in track_positions:
        stack = [((r, c), [], set(), 0)]  # pos, path, visited, steps
        while stack:
            (cr, cc), path, visited_local, steps = stack.pop()
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited_local:
                    char = maze[nr][nc]
                    new_path = path + [(nr, nc)]
                    if len(new_path) > max_cheat_length:
                        continue
                    if char == '#':
                        stack.append(((nr, nc), new_path, visited_local | {(nr, nc)}, steps + 1))
                    elif char in ('.', 'E') and new_path:
                        cheat_paths.append(((r, c), (nr, nc), new_path))
    return cheat_paths

def find_good_cheats(start, end, maze):
    normal_path_len = bfs_no_cheat(start, end, maze)
    cheat_paths = generate_cheat_paths(maze)
    better_cheats = []

    for cheat_start, cheat_end, path in cheat_paths:
        cheat_len = len(path)
        total_len = bfs_with_one_cheat(start, end, maze, cheat_start, cheat_end, path)
        if total_len < normal_path_len:
            saved = normal_path_len - total_len
            if saved >= 100:
                better_cheats.append((cheat_start, cheat_end, saved))
    return better_cheats

def bfs_with_cheat(start, end, maze, max_cheat=20):
    rows, cols = len(maze), len(maze[0])
    visited = set()
    queue = deque()
    queue.append((start[0], start[1], max_cheat, 0))  # r, c, cheat_left, steps
    paths = []

    while queue:
        r, c, cheat_left, steps = queue.popleft()

        if (r, c, cheat_left) in visited:
            continue
        visited.add((r, c, cheat_left))


        if (r, c) == end:
            paths.append(steps)

        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                char = maze[nr][nc]
                if char in ('.', 'S', 'E'):
                    queue.append((nr, nc, cheat_left, steps + 1))
                elif char == '#' and cheat_left > 0:
                    queue.append((nr, nc, cheat_left - 1, steps + 1))

    return paths


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



def part1Alt():
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

    # finde alle zwischenMauern
    allPossibleCheatingPositions = findAllCheatingPosition(maze)


    '''
    * Three possible ways to find the regular costs of a trip from S to E
    *
    '''

    '''
    * first way using dijkstra finding the way
    * makes no sens in this particular case, because all '.' are on our way 
    '''
    '''
    path = dijkstra(start, end, maze, rows, cols)
    regularCost = len(path) - 1
    '''

    '''    
    * second way just counting the '.', because all of them are on our way    
    '''
    '''
    regularCost = 0
    for row in maze:
        regularCost += row.count('.')
    regularCost += 1 #Don't forget the endpont E
    '''

    '''    
    * third way. just like the second counting the '.', but more efficient by using list comprehension 
    '''
    regularCost = sum(row.count('.') for row in maze)
    regularCost += 1 #Don't forget the endpont E


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


def part2():
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

    #allPossibleCheatingPositions = findAllCheatingPosition(maze)



    # Pfad
    #path = dijkstra(start, end, maze, rows, cols)
    path = bfs_no_cheat(start, end, maze)

    #regularCost = len(path) - 1

    allPathsSteps = find_good_cheats(start, end, maze)



    '''
    allCosts  = []
    for possbileCheatingPos in allPossibleCheatingPositions:
        maze[possbileCheatingPos[0]][possbileCheatingPos[1]]='.'
        path = dijkstra(start, end, maze, rows, cols)
        cost = len(path)-1
        maze[possbileCheatingPos[0]][possbileCheatingPos[1]] = '#'
        allCosts.append(regularCost-cost)
    '''



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
    #print(f'Regular Cost: {regularCost}')
    print(f'allPathsSteps: {allPathsSteps}')
    print(len(allPathsSteps))
    #print(sorted(allCosts))

    #higherAndEqual100 = [x for x in allCosts if x >= 100]
    #print(higherAndEqual100)
    #print(len(higherAndEqual100))

if __name__ == '__main__':
    #part1()
    part1Alt()
    #part2()