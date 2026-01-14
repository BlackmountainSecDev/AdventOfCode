import hashlib
import time




def part1():
    prefix = 'yzbqklnj'
    prefixEncoded = prefix.encode()

    theValue = 0 # könnte höher gesetzt werden
    run = True
    while run:
        theResult =  hashlib.md5(prefixEncoded + str(theValue).encode()).hexdigest()

        if theResult.startswith('00000'):
            run = False
        else:
            theValue +=1

    print(theResult)
    print(theValue)


def part2():
    prefix = 'yzbqklnj'
    prefixEncoded = prefix.encode()

    theValue = 0 # könnte höher gesetzt werden
    run = True
    while run:
        theResult =  hashlib.md5(prefixEncoded + str(theValue).encode()).hexdigest()

        if theResult.startswith('000000'):
            run = False
        else:
            theValue +=1

    print(theResult)
    print(theValue)

if __name__ == '__main__':

    startTime = time.time()
    part1()
    endTime = time.time()
    print(f'Elapsed: {endTime - startTime:.2f} seconds')

    startTime = time.time()
    part2()
    endTime = time.time()
    print(f'Elapsed: {endTime - startTime:.2f} seconds')