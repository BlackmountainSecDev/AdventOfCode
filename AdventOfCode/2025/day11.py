def readTheFile(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.read().split('\n')

            return {key: val.split() for key, val in [line.split(':') for line in lines]}
    except IOError:
        print('File not found')



def dfs(graph, currentNode, targetNode, currentPath, allPath):
    if currentNode not in currentPath:
        currentPath.append(currentNode)
        if currentNode != targetNode:
            for neighbour in graph[currentNode]:
                dfs(graph, neighbour, targetNode, currentPath.copy(), allPath)

        else:
            allPath.append(currentPath)


def dfsPart2(graph, currentNode, targetNode, currentPath, allPath):
    if currentNode not in currentPath:
        currentPath.append(currentNode)
        if currentNode != targetNode:
            if currentNode in graph.keys():
                for neighbour in graph[currentNode]:
                    dfsPart2(graph, neighbour, targetNode, currentPath.copy(), allPath)
        else:
           allPath.append(currentPath)


memo = {}
def countPaths(graph, start, end):
    # Eindeutiger Key für den Cache
    state = (start, end)
    if state in memo:
        return memo[state]

    if start == end:
        return 1
    if start not in graph:
        return 0

    total = 0
    for neighbor in graph[start]:
        total += countPaths(graph, neighbor, end)

    memo[state] = total
    return total

def part1():
    print('Part 1')

    test = False

    if test:
        graph = readTheFile('Resources/day11Training.txt')
    else:
        graph = readTheFile('Resources/day11.txt')

    if graph:
        #print(graph)

        currentPath = []  # List to keep track of visited nodes.
        allPaths = []

        # Driver Code
        dfs(graph, 'you', 'out', currentPath, allPaths)
        print(allPaths)
        print(len(allPaths))


def part2():
    print('Part 2')

    test = False

    if test:
        graph = readTheFile('Resources/day11Training2.txt')
    else:
        graph = readTheFile('Resources/day11.txt')

    if graph:
        memo.clear()  # Cache leeren

        # Variante 1: svr -> dac -> fft -> out
        p1 = countPaths(graph, 'svr', 'dac')
        p2 = countPaths(graph, 'dac', 'fft')
        p3 = countPaths(graph, 'fft', 'out')
        route1 = p1 * p2 * p3

        # Variante 2: svr -> fft -> dac -> out
        p4 = countPaths(graph, 'svr', 'fft')
        p5 = countPaths(graph, 'fft', 'dac')
        p6 = countPaths(graph, 'dac', 'out')
        route2 = p4 * p5 * p6

        # Die Gesamtzahl ist die Summe beider Möglichkeiten
        # (Da es ein gerichteter Graph ohne Zyklen ist, gibt es keine Überlappungen)
        print(f"Pfade über dac dann fft: {route1}")
        print(f"Pfade über fft dann dac: {route2}")
        print(f"Gesamtergebnis Part 2: {route1 + route2}")


if __name__ == '__main__':
    #part1()
    part2()