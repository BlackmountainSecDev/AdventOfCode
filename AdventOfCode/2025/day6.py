import re
import numpy as np


def readTheFile(filename):
    with open(filename, 'r') as file:
        lines = file.read()
        lines = lines.split('\n')
        operations = lines.pop()
        result_re = re.split(r'\s+', operations)
        operations = [op for op in result_re if op]

        values = [werte.split() for werte in lines]

        values = np.array(values, dtype=int)

        return operations, values


#code with Gemini
def readTheFilePart2(filename):
    with open(filename, 'r') as file:
        lines = file.read()
        lines = lines.split('\n')
        operations = lines.pop()
        result_re = re.split(r'\s+', operations)
        operations = [op for op in result_re if op]

        maxColumLength = max((len(line) for line in lines))

        # Füllen fehlender Teile mit Leerzeichen, um ein rechteckiges Gitter zu erhalten
        grid = [line.ljust(maxColumLength) for line in lines]


        # Transponieren (Spalten werden zu Zeilen)
        # columns[i] ist jetzt der Inhalt der i-ten Spalte von oben nach unten
        columns = [''.join(grid[row][col] for row in range(len(grid)))
                   for col in range(maxColumLength)]

        # Initialisierung der Arrays (behalten Sie die Int-Typisierung bei, wenn möglich)
        values = []  # Muss 'object' sein, da es Listen/Arrays enthalten wird
        currentLine = []

        for col in columns:
            # 1. Nur Ziffern extrahieren, um die Zahl zu erhalten
            num_str = "".join(filter(str.isdigit, col))

            # Prüfen, ob die Spalte eine Zahl enthält
            if num_str:
                # Fügen Sie die Zahl zur aktuellen Problemliste hinzu
                currentLine.append(int(num_str))
            else:
                # Leere Spalte gefunden (Trenner)
                # 2. Das abgeschlossene Problem speichern
                if currentLine:
                    values.append(currentLine)

                currentLine = []

        if currentLine:
            values.append(currentLine)

        values = np.array(values, dtype=object)
        return operations, values


def part1():

    test = False

    if test:
        operations, values = readTheFile('Resources/day6Training.txt')
    else:
        operations, values = readTheFile('Resources/day6.txt')


    allValuesAdded = 0
    for col_index in range(values.shape[1]):
        column_values = values[:, col_index]

        op = operations[col_index]

        if op == '+':
            column_result = np.sum(column_values)
        elif op == '*':
            column_result = np.prod(column_values)

        allValuesAdded += column_result


    print(allValuesAdded)


def part2():

    test = False

    if test:
        operations, values = readTheFilePart2('Resources/day6Training.txt')
    else:
        operations, values = readTheFilePart2('Resources/day6.txt')


    allValuesAdded = 0
    for theValues in values:
        #column_values = values[:, col_index]

        op = operations.pop(0)

        if op == '+':
            # Summe der Spaltenwerte berechnen
            column_result = np.sum(theValues)
        elif op == '*':
            # Produkt der Spaltenwerte berechnen
            column_result = np.prod(theValues)

        allValuesAdded += column_result

    print(allValuesAdded)

if __name__ == '__main__':
    part1()
    part2()