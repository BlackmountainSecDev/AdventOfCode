



def readTheFile(filename):
    with open(filename, 'r') as file:
        data = file.read()

        patterns, designs = data.split('\n\n')
        patterns = patterns.split(',')

        patterns = [i.strip() for i in patterns]

        designs = designs.split('\n')

    return patterns, designs


def can_build_design(design, towel_patterns_set, memo):
    if design in memo:
        return memo[design]
    if design == "":
        return True
    for pattern in towel_patterns_set:
        if design.startswith(pattern):
            if can_build_design(design[len(pattern):], towel_patterns_set, memo):
                memo[design] = True
                return True
    memo[design] = False
    return False

def count_possible_designs(patterns, designs):
    towel_patterns_set = set(patterns)
    count = 0
    for design in designs:
        if can_build_design(design, towel_patterns_set, memo={}):
            count += 1
    return count






def part1():
    #patterns, designs = readTheFile('Resources/day19ResourceTraining.txt')
    patterns, designs = readTheFile('Resources/day19Resource.txt')

    result = count_possible_designs(set(patterns), designs)
    print(f"Anzahl der möglichen Designs: {result}")


'''
********************
* geneerated by AI *
********************
'''
def count_possible_designs(available_patterns, desired_designs):#(available_patterns_str, desired_designs_str):

    possible_count = 0

    for design in desired_designs:
        print(design)
        n = len(design)
        # dp[i] ist True, wenn der Präfix von design der Länge i gebildet werden kann
        dp = [False] * (n + 1)
        dp[0] = True  # Leerer String kann immer gebildet werden

        for i in range(1, n + 1):
            for pattern in available_patterns:
                len_p = len(pattern)
                # Überprüfen, ob das aktuelle Muster an design[i-len_p : i] passt
                # und ob der vorherige Teil design[0 : i-len_p] bereits gebildet werden konnte
                if i >= len_p and dp[i - len_p] and design[i - len_p:i] == pattern:
                    dp[i] = True
                    print(pattern)
                    break  # Sobald eine Möglichkeit gefunden wurde, können wir zum nächsten i gehen

        if dp[n]:
            possible_count += 1
            print('\n')
            # Optional: Für Debugging, um zu sehen, welche Designs möglich sind
            # print(f"'{design}' ist möglich.")
        # else:
        # print(f"'{design}' ist unmöglich.")

    return possible_count


'''
********************
* geneerated by AI *
********************
'''
def count_total_arrangements(available_patterns, desired_designs):

    total_ways_sum = 0

    print("Berechne für jedes Design die Anzahl der Wege:")
    print("-------------------------------------------------")

    for design in desired_designs:
        n = len(design)
        # dp[i] wird die Anzahl der Wege speichern, wie der Präfix von design der Länge i gebildet werden kann
        dp = [0] * (n + 1)
        dp[0] = 1 # Es gibt 1 Weg, einen leeren String zu bilden (keine Handtücher)

        for i in range(1, n + 1):
            for pattern in available_patterns:
                len_p = len(pattern)
                # Überprüfen, ob das aktuelle Muster an design[i-len_p : i] passt
                # und ob der vorherige Teil design[0 : i-len_p] auf irgendeine Weise gebildet werden konnte
                if i >= len_p and design[i - len_p:i] == pattern:
                    dp[i] += dp[i - len_p] # Addiere die Wege vom vorherigen Teil

        ways_for_current_design = dp[n]
        total_ways_sum += ways_for_current_design
        print(f"'{design}': {ways_for_current_design} Wege")

    print("-------------------------------------------------")
    return total_ways_sum


def part2():
    patterns, designs = readTheFile('Resources/day19ResourceTraining.txt')
    #patterns, designs = readTheFile('Resources/day19Resource.txt')

    result = count_total_arrangements(set(patterns), designs)
    print(f"Anzahl der möglichen Designs: {result}")



if __name__ == '__main__':
    #part1()
    part2()