import time




def readTheFile2():
    data = open("Resources/day8Resource.txt", "r").read().splitlines()
    positions = [
        (ch, x, y)
        for y, line in enumerate(data)
        for x, ch in enumerate(line)
        if ch != '.'
    ]
    return positions


def readTheFile(dateiname):
    """
    Liest eine Textdatei zeilenweise und speichert die Zeilen- und Spaltenpositionen
    aller Zeichen, die nicht '.' sind.

    :param dateiname: Der Name der zu lesenden Datei.
    :return: Eine Liste von Tupeln: [(zeichen, zeile, spalte), ...].
    """
    #positionen = []
    positionen = {}

    # Der Context Manager stellt sicher, dass die Datei automatisch geschlossen wird
    with open(dateiname, 'r') as datei:
        for zeilen_index, zeile in enumerate(datei):
            # Zeilenumbruch entfernen, aber *nicht* andere Leerzeichen wie bei rstrip()
            # Der Zeilenumbruch würde die Spaltenpositionen verfälschen
            zeile = zeile.rstrip('\n\r')

            for spalten_index, zeichen in enumerate(zeile):
                if zeichen != '.':
                    if zeichen in positionen.keys():
                        positionen[zeichen].append((zeilen_index, spalten_index))
                    else:
                        positionen[zeichen] = [(zeilen_index, spalten_index)]

    return positionen, zeilen_index



def part1():

    minPos = 0
    ergebnisse, maxPos = readTheFile("Resources/day8Resource.txt")
#    ergebnisse, maxPos = readTheFile('Resources/day8ResourceTraining.txt')

    inlinePosition = set()


    for key in ergebnisse.keys():
        for currentindex in range(0, len(ergebnisse[key])-1):
            for nextIndex in range(currentindex+1, len(ergebnisse[key])):
                currentValue = ergebnisse[key][currentindex]
                nextValue = ergebnisse[key][nextIndex]

                distanceY = nextValue[0] - currentValue[0]
                distanceX = nextValue[1] - currentValue[1]

                inlineDownY = nextValue[0] + distanceY
                inlineDownX = nextValue[1] + distanceX

                inLineUpY = currentValue[0] - distanceY
                inLineUpX = currentValue[1] - distanceX

                if (minPos <= inlineDownY <= maxPos) and (minPos <= inlineDownX <= maxPos):
                    inlinePosition.add((inlineDownY, inlineDownX))

                if (minPos <= inLineUpY <= maxPos) and (minPos <= inLineUpX <= maxPos):
                    inlinePosition.add((inLineUpY, inLineUpX))

    #print(sorted(inlinePosition))
    print(len(inlinePosition))


def part2():

    minPos = 0
    ergebnisse, maxPos = readTheFile("Resources/day8Resource.txt")
#    ergebnisse, maxPos = readTheFile('Resources/day8ResourceTraining.txt')


    inlinePosition = set()


    for key, antennas in ergebnisse.items():
        for antenna in antennas:
            inlinePosition.add(antenna)


    for key in ergebnisse.keys():
        for currentindex in range(0, len(ergebnisse[key])-1):
            for nextIndex in range(currentindex+1, len(ergebnisse[key])):

                currentValue = ergebnisse[key][currentindex]
                nextValue = ergebnisse[key][nextIndex]

                distanceY = nextValue[0] - currentValue[0]
                distanceX = nextValue[1] - currentValue[1]



                inlineDownY = nextValue[0] + distanceY
                inlineDownX = nextValue[1] + distanceX

                while (minPos <= inlineDownY <= maxPos) and (minPos <= inlineDownX <= maxPos):
                    inlinePosition.add((inlineDownY, inlineDownX))

                    inlineDownY = inlineDownY + distanceY
                    inlineDownX = inlineDownX + distanceX


                inLineUpY = currentValue[0] - distanceY
                inLineUpX = currentValue[1] - distanceX

                while (minPos <= inLineUpY <= maxPos) and (minPos <= inLineUpX <= maxPos):
                    inlinePosition.add((inLineUpY, inLineUpX))

                    inLineUpY = inLineUpY - distanceY
                    inLineUpX = inLineUpX - distanceX


    #print(sorted(inlinePosition))
    print(len(inlinePosition))


if __name__ == '__main__':
    part1()
    part2()