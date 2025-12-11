import math


def readTheFile(filename):
    with open(filename, 'r') as file:
        lines = file.read()
        return [[int(x) for x in line.split(',')] for line in lines.split('\n')]


def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 +
                     (point1[1] - point2[1])**2 +
                     (point1[2] - point2[2])**2)


def solve_mst_problem(allDistances, max_connections):
    N = len(allDistances[0])  # Anzahl der Verteilerkästen (z.B. 20)

    # 1. INITIALISIERUNG DER DSU-STRUKTUR
    # parent[i] speichert den Repräsentanten (Wurzel) des Schaltkreises von Kasten i.
    parent = list(range(N))
    # size[i] speichert die Größe des Schaltkreises, ABER NUR AM INDEX DES REPRÄSENTANTEN!
    size = [1] * N

    def find(i):
        # FIND-Operation mit Pfadkomprimierung (macht die Struktur schnell)
        if parent[i] == i:
            return i
        parent[i] = find(parent[i])  # Aktualisiere den parent direkt zur Wurzel
        return parent[i]

    def union(i, j):
        # UNION-Operation mit Vereinigung nach Rang/Größe
        root_i = find(i)
        root_j = find(j)

        if root_i != root_j:
            # Verschiebe den kleineren Baum unter den größeren (für Optimierung)
            if size[root_i] < size[root_j]:
                root_i, root_j = root_j, root_i  # Tausche, sodass root_i immer der größere ist

            parent[root_j] = root_i  # root_i wird der neue Repräsentant
            size[root_i] += size[root_j]  # Größe des neuen Schaltkreises aktualisieren

            return True  # Union erfolgreich durchgeführt

        return False  # Union NICHT durchgeführt (sie waren bereits verbunden)

    # 2. VERARBEITUNG DER SORTIERTEN KANTEN
    # Wir nehmen an, allDistances ist bereits nach Entfernung sortiert: [[a, b, dist], ...]
    connections_made = 0

    for a, b, distance in allDistances:
        # Prüfe, ob A und B zu unterschiedlichen Schaltkreisen gehören, und verbinde sie
        if union(a, b):
            connections_made += 1
            if connections_made == max_connections:
                break

    # 3. ERGEBNIS BERECHNEN
    # Hier müssten Sie alle Werte im Size-Array filtern, die zu einem Repräsentanten gehören,
    # die größten drei finden und multiplizieren.

    circuit_sizes = []
    for i in range(N):
        if parent[i] == i:  # Nur die Größe des Repräsentanten ist relevant
            circuit_sizes.append(size[i])

    # Sortiere die Größen absteigend und wähle die größten drei
    circuit_sizes.sort(reverse=True)

    # Ergebnis = Größe_1 * Größe_2 * Größe_3
    result = circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]
    return result


# Beispielaufruf (N=20, 1000 Verbindungen):
# solve_mst_problem(sortierte_kantenliste, 1000)


def checkCircuits(currentIndex, allCircuits):

    for theIndex, currentCircuit in enumerate(allCircuits):
        if currentIndex in currentCircuit:
            return theIndex

    return -1


def part1():
    print('Part 1')

    test = False

    if test:
        coordinates = readTheFile('Resources/day8Training.txt')
    else:
        coordinates = readTheFile('Resources/day8.txt')

    allDistances = []
    for indexFirstCor in range(0, len(coordinates)):
        for indexSecondCor in range(indexFirstCor+1, len(coordinates)):
            eucDistance = euclideanDistance(coordinates[indexFirstCor], coordinates[indexSecondCor])

            #print(f'{coordinates[indexFirstCor]} {coordinates[indexSecondCor]} = {eucDistance}')

            allDistances.append([indexFirstCor, indexSecondCor, eucDistance])


    allDistances = sorted(allDistances, key=lambda x: x[2])


    allCircuits = []

    if test:
        endRange = 10
    else:
        endRange = 1000

    for currentDistance in range(0, endRange):

        a, b, distance = allDistances[currentDistance]
        retA = checkCircuits(a, allCircuits)
        retB = checkCircuits(b, allCircuits)

        if retA == -1 and retB == -1:
            newSet = set()
            newSet.add(a)
            newSet.add(b)
            allCircuits.append(newSet)
        elif retA == retB:
            #do nothing
            continue

        elif retA != -1 and retB != -1:
            #union

            # Wähle die Indizes, die gelöscht werden sollen
            idx_to_remove_low = min(retA, retB)
            idx_to_remove_high = max(retA, retB)

            # Hole die Sets VOR dem Löschen
            groupA = allCircuits[idx_to_remove_low]
            groupB = allCircuits[idx_to_remove_high]

            # 1. Lösche das Set mit dem HÖHEREN Index
            allCircuits.pop(idx_to_remove_high)

            # 2. Lösche das Set mit dem NIEDRIGEREN Index
            allCircuits.pop(idx_to_remove_low)

            # 3. Füge das vereinigte Set hinzu
            newGroup = groupA.union(groupB)
            allCircuits.append(newGroup)
        elif retA != -1 and retB == -1:
            allCircuits[retA].add(b)
        else:
            allCircuits[retB].add(a)

    #print(len(allCircuits))
    #print(allCircuits)

    allCircuits = sorted(allCircuits, key=lambda x: len(x), reverse=True)

    print(len(allCircuits[0])*len(allCircuits[1])*len(allCircuits[2]))



def part2():
    print('Part 2')

    test = False

    if test:
        coordinates = readTheFile('Resources/day8Training.txt')
    else:
        coordinates = readTheFile('Resources/day8.txt')

    allDistances = []
    for indexFirstCor in range(0, len(coordinates)):
        for indexSecondCor in range(indexFirstCor+1, len(coordinates)):
            eucDistance = euclideanDistance(coordinates[indexFirstCor], coordinates[indexSecondCor])

            #print(f'{coordinates[indexFirstCor]} {coordinates[indexSecondCor]} = {eucDistance}')

            allDistances.append([indexFirstCor, indexSecondCor, eucDistance])


    allDistances = sorted(allDistances, key=lambda x: x[2])


    allCircuits = []


    for currentDistance in range(0, len(allDistances)):

        a, b, distance = allDistances[currentDistance]
        retA = checkCircuits(a, allCircuits)
        retB = checkCircuits(b, allCircuits)

        if retA == -1 and retB == -1:
            newSet = set()
            newSet.add(a)
            newSet.add(b)
            allCircuits.append(newSet)
        elif retA == retB:
            #do nothing
            continue

        elif retA != -1 and retB != -1:
            #union

            # Wähle die Indizes, die gelöscht werden sollen
            idx_to_remove_low = min(retA, retB)
            idx_to_remove_high = max(retA, retB)

            # Hole die Sets VOR dem Löschen
            groupA = allCircuits[idx_to_remove_low]
            groupB = allCircuits[idx_to_remove_high]

            # 1. Lösche das Set mit dem HÖHEREN Index
            allCircuits.pop(idx_to_remove_high)

            # 2. Lösche das Set mit dem NIEDRIGEREN Index
            allCircuits.pop(idx_to_remove_low)

            # 3. Füge das vereinigte Set hinzu
            newGroup = groupA.union(groupB)
            allCircuits.append(newGroup)
        elif retA != -1 and retB == -1:
            allCircuits[retA].add(b)
        else:
            allCircuits[retB].add(a)

        if len(allCircuits) == 1 and (len(allCircuits[0]) == len(coordinates)):
            #print(f'{coordinates[a]} {coordinates[b]}: {len(allCircuits)} {len(allCircuits[0])}')
            print(coordinates[a][0]*coordinates[b][0])
            break



if __name__ == '__main__':
    part1()
    print()
    part2()