


def readTheFile(filename):
    with open(filename, 'r') as lines:
        return lines.read()




def part1():
    content = readTheFile('Resources/day1.txt')

    up = content.count('(')
    down = content.count(')')
    print(0 + up - down)


def part2():
    content = readTheFile('Resources/day1.txt')

    current_floor = 0
    for i, c in enumerate(content, start = 1):  #der index startet beim zählen mit 1 aber die Positionen bleiben gleich

        if c == '(':
            current_floor += 1
        else:
            current_floor -= 1

        if current_floor < 0:
            #print(currentFloor)
            print(i)
            break

if __name__ == '__main__':
    #part1()
    part2()