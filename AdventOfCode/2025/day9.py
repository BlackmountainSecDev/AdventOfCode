from sympy import false
import matplotlib.pyplot as plt
from matplotlib.path import Path
import os


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




'''
**********
* Gemini *
**********
'''
def is_rectangle_valid(p1, p2, poly_points):
    """
    Prüft, ob das aufgespannte Rechteck zwischen p1 und p2
    vollständig innerhalb des Polygons liegt.
    """
    xmin, xmax = sorted([p1[0], p2[0]])
    ymin, ymax = sorted([p1[1], p2[1]])

    # 1. Schritt: Raycasting (Mittelpunkt-Check)
    # Ist der geometrische Mittelpunkt des Rechtecks im Polygon?
    test_x, test_y = (xmin + xmax) / 2.0, (ymin + ymax) / 2.0
    inside = False
    for i in range(len(poly_points)):
        cp1 = poly_points[i]
        cp2 = poly_points[(i + 1) % len(poly_points)]
        if ((cp1[1] > test_y) != (cp2[1] > test_y)) and \
                (test_x < (cp2[0] - cp1[0]) * (test_y - cp1[1]) / (cp2[1] - cp1[1]) + cp1[0]):
            inside = not inside

    if not inside:
        return False

    # 2. Schritt: Schnitt-Check
    # Keine Linie des Polygons darf durch das Innere des Rechtecks verlaufen.
    # Da es nur H/V Linien sind, prüfen wir auf Überschneidungen.
    for i in range(len(poly_points)):
        cp1 = poly_points[i]
        cp2 = poly_points[(i + 1) % len(poly_points)]

        pk_xmin, pk_xmax = sorted([cp1[0], cp2[0]])
        pk_ymin, pk_ymax = sorted([cp1[1], cp2[1]])

        # Horizontale Polygon-Kante
        if cp1[1] == cp2[1]:
            # Wenn die Kante auf einer Y-Höhe liegt, die im Rechteck liegt
            if ymin < cp1[1] < ymax:
                # Und die Kante sich mit dem X-Bereich des Rechtecks überschneidet
                if not (pk_xmax <= xmin or pk_xmin >= xmax):
                    return False

        # Vertikale Polygon-Kante
        else:
            # Wenn die Kante auf einer X-Position liegt, die im Rechteck liegt
            if xmin < cp1[0] < xmax:
                # Und die Kante sich mit dem Y-Bereich des Rechtecks überschneidet
                if not (pk_ymax <= ymin or pk_ymin >= ymax):
                    return False

    return True

'''
**********
* Gemini *
**********
'''
def part2():
    test = True  # Auf False setzen für die große Datei
    fileName = 'Resources/day9Training.txt' if test else 'Resources/day9.txt'

    content = readTheFile(fileName)
    if not content:
        print("Keine Daten gefunden.")
        return

    max_area = 0
    best_pair = None

    print(f"Berechne größte Fläche für {len(content)} Punkte...")

    # Alle Paare von Punkten (rote Fliesen) prüfen
    for i in range(len(content)):
        for j in range(i + 1, len(content)):
            p1 = content[i]
            p2 = content[j]


            # Rechteck-Bedingung: unterschiedliche X und Y
            if p1[0] == p2[0] or p1[1] == p2[1]:
                continue

            # Vorab-Berechnung der Fläche (+1 für Inklusivität der Fliesen)
            width = abs(p1[0] - p2[0]) + 1
            height = abs(p1[1] - p2[1]) + 1
            area = width * height

            # Nur prüfen, wenn die Fläche überhaupt größer sein könnte
            if area > max_area:
                if is_rectangle_valid(p1, p2, content):
                    max_area = area
                    best_pair = (p1, p2)

    if best_pair:
        print("\n--- ERGEBNIS ---")
        print(f"Datei: {fileName}")
        print(f"Größte Fläche: {max_area}")
        print(f"Eckpunkte: {best_pair[0]} und {best_pair[1]}")
    else:
        print("Kein gültiges Rechteck gefunden.")

if __name__ == '__main__':
    part1()
    part2()














