import json


def readTheFile(filename):

    try:
        with open(filename, 'r') as lines:
            return lines.read()

    except FileNotFoundError:
        return []

def readTheJsonFile(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def extractNumbers(obj, numbers=None):
    if numbers is None:
        numbers = []

    if isinstance(obj, (int, float)):
        numbers.append(obj)
    elif isinstance(obj, dict):
        for value in obj.values():
            extractNumbers(value, numbers)
    elif isinstance(obj, list):
        for item in obj:
            extractNumbers(item, numbers)

    return numbers


def extractNumbersExceptRed(obj, numbers=None):
    if numbers is None:
        numbers = []

    if isinstance(obj, (int, float)):
        numbers.append(obj)
    elif isinstance(obj, dict):
        if 'red' not in obj.values():
            for value in obj.values():
                extractNumbersExceptRed(value, numbers)
    elif isinstance(obj, list):
        for item in obj:
            extractNumbersExceptRed(item, numbers)

    return numbers


def part1():
    print('Part 1')

    jsonObj = readTheJsonFile('Resources/day12.json')

    numbers = extractNumbers(jsonObj)

    print(sum(numbers))


def part2():
    print('Part 2')

    jsonObj = readTheJsonFile('Resources/day12.json')

    numbers = extractNumbersExceptRed(jsonObj)

    print(sum(numbers))


if __name__ == '__main__':
    part1()
    part2()