import heapq
from collections import defaultdict
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


def dijkstraAllPossWays_efficient(start, end, maze, rows, cols, startDir):
    # dist: speichert die minimale Distanz zum Erreichen eines Zustands (Position, Richtung)
    dist = defaultdict(lambda: float('inf'))

    # prev: speichert ALLE vorhergehenden Zustände, die den minimalen Abstand ergeben
    # prev[(r, c, dr, dc)] = {((pr, pc), (pdr, pdc)), ...}
    prev = defaultdict(set)

    # Der Heap speichert: (distance, r, c, dr, dc)
    # (dr, dc) ist die Richtung, aus der (r, c) erreicht wurde.
    pq = []

    # Initialisierung des Startzustands:
    # Da der Start (S) von außen erreicht wird (oder der erste Schritt erfolgt),
    # ist die Kosten 0. Der erste Schritt vom Start in startDir hat Kosten 1.
    # Wir modellieren den Startzustand als den Zustand, in dem wir uns befinden,
    # nachdem wir den Startknoten erreicht haben.

    # Für den Startknoten setzen wir die "Letzte_Richtung" auf startDir, damit
    # der erste Schritt die korrekten Kosten von 1 hat, wenn er in dieselbe
    # Richtung geht, oder 1001, wenn er die Richtung ändert.
    start_state = (start, startDir)
    dist[start_state] = 0
    heapq.heappush(pq, (0, *start, *startDir))  # (Distanz, r, c, dr, dc)

    min_end_dist = float('inf')

    while pq:
        d, r, c, last_dr, last_dc = heapq.heappop(pq)
        current_pos = (r, c)
        current_dir = (last_dr, last_dc)
        current_state = (current_pos, current_dir)

        # Wenn wir bereits einen besseren (oder gleichwertigen) Pfad gefunden haben, ignorieren
        if d > dist[current_state]:
            continue

        # Wenn der Endknoten erreicht wird
        if current_pos == end:
            if d < min_end_dist:
                min_end_dist = d
            # Wenn d > min_end_dist, ist dieser Pfad länger als der kürzeste bisher gefundene.
            # Da Dijkstra die Knoten in aufsteigender Reihenfolge der Distanz besucht,
            # können wir aufhören, sobald die aktuelle Distanz die minimale Distanz
            # zum Ziel überschreitet.
            if d > min_end_dist:
                break

        # Nur Nachbarn besuchen, wenn die aktuelle Distanz nicht bereits die minimale Enddistanz überschreitet
        if d <= min_end_dist:
            for neighbor_pos, neighbor_dir in neighbors(r, c, maze, rows, cols):
                nr, nc = neighbor_pos
                ndr, ndc = neighbor_dir
                neighbor_state = (neighbor_pos, neighbor_dir)


                # Kosten berechnen: 1 für gleiche Richtung, 1001 für Richtungswechsel
                if neighbor_dir == current_dir:
                    cost = 1  # Richtung beibehalten
                else:
                    cost = 1001  # Richtung gewechselt

                tentative_dist = d + cost

                if tentative_dist < dist[neighbor_state]:
                    # Neuer bester Pfad gefunden
                    dist[neighbor_state] = tentative_dist
                    prev[neighbor_state] = {current_state}
                    heapq.heappush(pq, (tentative_dist, nr, nc, ndr, ndc))
                elif tentative_dist == dist[neighbor_state]:
                    # Gleichwertiger Pfad gefunden, zum prev-Set hinzufügen
                    prev[neighbor_state].add(current_state)

    # --- Rekonstruktion aller kürzesten Wege (DFS/Rekursion) ---
    shortest_paths = []

    # Alle Endzustände mit minimaler Distanz sammeln
    final_states = []
    for (pos, direction), distance in dist.items():
        if pos == end and distance == min_end_dist:
            final_states.append((pos, direction))


    # Rekursive Funktion zur Nachverfolgung der Pfade
    def backtrack(current_state, path_positions):

        # Füge die Position des aktuellen Zustands zum Pfad hinzu
        path_positions = [current_state[0]] + path_positions

        # Basisfall: Startzustand erreicht (Distanz 0)
        if dist[current_state] == 0:
            shortest_paths.append(path_positions)
            return

        # Rekursion: Gehe zu allen vorhergehenden Zuständen
        for prev_state in prev[current_state]:
            backtrack(prev_state, path_positions)

    # Starte die Rekonstruktion von allen finalen Zuständen
    for state in final_states:
        backtrack(state, [])

    # Sammeln aller eindeutigen besuchten Punkte (aus allen kürzesten Wegen)
    all_points = set()
    for path in shortest_paths:
        for point in path:
            all_points.add(point)

    return all_points, min_end_dist


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

    # Die Startrichtung (0, 1) wurde beibehalten
    print(f'Starte Pfadsuche von S={start} nach E={end}...')
    all_points, min_dist = dijkstraAllPossWays_efficient(start, end, maze, MAXROW, MAXCOL, (0, 1))

    print(f'\n--- Ergebnis ---')
    print(f'Minimale Kosten des kürzesten Weges: {min_dist}')
    print(f'Anzahl der eindeutigen besuchten Punkte auf ALLEN kürzesten Wegen: {len(all_points)}')

    '''
    all_paths = dijkstraAllPossWays(start, end, maze, MAXROW, MAXCOL, (0, 1))

    allPoints = set()


    for path in all_paths:
        for point in path.visited:
            allPoints.add(point)

    print(len(allPoints))
    '''


if __name__ == '__main__':
    print('day 16')
    #part1()
    part2()