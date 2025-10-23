from sympy import symbols, Eq, solve
import re
import numpy as np



def gesamt_tokens_sympy(datei, offset=0):
    x, y = symbols('x y', integer=True, nonnegative=True)

    with open(datei, "r", encoding="utf-8") as f:
        content = f.read()  #ließt die Datei

    #erstellt ein Muster mit regex
    pattern = re.compile(
        r"Button A: X\+(\d+), Y\+(\d+)\s*"
        r"Button B: X\+(\d+), Y\+(\d+)\s*"
        r"Prize: X=(\d+), Y=(\d+)",
        re.MULTILINE
    )


    matches = pattern.findall(content)  #extrahiert die Daten anhand des Regex Musters
    gesamt = 0

    for match in matches:
        a_x, a_y, b_x, b_y, p_x, p_y = map(int, match)      #wandelt die Werte von String in int
        # Offset hinzufügen
        p_x += offset
        p_y += offset

        #Mathe
        eq1 = Eq(a_x*x + b_x*y, p_x)
        eq2 = Eq(a_y*x + b_y*y, p_y)

        sol = solve((eq1, eq2), (x, y), dict=True)

        if sol:
            sol_xy = sol[0]
            X_val = sol_xy[x]
            Y_val = sol_xy[y]
            # Token-Kosten berechnen
            gesamt += 3*X_val + Y_val

    return gesamt



def part1():
    '''
    *********************************
    * Solution created with ChatGPT *
    *********************************
    '''
    total_tokens = gesamt_tokens_sympy("Resources/day13Resource.txt", offset=0)
    print(total_tokens)


def part2():
    '''
    *********************************
    * Solution created with ChatGPT *
    *********************************
    '''
    total_tokens = gesamt_tokens_sympy("Resources/day13Resource.txt", offset=10_000_000_000_000)
    print(total_tokens)



if __name__ == '__main__':
    part1()
    part2()