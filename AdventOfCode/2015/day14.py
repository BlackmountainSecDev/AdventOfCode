



def readTheFile(filename):
    try:
        with open(filename, 'r') as lines:
            return lines.read().split('\n')

    except FileNotFoundError:
        return []


def part1And2():
    print('Part 1')

    allreindirs = {
        #'comet': {'v': 14, 's': 10, 'cs': 10, 'p': 127, 'cp': 127, 'r': True, 'wd': 0},
        #'dancer': {'v': 16, 's': 11, 'cs': 11, 'p': 162, 'cp': 162, 'r': True, 'wd': 0}
    }

    content = readTheFile('Resources/day14.txt')
    for line in content:
        splittedline = line.split()
        allreindirs[splittedline[0]] = {'v': int(splittedline[3]), 's': int(splittedline[6]), 'cs': int(splittedline[6]), 'p': int(splittedline[-2]), 'cp': int(splittedline[-2]), 'r': True, 'wd': 0, 'points':0}

    #print(allreindirs)


    for t in range(2503):
        leadDistance = 0
        leadingReindirs = {}
        for currentReindir in allreindirs.keys():
            if allreindirs[currentReindir]['r']:
                allreindirs[currentReindir]['wd'] += allreindirs[currentReindir]['v']
                allreindirs[currentReindir]['cs'] -= 1

                if allreindirs[currentReindir]['cs'] == 0:
                    allreindirs[currentReindir]['r'] = False
                    allreindirs[currentReindir]['cs'] = allreindirs[currentReindir]['s']

            else:
                allreindirs[currentReindir]['cp'] -= 1

                if allreindirs[currentReindir]['cp'] == 0:
                    allreindirs[currentReindir]['r'] = True
                    allreindirs[currentReindir]['cp'] = allreindirs[currentReindir]['p']

            #part 2
            if allreindirs[currentReindir]['wd']  > leadDistance:
                leadDistance = allreindirs[currentReindir]['wd']
                leadingReindirs = [currentReindir]
            elif allreindirs[currentReindir]['wd'] == leadDistance:
                leadingReindirs.append(currentReindir)

        # part 2
        for currentReindir in leadingReindirs:
            allreindirs[currentReindir]['points'] += 1

    wd_values = [reindeer['wd'] for reindeer in allreindirs.values()]
    print(max(wd_values))

    # part 2
    points = [reindeer['points'] for reindeer in allreindirs.values()]
    print(max(points))



if __name__ == '__main__':
    part1And2()