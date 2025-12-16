import copy


def readTheFile(filename):

    try:
        with open(filename, 'r') as file:
            lines = file.read().split('\n\n')
            shapesOfPresents = lines[:-1]
            presentHelper =  [shape.split(',')[0].split('\n') for shape in shapesOfPresents]

            allPresents = {}
            for present in presentHelper:
                presentID = int(present[0][0])
                shapeOfPresentStr = present[1:]

                shapeOfPresent = []
                sizeOfPresent = 0
                for eachLine in shapeOfPresentStr:
                    emptyLine = []
                    for sign in eachLine:
                        if sign == '#':
                            emptyLine.append(1)
                            sizeOfPresent += 1
                        else:
                            emptyLine.append(0)
                    shapeOfPresent.append(emptyLine)

                allPresents[presentID] = [sizeOfPresent, shapeOfPresent]


            regions = lines[-1].split('\n')

            allRegions = []

            for region in regions:
                size, content = region.split(':')
                w, l = map(int, size.split('x'))
                content = list(map(int, content.strip().split(' ')))
                allRegions.append([w,l, content])

            return allPresents, allRegions

    except IOError:
        print(f'Couldn\'t open the file {filename}')


def rotateShapeby90Deg(theShape):
    # Nutzt zip und reversed für eine effiziente Transponierung und Drehung
    return [list(row) for row in zip(*reversed(theShape))]


def flipShape(theShape):
    # Spiegelt die Form horizontal
    return [row[::-1] for row in theShape]


def printRowWise(content):
    for _ in content:
        print(_)


'''
def tryToFit(field, startR, startC, currentShape):

    maxWShape = len(currentShape)
    maxCShape = len(currentShape[0])

    maxRow = len(field)
    maxColum = len(field[0])


    r = startR
    for currentW in range(maxWShape):
        if r < maxRow:
            c = startC
            for currentC in range(maxCShape):
                if c < maxColum:
                    if currentShape[currentW][currentC] == 1:
                        if field[r][c] == 0:
                            field[r][c] = 1

                        else:
                            return False

                else:
                    return False

                c += 1
        else:
            return False
        r +=1

    return True
'''


def tryToFit(field, startR, startC, currentShape):
    maxWShape = len(currentShape)
    maxCShape = len(currentShape[0])

    maxRow = len(field)
    maxColum = len(field[0])

    for currentW in range(maxWShape):
        r = startR + currentW  # Berechne die Zielzeile im Feld

        # 1. Prüfen, ob die Zeile außerhalb der Grenzen liegt
        if r >= maxRow:
            return False

        for currentC in range(maxCShape):
            c = startC + currentC  # Berechne die Zielspalte im Feld

            # 2. Prüfen, ob die Spalte außerhalb der Grenzen liegt
            if c >= maxColum:
                return False

            # Nur wenn die Form an dieser Stelle ein belegtes Feld hat (1), prüfen wir die Kollision
            if currentShape[currentW][currentC] == 1:

                # 3. Prüfen, ob eine Kollision mit einer bereits belegten Zelle vorliegt
                if field[r][c] == 0:
                    field[r][c] = 1  # Passt, Zelle belegen
                else:
                    return False  # Kollision

    # Wenn die gesamte Form erfolgreich platziert wurde, return True
    return True


def doesItFit(field, shape):
    maxR = len(field)
    maxC = len(field[0])

    # Wir iterieren systematisch von unten nach oben (row) und von links nach rechts (column)
    # BLF-Strategie: Wir wollen zuerst die unterste mögliche Reihe testen, dann die nächste, usw.
    # Da Python von 0 (oben) nach N (unten) indiziert, müssen wir die Reihenfolge umkehren,
    # um die "unterste" Position zuerst zu finden.

    # 1. Iteriere von der untersten möglichen Reihe (maxR - 1) zur obersten (0)
    #    Für Tetris/Container wird oft von oben nach unten (0 nach maxR-1) iteriert,
    #    aber da BLF "Bottom" sucht, iterieren wir von unten.
    #    Wenn wir die BL-Position suchen:
    #    Die Startzeile (row) muss bis maximal maxR - Höhe des Teils gehen.

    # NEU: Wir gehen die Startpunkte von (0,0) bis (maxR-H, maxC-W) durch.
    # Die Iteration von (0,0) ist in Ordnung, wenn wir die gesamte Region testen
    # und der erste Fund (links oben) als der beste Platz *in dieser Iteration* gilt.

    # Aber da wir ein Gier-Problem lösen, sollte die erste gefundene Passform
    # links oben in einem leeren Bereich der beste Platz sein (Grid-Based-BLF).

    # Wir iterieren über ALLE möglichen Startpositionen (row, column) für die obere linke Ecke des Teils:
    max_start_row = maxR - len(shape)
    max_start_col = maxC - len(shape[0])

    for row in range(max_start_row + 1):  # +1 weil range exklusiv ist
        for column in range(max_start_col + 1):

            # --- Hier beginnt die BLF-Prüfung für die aktuelle Startposition (row, column) ---

            # 1. Testen der 0 Grad Orientierung
            fits, newField = test_all_orientations(field, shape, row, column)

            if fits:
                # Da wir von (0,0) nach rechts unten scannen, ist der erste Fund
                # die "linkeste" und "oberste" freie Position.
                # In einem gitterbasierten BLF-Ansatz ist das ausreichend,
                # solange wir alle möglichen Startpositionen testen.
                return True, newField

    return False, None


def test_all_orientations(field, shape, startR, startC):
    # 1. Orientierungen der Originalform (4 Stück)
    orientations = []

    current_shape = copy.deepcopy(shape)
    for _ in range(4):
        orientations.append(current_shape)
        current_shape = rotateShapeby90Deg(current_shape)

    # 2. Orientierungen der GESPIEGELTEN Form (4 Stück)
    flipped_shape = flipShape(shape)
    current_flipped_shape = flipped_shape
    for _ in range(4):
        # Nur hinzufügen, wenn die gespiegelte Form nicht identisch mit einer der ersten 4 ist
        if current_flipped_shape not in orientations:
            orientations.append(current_flipped_shape)
        current_flipped_shape = rotateShapeby90Deg(current_flipped_shape)

    # 3. Alle Orientierungen testen
    for current_rotated_shape in orientations:
        # Größe der Form muss in den verbleibenden Platz passen (Begrenzung prüfen)
        if startR + len(current_rotated_shape) > len(field) or \
                startC + len(current_rotated_shape[0]) > len(field[0]):
            continue  # Passt nicht vom Startpunkt aus

        # Prüfen auf Kollisionen
        if checkCollision(field, startR, startC, current_rotated_shape):
            # Wenn es passt, geben wir die belegte Version zurück
            newField = applyShape(field, startR, startC, current_rotated_shape)
            return True, newField

    return False, None

def checkCollision(field, startR, startC, currentShape):
    maxWShape = len(currentShape)
    maxCShape = len(currentShape[0])

    maxRow = len(field)
    maxColum = len(field[0])

    for currentW in range(maxWShape):
        r = startR + currentW
        if r >= maxRow:
            return False  # Außerhalb der Zeilengrenze

        for currentC in range(maxCShape):
            c = startC + currentC
            if c >= maxColum:
                return False  # Außerhalb der Spaltengrenze

            if currentShape[currentW][currentC] == 1:
                # Wenn das Teil hier einen Block hat UND das Feld bereits belegt ist (== 1)
                if field[r][c] == 1:
                    return False  # Kollision

    # Wenn wir den gesamten Shape durchgegangen sind und keine Kollision gefunden haben:
    return True


def applyShape(field, startR, startC, currentShape):
    # Diese Funktion wird NUR aufgerufen, wenn checkCollision True war.
    newField = copy.deepcopy(field)  # Kopie für die Rückgabe

    for currentW in range(len(currentShape)):
        r = startR + currentW
        for currentC in range(len(currentShape[0])):
            c = startC + currentC

            if currentShape[currentW][currentC] == 1:
                newField[r][c] = 1  # Eintragen

    return newField  # Das neue, belegte Feld zurückgeben

'''
def doesItFit(field, shape):
    # ... (Initialisierung) ...

    didntFit = True

    startR = 0
    maxR = len(field)

    startC = 0
    maxC = len(field[0])

    maxWShape = len(shape)
    maxLShape = len(shape[0])

    # get allshape forms
    allShapes = []

    for row in range(startR, maxR):
        for column in range(startC, maxC):

            if field[row][column] == 0:
                # 1. Start der 4 Orientierungen mit der Original-Form
                current_rotated_shape = copy.deepcopy(shape)  # <--- Neue Temp-Variable

                # 2. Versuch 1: 0 Grad Orientierung
                copyOfField = copy.deepcopy(field)
                fits = tryToFit(copyOfField, row, column, current_rotated_shape)

                if fits == False:
                    # 3. Versuche 2, 3, 4: Drehen der temporären Form
                    for _ in range(3):
                        current_rotated_shape = rotateShapeby90Deg(current_rotated_shape)  # <--- Nur die Temp-Variable ändern
                        copyOfField = copy.deepcopy(field)  # Muss jedes Mal kopiert werden, da tryToFit es mutiert

                        fits = tryToFit(copyOfField, row, column, current_rotated_shape)

                        if fits:
                            break

                if fits:
                    return True, copyOfField

    return False, None
'''

'''
def doesItFit(field, shape):

    didntFit = True

    startR = 0
    maxR = len(field)

    startC = 0
    maxC = len(field[0])

    maxWShape = len(shape)
    maxLShape = len(shape[0])

    #get allshape forms
    allShapes = []


    for row in range(startR, maxR):
        for column in range(startC, maxC):

            if field[row][column] == 0:
                copyOfField = copy.deepcopy(field)
                fits = tryToFit(copyOfField, row, column, shape)

                if fits == False:
                    for _ in range(3):
                        copyOfField = copy.deepcopy(field)
                        shape = rotateShape(shape)
                        fits = tryToFit(copyOfField, row, column, shape)

                        if fits:
                            break

                if fits:
                    return True, copyOfField

    return False, None
'''


# Hilfsfunktion, um die Liste der benötigten Teile zu erstellen
def get_all_presents_list(allPresents, region_content):
    presents_to_place = []
    for presentID, amount in enumerate(region_content):
        # Kopie der Shape-Daten für jedes benötigte Exemplar hinzufügen
        for _ in range(amount):
            # Speichere die Shape-Daten (presents[presentID][1])
            # und die ID (presentID), falls benötigt
            presents_to_place.append(allPresents[presentID][1])  # Nur die Shape

    # Optional, aber empfohlen: Sortieren der Liste nach absteigender Größe (FFD-Strategie)
    # Dies ist eine Heuristik, die die Suche beschleunigt
    presents_to_place.sort(key=lambda shape: sum(sum(row) for row in shape), reverse=True)

    return presents_to_place


# DFS / Backtracking Funktion
# present_list: Liste der Shapes, die noch platziert werden müssen (z.B. [Shape0, Shape2, Shape4, ...])
def solve_packing_puzzle(field, present_list):
    # BASISFALL: Wenn die Liste leer ist, haben wir alle Teile erfolgreich platziert!
    if not present_list:
        return True, field

    # Wähle das nächste Teil, das platziert werden soll (immer das erste in der sortierten Liste)
    current_shape = present_list[0]
    remaining_list = present_list[1:]

    maxR = len(field)
    maxC = len(field[0])

    # BLF-Strategie: Teste systematisch alle möglichen Startpositionen (Reihe, Spalte)
    # Beachte: Wir iterieren hier von (0,0) nach rechts unten
    # Die Iteration sollte so optimiert werden, dass man nur leere Bereiche prüft.
    # Für den Anfang testen wir alle gültigen Startpunkte:

    max_start_row = maxR - len(current_shape)
    max_start_col = maxC - len(current_shape[0])

    for row in range(max_start_row + 1):
        for column in range(max_start_col + 1):

            # --- Versuch, das Teil in allen Orientierungen an (row, column) zu platzieren ---

            # Die Funktion test_all_orientations gibt True und das NEUE Feld zurück,
            # wenn das Teil erfolgreich platziert werden konnte.
            fits_orientation, new_field = test_all_orientations(field, current_shape, row, column)

            if fits_orientation:
                # REKURSION: Versuche, den REST der Liste in das NEUE Feld zu packen
                success, final_field = solve_packing_puzzle(new_field, remaining_list)

                if success:
                    # Wenn die nachfolgende Rekursion erfolgreich ist, geben wir True zurück
                    return True, final_field

    # BACKTRACKING-FALL: Wenn alle Platzierungsversuche (alle Positionen und Orientierungen)
    # für das aktuelle Teil fehlschlagen, kehren wir zurück und versuchen eine andere
    # Entscheidungsebene höher (d.h. eine andere Platzierung für das VORHERIGE Teil).
    return False, None


def part1alt():
    print('Part 1')

    test = True

    if test:
        presents, regions = readTheFile('Resources/day12Training.txt')
    else:
        presents, regions  = readTheFile('Resources/day12.txt')

    #print(presents.values())
    #print(regions)


    '''
    counter = 0
    for region in regions:
        #wholeAvailableSpace = region[0]*region[1]

        #built the empty region
        #theField = [[0]*region[0]]*region[1] makes late problems

        theField = [[0] * region[0] for _ in range(region[1])]
        sizeOfRegion = region[0] * region[1]

        allPresentsSize = 0
        for presentID, presentAmount in enumerate(region[2]):
            if presentAmount > 0:
                #print(f'{presentID}: {presents[presentID][0]}')
                allPresentsSize += presents[presentID][0]

        #this is check is needed for the reson the size of all presents is aleady bigger than the available region
        if allPresentsSize <= sizeOfRegion:
            print('fits in general')
        else:
            print('Does not fit!')

        fits = True



        for presentID, presentAmount in enumerate(region[2]):
            if fits:
                if presentAmount > 0:
                    #print(presentID)
                    #print(presentAmount)
                    for _ in range(presentAmount):
                        fits, newField = doesItFit(theField, presents[presentID][1]) # we give a copy of the shape because we will need a couple

                        if fits == False:
                            break
                        else:
                            theField = newField
        if fits:
            print(region[2])
            counter += 1
    '''

    counter = 0
    for region in regions:
        # ... (Bereich initialisieren: theField) ...

        # 1. Erstellen der sortierten Gesamtliste der benötigten Shapes
        presents_to_place = get_all_presents_list(presents, region[2])

        # 2. Prüfung, ob die Gesamtfläche überhaupt reinpasst (wie in Ihrem Code)
        # ... (allPresentsSize <= sizeOfRegion Check) ...

        # 3. Starte die Backtracking-Suche
        fits, final_field = solve_packing_puzzle(theField, presents_to_place)

        if fits:
            print(f"Region {region[2]} PASST.")
            # Optional: printRowWise(final_field)
            counter += 1
        else:
            print(f"Region {region[2]} PASST NICHT.")

    print(f'\n{counter} Regionen passen insgesamt.')

'''
**********
* Gemini *
**********
'''

def part1():
    print('--- Teil 1: 2D Packing Problem ---')

    test = False

    if test:
        presents, regions = readTheFile('Resources/day12Training.txt')
    else:
        # Passen Sie den Pfad zu Ihrer Puzzle-Eingabe an
        presents, regions = readTheFile('Resources/day12.txt')

    if not presents or not regions:
        print("Fehler beim Laden der Daten.")
        return

    counter = 0

    for i, region in enumerate(regions):
        W, L, content = region

        # Leeres Feld initialisieren (L Zeilen, W Spalten)
        theField = [[0] * W for _ in range(L)]
        sizeOfRegion = W * L

        # Gesamte Liste der zu platzierenden Shapes erstellen und sortieren (FFD)
        presents_to_place = get_all_presents_list(presents, content)

        # Vorabprüfung der Gesamtfläche
        allPresentsSize = sum(presents[pID][0] * content[pID] for pID in range(len(content)) if pID in presents)

        print(f'\nRegion {i + 1} ({W}x{L}): {content}')

        if allPresentsSize > sizeOfRegion:
            print(f'-> Passt NICHT (Fläche: {allPresentsSize} > {sizeOfRegion}).')
            continue

            # Starte die Backtracking-Suche
        fits, final_field = solve_packing_puzzle(theField, presents_to_place)

        if fits:
            print('-> Passt! (Backtracking erfolgreich)')
            counter += 1
            # Optional: Visualisierung der Lösung
            # for row in final_field: print(''.join(map(str, row)).replace('0', '.').replace('1', '#'))
        else:
            print('-> Passt NICHT (Backtracking erfolglos)')
            # Da es sich um ein NP-schweres Problem handelt, bedeutet das Fehlschlagen der
            # FFD-Backtracking-Heuristik in der Regel, dass keine Lösung existiert.

    print(f'\n--- Endergebnis: {counter} Regionen passen insgesamt. ---')


if __name__ == '__main__':
    part1()