import re 



def readTheFile(filename):
    with open(filename, 'r') as lines:
        return lines.read().split('\n')


def part1():
    test = False

    if test:
        content = readTheFile('Resources/day5Training.txt')
    else:
        content = readTheFile('Resources/day5.txt')


    patternDoubleletter = r'(.)\1'
    vowels = "[aeiou]"

    counter = 0
    for text in content:
        if re.search(patternDoubleletter, text):
            if len(re.findall(vowels, text)) >= 3:
                if 'ab' not in text and'cd' not in text and 'pq' not in text and 'xy' not in text:
                    #print(text)
                    counter += 1

    print(counter)


def part2():
    test = False

    if test:
        content = readTheFile('Resources/day5Training.txt')
    else:
        content = readTheFile('Resources/day5.txt')

    counter = 0
    for text in content:
        rule1 = bool(re.search(r'(..).*\1', text))  # I hate regex, supported by claude ai
        rule2 = bool(re.search(r'(.).\1', text))    # I hate regex, supported by claude ai

        if rule1 and rule2:
            counter += 1

    print(counter)

if __name__ == '__main__':
    part1()
    part2()