
def datei_einlesen(dateiname):
    """Liest die Datei und teilt sie in Blöcke auf."""
    with open(dateiname, 'r') as datei:
        inhalt = datei.read()
    bloecke = inhalt.split('\n')  # Teilt den Inhalt bei doppelten Zeilenumbrüchen

    return bloecke



def part1():
    rows = datei_einlesen('Resources/day23Resource.txt')
    # rows = datei_einlesen('Resources/day23ResourceTraining.txt')

    theWholeDict = {}

    for row in rows:
        k, v = row.split('-')
        if k in theWholeDict.keys():
            theWholeDict[k].append(v)
        else:
            theWholeDict[k] = [v]

        if v in theWholeDict.keys():
            theWholeDict[v].append(k)
        else:
            theWholeDict[v] = [k]

    allkeys = sorted(theWholeDict.keys())

    wholeList = []
    tCounter = 0

    while len(allkeys) > 0:
        currentKey = allkeys[0]
        allkeys.pop(0)

        for nextIndex in range(0, len(allkeys)):
            nextKey = allkeys[nextIndex]


            if nextKey in theWholeDict[currentKey]:
                interSectList = list(set(theWholeDict[currentKey]) & set(theWholeDict[nextKey]))
                if len(interSectList) > 0:

                    for interSectVal in interSectList:

                        if currentKey in theWholeDict[interSectVal] and nextKey in theWholeDict[interSectVal]:
                            helperList = sorted([currentKey, nextKey, interSectVal])


                            if helperList not in wholeList:
                                wholeList += [helperList]

                                for val in helperList:
                                    if val.startswith('t'):
                                        tCounter += 1
                                        break


    #print(sorted(wholeList))
    #print(len(wholeList))
    print(tCounter)



if __name__ == '__main__':
    part1()