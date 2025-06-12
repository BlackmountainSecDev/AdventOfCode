

def readTheFile(filename):
    """Liest die Datei und teilt sie in Blöcke auf."""
    with open(filename, 'r') as file:
        content = file.read()
    blocks = content.split('\n\n')  # Teilt den Inhalt bei doppelten Zeilenumbrüchen

    splittedBlocks = [x.split() for x in blocks]

    return splittedBlocks


def transpose_list(liste):
    """Transponiert eine Liste von Strings (Spalten werden zu Zeilen)."""
    if not liste:
        return []

    anzahl_spalten = len(liste[0])
    neue_liste = ['' for _ in range(anzahl_spalten)]

    for zeile in liste:
        for spalte_index, zeichen in enumerate(zeile):
            neue_liste[spalte_index] += zeichen

    return neue_liste


def block_to_row(block):
    return block.splitlines()


def part1():
    bloecke = readTheFile('Resources/day25Resource.txt')
    #bloecke = readTheFile('Resources/day25ResourceTraining.txt')

    locks = []
    keys = []

    for block in bloecke:
        if block[0] == '#####' and block[-1] == '.....':
            newLock = block.copy()
            newLock.pop(-1)
            newLock.pop(0)

            newLock = transpose_list(newLock)

            lockNumbers = [aLock.count('#') for aLock in newLock]

            locks.append(lockNumbers)

        else:
            newKey = block.copy()
            newKey.pop(-1)
            newKey.pop(0)


            newKey = transpose_list(newKey)

            keyNumbers = [aKey.count('#') for aKey in newKey]

            keys.append(keyNumbers)


    amountOfFits = 0
    for lock in locks:
        for key in keys:
            fit = True
            for index in range (0, len(lock)):
                if key[index] + lock[index]  > 5:
                    fit = False
                    break

            if fit == True:
               amountOfFits += 1


    #print(locks)
    #print(keys)
    print(amountOfFits)



if __name__ == '__main__':
    part1()