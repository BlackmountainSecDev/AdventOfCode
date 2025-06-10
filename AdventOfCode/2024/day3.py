import re

def readTheFile():
    with open('Resources/day3Resource.txt', 'r') as lines:
        return lines.readline()

def part1():
    content = readTheFile()
    pattern = r"mul\(\d+,\d+\)"
    findings = re.findall(pattern, content)

    print(findings)

    nextPattern = r"-?\d+\.?\d*"
    # Alle Treffer finden
    wholeNumber = 0
    for x in findings:
        zahlen = re.findall(nextPattern, x)
        aha = [float(zahl) if '.' in zahl else int(zahl) for zahl in zahlen]
        wholeNumber += (aha[0]*aha[1])

    print(wholeNumber)


def berechne_mul_summe(text):
    # Regex für die Erkennung von mul(x,y), do() und don't()
    mul_pattern = r"mul\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)"
    control_pattern = r"do\(\)|don't\(\)"

    # Startzustand: mul-Anweisungen sind aktiviert
    mul_aktiviert = True
    summe = 0

    # Text in Teile zerlegen: Jede do(), don't() oder mul(x,y) einzeln finden
    matches = re.finditer(f"{control_pattern}|{mul_pattern}", text)

    for match in matches:
        # Prüfen, ob es eine Steueranweisung ist
        if match.group(0) == "do()":
            mul_aktiviert = True
        elif match.group(0) == "don't()":
            mul_aktiviert = False
        # Prüfen, ob es eine mul-Anweisung ist
        elif match.lastindex == 2:  # Wenn beide Zahlen in Gruppen gefunden wurden
            if mul_aktiviert:  # Nur aktive mul-Anweisungen verarbeiten
                x, y = int(match.group(1)), int(match.group(2))
                summe += x * y

    return summe

def part2():
    content = readTheFile()
    print(content)
    ergebnis = berechne_mul_summe(content)
    print(ergebnis)


if __name__ == '__main__':
    part1()
    part2()