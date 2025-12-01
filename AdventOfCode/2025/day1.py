



def readTheFile(filename):
    with open(filename, 'r') as lines:
        aha = [a.replace('\n','') for a in lines.readlines()]
        return aha

LEFT = 'L'
#RIGHT = 'R'

def part1():

    test = False

    if test:
        content = readTheFile('Resources/day1Training.txt')
    else:
        content = readTheFile('Resources/day1.txt')

    currentValue = 50
    zeroCounter = 0
    for line in content:
        direction = line[:1]
        value = int(line[1:])

        value = value % 100

        if direction == LEFT:
            currentValue -= value

            '''
            endValue = currentValue - value
            print(f'{currentValue} - {value} = {endValue}')
            currentValue = endValue
            '''

            if currentValue < 0:
                currentValue += 100
                #print(f'corrected: {currentValue}')

        else:
            currentValue += value

            '''
            endValue = currentValue + value
            print(f'{currentValue} + {value} = {endValue}')
            currentValue = endValue
            '''
            
            if currentValue > 99:
                 currentValue -= 100
                 #print(f'corrected: {currentValue}')

        if currentValue == 0:
            zeroCounter += 1

    print(f'currentValue: {currentValue} ')
    print(f'amount of zeros: {zeroCounter}')




def part2():
    test = False

    if test:
        content = readTheFile('Resources/day1Training.txt')
    else:
        content = readTheFile('Resources/day1.txt')

    currentValue = 50
    zeroCounter = 0
    for line in content:
        direction = line[:1]
        value = int(line[1:])

        if value > 100:
            newValue = value % 100
            helper = value - newValue
            helper = int(helper / 100)
            zeroCounter += helper
            value = newValue


        if direction == LEFT:
            endValue = currentValue - value

            if endValue < 0:
                endValue += 100
                if endValue != 0 and currentValue != 0:
                    zeroCounter += 1


        else:
            endValue = currentValue + value

            if endValue > 99:
                endValue -= 100
                if endValue != 0 and currentValue != 0:
                    zeroCounter += 1


        currentValue = endValue

        if currentValue == 0:
            zeroCounter += 1

    print(f'currentValue: {currentValue} ')
    print(f'amount of zeros: {zeroCounter}')

if __name__ == '__main__':
    part1()
    part2()

