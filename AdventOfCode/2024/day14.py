import math


def readTheFile(fileName):
    datas = []
    try:
        with open(fileName, 'r') as file:
            for line in file:
                # Zeilenumbrüche und Leerzeichen am Anfang/Ende entfernen
                line = line.strip()
                if not line:  # Leere Zeilen überspringen
                    continue

                # Die Zeile in die Teile "p=..." und "v=..." aufteilen
                parts = line.split(' ')

                # Position (p) extrahieren
                # 'p=0,4' -> '0,4' -> ['0', '4'] -> (0.0, 4.0)
                p_str = parts[0].split('=')[1]
                px, py = map(int, p_str.split(','))

                # Vektor (v) extrahieren
                # 'v=3,-3' -> '3,-3' -> ['3', '-3'] -> (3.0, -3.0)
                v_str = parts[1].split('=')[1]
                vx, vy = map(int, v_str.split(','))

                datas.append({
                    'sp': (px, py),
                    'p': (px, py),
                    'v': (vx, vy)
                })

    except FileNotFoundError:
        print(f"Error: The file '{fileName}' wasn't found.")
    except Exception as e:
        print(f"One error happend during read: {e}")

    return datas


def part1():

    print('part 1')

    #TEST = True
    TEST = False
    MINX = 0
    MINY = 0


    if TEST:
        theFileName = "Resources/day14ResourceTraining.txt"
        #theFileName = "Resources/day14ResourceTraining2.txt"
        MAXX = 11
        MAXY = 7

    else:
        theFileName = "Resources/day14Resource.txt"
        MAXX = 101
        MAXY = 103


    datas = readTheFile(theFileName)


    for round in range(100):
        for currentData in datas:
            x, y = currentData['p']
            x += currentData['v'][0]
            y += currentData['v'][1]

            if x < MINX:
                x += MAXX
            if x >= MAXX:
                x -= MAXX
            if y < MINY:
                y += MAXY
            if y >= MAXY:
                y -= MAXY

            currentData['p'] = (x, y)


    #find the lines
    verticalLine = math.floor(MAXX/2)
    horizontalLine = math.floor(MAXY/2)



    currentPositions = [entry['p'] for entry in datas]



    upperData = [entry for entry in currentPositions if entry[1] < horizontalLine]
    bottomData = [entry for entry in currentPositions if entry[1] > horizontalLine]

    leftUpperData = [entry for entry in upperData if entry[0] < verticalLine]
    rightUpperData = [entry for entry in upperData if entry[0] > verticalLine]

    leftBottomData = [entry for entry in bottomData if entry[0] < verticalLine]
    rightBottomData = [entry for entry in bottomData if entry[0] > verticalLine]

    print(len(leftUpperData)*len(rightUpperData)*len(leftBottomData)*len(rightBottomData))



if __name__ == '__main__':
    print('day 14')
    part1()
