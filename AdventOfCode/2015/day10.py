



def part1():
    print("2015 Day 10 Part 1")
    currentvalue = '3113322113'

    newValue = ''
    for x in range(40):
        index = 0
        maxlen = len(currentvalue)
        newValue = ''
        while index < maxlen:

            searchVal = currentvalue[index]

            nextIndex = index + 1
            theLen = 1
            while nextIndex < maxlen:
                if currentvalue[nextIndex] == searchVal:
                    nextIndex += 1
                    theLen += 1
                else:
                    break

            newValue += str(theLen)+searchVal
            index += 1
            if index < nextIndex:
                index = nextIndex

        currentvalue = newValue

    print(len(currentvalue))


def part2():
    print("2015 Day 10 Part 2")
    currentvalue = '3113322113'

    newValue = ''
    for x in range(50):
        index = 0
        maxlen = len(currentvalue)
        newValue = ''
        while index < maxlen:

            searchVal = currentvalue[index]

            nextIndex = index + 1
            theLen = 1
            while nextIndex < maxlen:
                if currentvalue[nextIndex] == searchVal:
                    nextIndex += 1
                    theLen += 1
                else:
                    break

            newValue += str(theLen)+searchVal
            index += 1
            if index < nextIndex:
                index = nextIndex

        currentvalue = newValue

    print(len(currentvalue))

if __name__ == "__main__":
    part1()
    part2()