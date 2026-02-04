def readfile(filename):
    with open(filename, 'r') as datei:
        localContent = datei.read()
        localContent = localContent.split('\n')

        allSues = {}

        for line in localContent:
            all = line.split(',')
            name, firstValName, firsVal = all[0].split(':')
            allSues[name] = {firstValName.strip():int(firsVal)}
            theLen = len(all)
            for counter in range(1, theLen):
                valName, val = all[counter].split(':')
                allSues[name][valName.strip()] = int(val)

    return allSues





def part1():

    allAunts = readfile('Resources/day16.txt')


    targetAunt = {
            'children': 3,
            'cats': 7,
            'samoyeds': 2,
            'pomeranians': 3,
            'akitas': 0,
            'vizslas': 0,
            'goldfish': 5,
            'trees': 3,
            'cars': 2,
            'perfumes': 1
    }

    possibleAunt = []
    for key in allAunts:
        same = True
        for attributeKey in targetAunt:
            if attributeKey in allAunts[key]:
                if targetAunt[attributeKey] != allAunts[key][attributeKey]:
                    same = False
                    break


        if same:
            possibleAunt.append(key)

    print(possibleAunt)



def part2():

    allAunts = readfile('Resources/day16.txt')

    targetAunt = {
            'children': 3,
            'cats': 7,
            'samoyeds': 2,
            'pomeranians': 3,
            'akitas': 0,
            'vizslas': 0,
            'goldfish': 5,
            'trees': 3,
            'cars': 2,
            'perfumes': 1
    }

    possibleAunt = []
    for key in allAunts:
        same = True
        for attributeKey in targetAunt:

            if attributeKey in allAunts[key]:
                if attributeKey == 'cats' or attributeKey == 'trees':
                    if targetAunt[attributeKey] > allAunts[key][attributeKey]:
                        same = False
                        break

                elif attributeKey == 'pomeranians' or attributeKey == 'goldfish':
                    if targetAunt[attributeKey] < allAunts[key][attributeKey]:
                        same = False
                        break
                else:
                    if targetAunt[attributeKey] != allAunts[key][attributeKey]:
                        same = False
                        break


        if same:
            possibleAunt.append(key)

    print(possibleAunt)

if __name__ == '__main__':
    part1()
    part2()