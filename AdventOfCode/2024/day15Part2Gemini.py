import numpy as np
import copy  # Füge dies hinzu, um die Karte bei der Rekursion/Prüfung sauber zu kopieren

# --- NEUE KONSTANTEN ---
BOX_LEFT = '['
BOX_RIGHT = ']'

# Deine Konstanten bleiben:
ROBOT = '@'
WALL = '#'
FREE = '.'


# ---

def scaleMap(originalMap):
    """ Skaliert die ursprüngliche Karte auf doppelte Breite für Part 2. """
    newMap = []
    for y, row in enumerate(originalMap):
        newRow = []
        for x, char in enumerate(row):
            if char == '#':
                newRow.extend(['#', '#'])
            elif char == 'O':
                newRow.extend([BOX_LEFT, BOX_RIGHT])  # []
            elif char == '.':
                newRow.extend(['.', '.'])  # ..
            elif char == ROBOT:
                newRow.extend([ROBOT, FREE])  # @.
            # Annahme: Original-Karte hat nur #, O, ., @
        newMap.append(newRow)
    return newMap


# Die komplexe checkAndMovePart2-Funktion
# Sie gibt zurück: (moved, newY, newX, newMap)
def checkAndMovePart2(currentY, currentX, dY, dX, paraTheMap):
    # Koordinaten des Zielfelds für den Roboter
    nextY = currentY + dY
    nextX = currentX + dX

    # 1. Prüfe, ob das Zielfeld innerhalb der Grenzen liegt
    if not (MINY <= nextY <= MAXY and MINX <= nextX <= MAXX):
        return False, currentY, currentX, paraTheMap  # Trifft auf Wand/Rand

    thePointOnMap = paraTheMap[nextY][nextX]

    # --- Fall 1: Freies Feld ---
    if thePointOnMap == FREE:
        paraTheMap[currentY][currentX] = FREE
        paraTheMap[nextY][nextX] = ROBOT
        return True, nextY, nextX, paraTheMap

    # --- Fall 2: Wand oder falsche Seite der Kiste ---
    elif thePointOnMap == WALL or thePointOnMap == BOX_RIGHT and dX > 0 or thePointOnMap == BOX_LEFT and dX < 0:
        # Roboter kann nicht gegen eine Wand, oder
        # Roboter kann nicht in eine Kiste hinein (stößt gegen BOX_RIGHT von links oder BOX_LEFT von rechts)
        return False, currentY, currentX, paraTheMap

    # --- Fall 3: Kiste schieben (BOX_LEFT oder BOX_RIGHT, von der richtigen Seite) ---
    elif thePointOnMap == BOX_LEFT or thePointOnMap == BOX_RIGHT:

        # Finde die Koordinaten des BOX_LEFT-Teils der Kiste
        if thePointOnMap == BOX_LEFT:
            boxLY, boxLX = nextY, nextX  # linke Hälfte
        else:  # thePointOnMap == BOX_RIGHT
            boxLY, boxLX = nextY, nextX - 1  # linke Hälfte ist links daneben

        boxRY, boxRX = boxLY, boxLX + 1  # rechte Hälfte

        # Koordinaten des neuen Kisten-Ziels
        newBoxLY, newBoxLX = boxLY + dY, boxLX + dX
        newBoxRY, newBoxRX = boxRY + dY, boxRX + dX

        # 3.1 Prüfe, ob die ZIEL-Koordinaten der Kiste innerhalb der Grenzen liegen
        if not (MINY <= newBoxLY <= MAXY and MINX <= newBoxLX <= MAXX and \
                MINY <= newBoxRY <= MAXY and MINX <= newBoxRX <= MAXX):
            return False, currentY, currentX, paraTheMap  # Kiste würde in Wand/Rand gedrückt

        # 3.2 Prüfe, ob die ZIEL-Felder der Kiste frei sind (oder ob es eine weitere Kiste ist)

        # Für vertikale Bewegungen (dy != 0): Nur ein Feld muss frei sein, da die Breite nicht geändert wird
        if dY != 0:
            # Für Vertikal: Beide Ziel-Felder MÜSSEN frei sein ('.')
            # Prüfe, ob das Feld unter/über der Kiste frei ist.
            targetPointL = paraTheMap[newBoxLY][newBoxLX]
            targetPointR = paraTheMap[newBoxRY][newBoxRX]

            if targetPointL == FREE and targetPointR == FREE:
                # Kiste und Roboter bewegen
                paraTheMap[newBoxLY][newBoxLX] = BOX_LEFT
                paraTheMap[newBoxRY][newBoxRX] = BOX_RIGHT

                paraTheMap[boxLY][boxLX] = FREE  # alte Kiste löschen
                paraTheMap[boxRY][boxRX] = FREE

                paraTheMap[currentY][currentX] = FREE  # alter Roboter löschen
                paraTheMap[nextY][nextX] = ROBOT  # neuen Roboter setzen

                return True, nextY, nextX, paraTheMap

        # Für horizontale Bewegungen (dx != 0):
        elif dX != 0:
            # Nur das äusserste Zielfeld muss frei sein
            if dX > 0:  # Nach Rechts
                # Prüfe nur newBoxRX
                targetPoint = paraTheMap[newBoxRY][newBoxRX]
            else:  # Nach Links
                # Prüfe nur newBoxLX
                targetPoint = paraTheMap[newBoxLY][newBoxLX]

            if targetPoint == FREE:
                # Kiste und Roboter bewegen

                # Zuerst Kiste bewegen (muss in korrekter Reihenfolge geschehen, um Überschreibungen zu vermeiden)
                if dX < 0:  # Links: starte mit [
                    paraTheMap[newBoxLY][newBoxLX] = BOX_LEFT
                    paraTheMap[newBoxRY][newBoxRX] = BOX_RIGHT
                    paraTheMap[boxRY][boxRX] = FREE  # alte Kiste löschen
                    paraTheMap[boxLY][boxLX] = FREE
                else:  # Rechts: starte mit ]
                    paraTheMap[newBoxRY][newBoxRX] = BOX_RIGHT
                    paraTheMap[newBoxLY][newBoxLX] = BOX_LEFT
                    paraTheMap[boxRY][boxRX] = FREE  # alte Kiste löschen
                    paraTheMap[boxLY][boxLX] = FREE

                # Roboter bewegen
                paraTheMap[currentY][currentX] = FREE
                paraTheMap[nextY][nextX] = ROBOT

                return True, nextY, nextX, paraTheMap

    # Wenn ein Feld nicht frei ist, oder die Kiste nicht bewegt werden kann (z.B. trifft auf Wand/andere Kiste)
    return False, currentY, currentX, paraTheMap


def part2():
    global MAXX
    global MAXY

    # Hier liest du die ursprüngliche Karte ein
    TRAIN = False
    if TRAIN:
        theMapOriginal, theDirections = readFile('Resources/day15ResourceTraining.txt')
    else:
        theMapOriginal, theDirections = readFile('Resources/day15Resource.txt')

    # Die Karte skalieren
    theMap = scaleMap(theMapOriginal)

    MAXX = len(theMap[0]) - 1
    MAXY = len(theMap) - 1

    # Finde den Roboter @ (der ist jetzt bei @.)
    currentPositionRobot = np.array([0, 0])
    for indexY, line in enumerate(theMap):
        for indexX, char in enumerate(line):
            if ROBOT == char:
                currentPositionRobot = np.array([indexY, indexX])
                break

    for direction in theDirections:
        # ... (dein Code zur Bestimmung von nextDirection bleibt gleich)
        if direction == '^':
            nextDirection = UP
        elif direction == '<':
            nextDirection = LEFT
        elif direction == '>':
            nextDirection = RIGHT
        else:
            nextDirection = DOWN

        moved, newPositionY, newPositionX, theMap = checkAndMovePart2(
            currentPositionRobot[0], currentPositionRobot[1],
            nextDirection[0], nextDirection[1], theMap
        )

        if moved:
            currentPositionRobot[0] = newPositionY
            currentPositionRobot[1] = newPositionX

    # printTheMap(theMap) # Optional zur Überprüfung

    theSum = 0
    # Berechne die GPS-Summe nur für den linken Teil der Kiste (BOX_LEFT)
    for y, line in enumerate(theMap):
        for x, char in enumerate(line):
            if char == BOX_LEFT:
                theSum += 100 * (y + 1) + (x + 1)

    print(f"Ergebnis Teil 2: {theSum}")


# Den Rest deines Original-Codes (readFile, printTheMap, globale Arrays) beibehalten

if __name__ == '__main__':
    part2()