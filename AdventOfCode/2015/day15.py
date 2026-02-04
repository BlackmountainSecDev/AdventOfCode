



def readTheFile(filename):
    try:
        with open(filename, 'r') as lines:
            return lines.read().split('\n')

    except FileNotFoundError:
        return []


def generate_all_combinations():
    """Generiert alle Kombinationen von 4 Werten, die zusammen max. 100 ergeben"""
    combinations = []

    for a in range(101):  # 0 bis 100
        for b in range(101 - a):  # 0 bis (100-a)
            for c in range(101 - a - b):  # 0 bis (100-a-b)
                d = 100 - a - b - c  # Rest (kann auch 0 sein)
                combinations.append([a, b, c, d])

    return combinations

def part1and2():

    test = False

    if test:
        content = readTheFile('Resources/day15Training.txt')
    else:
        content = readTheFile('Resources/day15.txt')

    ingredients = {}
    for line in content:
        name, rest = line.split(':')
        ingredients[name] = {}
        print(name)
        ingAndVals = rest.split(',')
        for ingAndVal in ingAndVals:
            ing, val = ingAndVal.strip().split(' ')
            ingredients[name][ing] = int(val)


    combos = generate_all_combinations()
    wholeSum = 0
    for currentCombo in combos:
        capacities = 0
        durabilities = 0
        flavores = 0
        textures = 0
        calories = 0

        counter = 0

        for currentKey in ingredients.keys():
            capacities += ingredients[currentKey]['capacity'] * currentCombo[counter]
            durabilities += ingredients[currentKey]['durability'] * currentCombo[counter]
            flavores += ingredients[currentKey]['flavor'] * currentCombo[counter]
            textures += ingredients[currentKey]['texture'] * currentCombo[counter]
            calories += ingredients[currentKey]['calories'] * currentCombo[counter] #Part 2
            counter += 1


        if capacities > 0 and durabilities > 0 and flavores > 0 and textures > 0 and calories == 500: #part 2 is starting with the and
            res = capacities * durabilities * flavores * textures
            if res > wholeSum:
                wholeSum = res



    #print(ingredients)

    #
    #print(f"Anzahl Kombinationen: {len(combos)}")
    print(wholeSum)

if __name__ == '__main__':
    part1and2()