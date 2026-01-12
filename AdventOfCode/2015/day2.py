



def readTheFile(filename):
    with open(filename, 'r') as lines:
        content = [a.replace('\n','') for a in lines.readlines()]
        content = [list(map(int, a.split('x'))) for a in content]

        return content




def part1():
    content = readTheFile('Resources/day2.txt')
    print(content)

    wholeSqureFeet = 0
    for l,w,h in content:
        wholeSqureFeet += 2 * l * w + 2 * w * h + 2 * h * l + min([l * w, w * h, h * l])

    print(wholeSqureFeet)


def part2():
    content = readTheFile('Resources/day2.txt')
    print(content)

    wholeSqureFeet = 0
    for entry in content:
        a,b,c = sorted(entry)
        wholeSqureFeet += 2*a + 2*b + a*b*c



    print(wholeSqureFeet)

if __name__ == '__main__':
    #part1()
    part2()




