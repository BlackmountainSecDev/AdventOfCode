#from functools import reduce
from itertools import combinations
from functools import reduce
import operator
import pulp
import numpy as np

def readTheFile(filename):
    content = []
    with open(filename, 'r') as file:
        lines = file.read().split('\n')

        for line in lines:
            firstPos = line.index(']')
            lastPos  = line.index('{')
            indicatorLightDiagram = [sign for sign in line[1:firstPos]]
            buttonWiringsStr = line[firstPos+2:lastPos-1]
            buttonWirings = [
                [int(num) for num in group.replace('(', '').replace(')', '').split(',')]
                for group in buttonWiringsStr.split(' ')
            ]
            joltagesStr = line[lastPos+1:-1]
            joltages = [int(val) for val in joltagesStr.split(',')]


            content.append([indicatorLightDiagram, buttonWirings, joltages])

    return content


def xor_vec(a, b):
    return [x ^ y for x, y in zip(a, b)]

def part1():
    print('Part 1')

    test = False

    if test:
        content = readTheFile('Resources/day10Training.txt')
    else:
        content = readTheFile('Resources/day10.txt')


    allCombos = 0
    for currentLine in content:
        indicationLightTarget, buttonWirings, joltages = currentLine

        targetBin = [1 if c == '#' else 0 for c in indicationLightTarget]
        currentLen = len(targetBin)
        targetNumber = int(''.join(map(str, targetBin)), 2)


        allWirings = []
        for currentWiring in buttonWirings:
            lst = [0] * currentLen
            for pos in currentWiring:
                lst[pos] = 1

            allWirings.append(int(''.join(map(str, lst)), 2))


        shortestCombo = float('inf')
        # Länge der Kombinationen variieren: 2, 3, ... bis len(numbers)
        for r in range(1, len(allWirings) + 1):
            for combo in combinations(allWirings, r):
                # XOR aller Zahlen in der Kombination
                result = reduce(operator.xor, combo)

                if result == targetNumber:
                    if len(combo) < shortestCombo:
                        print(f"{combo} -> {result}")
                        shortestCombo = len(combo)

        allCombos += shortestCombo

    print(allCombos)


import pulp


def readTheFile(filename):
    content = []
    with open(filename, 'r') as file:
        lines = file.read().strip().split('\n')
        for line in lines:
            if not line: continue

            # Zerlege die Zeile
            firstPos = line.index(']')
            lastPos = line.index('{')

            # Button-Verkabelung extrahieren
            # Wir suchen alle Inhalte in Klammern (x,y,z)
            button_part = line[firstPos + 2:lastPos].strip()
            # Wir splitten bei ") (" und säubern die Reste
            button_groups = button_part.replace('(', '').replace(')', '').split(' ')
            buttonWirings = [[int(n) for n in g.split(',')] for g in button_groups if g]

            # Joltages extrahieren
            joltagesStr = line[lastPos + 1:-1]
            joltages = [int(val) for val in joltagesStr.split(',')]

            content.append([buttonWirings, joltages])
    return content


def solve_machine(button_wirings, target_joltages):
    num_buttons = len(button_wirings)
    num_counters = len(target_joltages)

    # Problem definieren: Wir wollen die Summe der Drücke MINIMIEREN
    prob = pulp.LpProblem("Minimize_Button_Presses", pulp.LpMinimize)

    # Variablen: x_i ist die Anzahl der Drücke für Knopf i
    # Die Anzahl muss eine ganze Zahl (Integer) und >= 0 sein
    presses = [pulp.LpVariable(f"btn_{i}", lowBound=0, cat='Integer') for i in range(num_buttons)]

    # Zielfunktion: Summe aller presses
    prob += pulp.lpSum(presses)

    # Nebenbedingungen: Für jeden Zähler muss die Summe der Drücke dem Ziel entsprechen
    for counter_idx in range(num_counters):
        # Finde alle Knöpfe, die diesen spezifischen Zähler beeinflussen
        contributing_buttons = []
        for btn_idx, wiring in enumerate(button_wirings):
            if counter_idx in wiring:
                contributing_buttons.append(presses[btn_idx])

        # Die Summe dieser Knöpfe muss exakt target_joltages[counter_idx] sein
        prob += pulp.lpSum(contributing_buttons) == target_joltages[counter_idx]

    # Lösen (ohne Konsolenausgabe)
    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    # Rückgabe der Summe der Drücke
    return int(pulp.value(prob.objective))


def part2():
    print('Part 2 - Joltage Configuration')

    test = True
    if test:
        content = readTheFile('Resources/day10Training.txt')
    else:
        content = readTheFile('Resources/day10.txt')


    total_min_presses = 0

    for button_wirings, joltages in content:
        result = solve_machine(button_wirings, joltages)
        total_min_presses += result
        print(f"Maschine benötigt {result} Drücke.")

    print(f"--- GESAMT: {total_min_presses} ---")


if __name__ == '__main__':
    #part1()
    part2()