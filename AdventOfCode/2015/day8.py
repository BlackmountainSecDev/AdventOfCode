

def readTheFile(filename):
    with open(filename, 'r') as lines:
        return lines.read().split('\n')


def part1():
    test = True

    if test:
        content = readTheFile('Resources/day8Training.txt')
    else:
        content = readTheFile('Resources/day8.txt')

    #print(content)

    allWholeLenghts = []
    allRealLenghts = []
    for line in content:
        allWholeLenghts.append(len(line))
        #print(f'{line} len: {len(line)}')

        index = 0
        line = line[1:-1]

        maxLen = len(line)
        characterCounter = 0
        while index < maxLen:

            if line[index] == '\\':
                if line[index+1] == 'x':
                    index += 3
                else:
                    index += 1


            characterCounter += 1
            index += 1

        allRealLenghts.append(characterCounter)

    print(f'allWholeLenghts: {allWholeLenghts} {sum(allWholeLenghts)}')
    print(f'allRealLenghts: {allRealLenghts} {sum(allRealLenghts)}')
    #print(allRealLenghts)
    print(sum(allWholeLenghts)-sum(allRealLenghts))



def part2():
    test = False

    if test:
        content = readTheFile('Resources/day8Training.txt')
    else:
        content = readTheFile('Resources/day8.txt')

    #print(content)

    allWholeLenghts = []
    allRealLenghts = []
    for line in content:
        allWholeLenghts.append(len(line)+4) # adding \" at start and end
        allRealLenghts.append(len(line))
        #print(f'{line} len: {len(line)}')

        index = 0
        line = line[1:-1]

        maxLen = len(line)
        characterCounter = 0
        while index < maxLen:

            if line[index] == '\\':
                if line[index+1] == 'x':
                    index += 3
                    characterCounter += 1

                else:
                    index += 1
                    characterCounter += 2


            #characterCounter += 1
            index += 1

        allWholeLenghts[-1] += characterCounter
        #allRealLenghts.append(characterCounter)

    print(f'allWholeLenghts: {allWholeLenghts} {sum(allWholeLenghts)}')
    print(f'allRealLenghts: {allRealLenghts} {sum(allRealLenghts)}')
    #print(allRealLenghts)
    print(sum(allWholeLenghts)-sum(allRealLenghts))


if __name__ == '__main__':
    #part1()
    part2()