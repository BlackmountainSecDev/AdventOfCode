

def readTheFile():
    with open('Resources/day2Resource.txt', 'r') as file:
    #with open('Resources/day2ResourceTraining.txt', 'r') as file:
        lines = file.readlines()
        strlines = [line.strip() for line in lines]
        return [line.split() for line in strlines]


def part1():
    safecounter = 0
    report = readTheFile()

    #print(report)

    for line in report:
        intLine = [int(x) for x in line]

        safe = True
        increasing = 0
        for theIndex in range(0, len(intLine)-1):
            res = intLine[theIndex] - intLine[theIndex+1]
            #print(f'{intLine[theIndex]} - {intLine[theIndex+1]} = {res}')

            if res < 0:
                res *= -1
                if increasing == -1:
                    safe = False
                    break
                increasing = 1
            else:
                if increasing == 1:
                    safe = False
                    break
                increasing = -1

            if res < 1 or res > 3:
                safe = False
                break

        if safe:
            safecounter += 1
    #print('next line')

    print(f'safecounter: {safecounter}')


def safetyCheck(theLine):
    safe = True
    increasing = 0
    for theIndex in range(0, len(theLine) - 1):
        res = theLine[theIndex] - theLine[theIndex + 1]

        if res < 0:
            res *= -1
            if increasing == -1:
                return False

            increasing = 1
        else:
            if increasing == 1:
                return False

            increasing = -1

        if res < 1 or res > 3:
            return False

    return True


def part2():
    safecounter = 0
    report = readTheFile()

    #print(report)

    for line in report:
        intLine = [int(x) for x in line]

        theResult = safetyCheck(intLine)
        if theResult == False:
            for removeCounter in range(0, len(intLine)):
                copyLine = intLine.copy()
                copyLine.pop(removeCounter)
                theResult = safetyCheck(copyLine)
                if theResult == True:
                    safecounter += 1
                    break
        else:
            safecounter += 1

    print(f'safecounter: {safecounter}')



if __name__ == '__main__':
    part1()
    part2()
