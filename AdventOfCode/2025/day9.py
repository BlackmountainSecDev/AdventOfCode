import numpy as np
import matplotlib.pyplot as plt


def readTheFile(fileName):
    try:
        with open(fileName) as file:
            return [[int(x) for x in line.split(',')] for line in file.read().split('\n')]

    except IOError:
        print('File not found')



def part1():

    print('Part 1')
    test = False

    if test:
        content = readTheFile('Resources/day9Training.txt')
    else:
        content = readTheFile('Resources/day9.txt')

    allDiffs = []
    if content:
        print(content)
        for firstElemPos in range(0, len(content)):
            for secondElemPos in range(firstElemPos+1, len(content)):
                fx, fy = content[firstElemPos]
                sx, sy = content[secondElemPos]
                x = abs(fx - sx) + 1
                y = abs(fy - sy) + 1
                allDiffs.append([firstElemPos, secondElemPos, x*y])

    #print(allDiffs)

    allDiffs = sorted(allDiffs, key=lambda x: x[2], reverse=True)
    print(allDiffs[0])


def findOppositeAndCountSizeOfArea(currentElem, lookupTableByX, lookupTableByY):
    x, y = currentElem

    neigbhourC = -1
    #find neigbhour in same column
    for val in lookupTableByX[x]:
        if val != currentElem and val[1] > y:
            neigbhourC = val

    if neigbhourC != -1:
        #find from the neighour, the neigbhour in same row
        nx, ny = neigbhourC
        neigbhourR = -1
        for val in lookupTableByY[ny]:
            if val != neigbhourC and val[0] > x:
                neigbhourR = val


        if neigbhourR != -1:
            fx, fy = currentElem
            sx, sy = neigbhourR
            x = abs(fx - sx) + 1
            y = abs(fy - sy) + 1
            return [currentElem, neigbhourR, x*y]



    return -1


def part2():

    print('Part 2')
    test = False

    if test:
        content = readTheFile('Resources/day9Training.txt')
    else:
        content = readTheFile('Resources/day9.txt')

    minYPos = min(content, key=lambda x: (x[1]))
    maxYPos = max(content, key=lambda x: (x[1]))
    minXPos = min(content, key=lambda x: (x[0]))
    maxXPos = max(content, key=lambda x: (x[0]))

    #content = sorted(content, key=lambda x: (x[1],  x[0]))

    lookupTableByX = {}
    lookupTableByY = {}

    for pair in content:
        #for x,y in pair:
            #x, y = pair
        if pair[0] not in lookupTableByX:
            lookupTableByX[pair[0]] = []
        lookupTableByX[pair[0]].append(pair)

        if pair[1] not in lookupTableByY:
            lookupTableByY[pair[1]] = []
        lookupTableByY[pair[1]].append(pair)

            #if pair not in lookupTableByY:
            #    lookupTableByY[pair] =
    
    print(minYPos)
    print(maxYPos)
    print(minXPos)
    print(maxXPos)

    fx, fy = minYPos
    sx, sy = maxYPos
    x = abs(fx - sx) + 1
    y = abs(fy - sy) + 1
    print(f'{minYPos} {maxYPos} {x*y}')
    fx, fy = minXPos
    sx, sy = maxXPos
    x = abs(fx - sx) + 1
    y = abs(fy - sy) + 1
    print(f'{minYPos} {maxYPos} {x * y}')

    print(content)
    
    # 1. Daten in X- und Y-Koordinaten aufteilen
    X = [point[0] for point in content]
    Y = [point[1] for point in content]

    # 2. Ein Matplotlib-Plot erstellen
    plt.figure(figsize=(10, 8))  # Größe des Plots einstellen

    ## --- 2A: Die Punkte als Linienzug darstellen ---
    # Dies ist relevant, da der Input eine geschlossene Begrenzung/ein Polygon darstellt
    plt.plot(X, Y,
             linestyle='-',  # Linien zwischen den Punkten zeichnen
             color='blue',  # Farbe der Linie
             linewidth=1.5,  # Dicke der Linie
             label='Polygonzug')

    # Den letzten Punkt mit dem ersten Punkt verbinden (um das Polygon zu schließen)
    # Hierfür hängen wir den ersten Punkt an das Ende der Listen an.
    plt.plot([X[-1], X[0]], [Y[-1], Y[0]],
             linestyle='-',
             color='blue',
             linewidth=1.5)

    ## --- 2B: Die einzelnen Punkte als Scatter Plot darstellen ---
    plt.scatter(X, Y,
                color='red',  # Farbe der Punkte
                marker='o',  # Form der Punkte (Kreis)
                s=10,  # Größe der Punkte
                label='Eckpunkte')

    # 3. Das Plot-Layout anpassen
    plt.title('Visualisierung des Polygonumrisses')
    plt.xlabel('X-Koordinate')
    # Da Y in deinem Datensatz sehr groß wird, kehren wir die Achse um,
    # wenn die Punkte von einer "oben-nach-unten"-Darstellung stammen (häufig bei Bilddaten oder Koordinaten in bestimmten Kontexten).
    # Wenn das Polygon die "normale" geografische Darstellung (unten=klein) abbilden soll, kannst du diese Zeile entfernen.
    # plt.gca().invert_yaxis()

    # 4. Seitenverhältnis festlegen
    # Dies ist SEHR wichtig, damit der Umriss nicht verzerrt aussieht (1 Einheit X = 1 Einheit Y).
    plt.axis('equal')

    # 5. Legende und Gitter anzeigen
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    # 6. Plot anzeigen
    plt.show()

    allDiffs = []
    for firstElemPos in range(0, len(content)-2, 2): # only look rowwise
        #x, y = firstElemPos
        #print(content[firstElemPos])
        retVal = findOppositeAndCountSizeOfArea(content[firstElemPos], lookupTableByX, lookupTableByY)
        if retVal != -1:
            allDiffs.append(retVal)

    allDiffs = sorted(allDiffs, key=lambda x: x[2], reverse=True)
    print(allDiffs)


if __name__ == '__main__':
    #part1()
    part2()














