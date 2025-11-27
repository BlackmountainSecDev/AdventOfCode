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


import matplotlib.pyplot as plt
import matplotlib.animation as animation

def simulate(datas, width, height, max_seconds=20000):
    positions_per_second = []

    for t in range(max_seconds):
        for d in datas:
            x, y = d["p"]
            vx, vy = d["v"]
            x = (x + vx) % width
            y = (y + vy) % height
            d["p"] = (x, y)
        positions_per_second.append([d["p"] for d in datas])
    return positions_per_second


def animate_motion(positions_per_second, width, height):
    fig, ax = plt.subplots()
    scat = ax.scatter([], [], s=10)
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect("equal")

    def update(frame):
        x, y = zip(*positions_per_second[frame])
        scat.set_offsets(list(zip(x, y)))
        ax.set_title(f"t = {frame}")
        return scat,

    ani = animation.FuncAnimation(fig, update, frames=len(positions_per_second), interval=50, blit=True)
    plt.show()

def part2():
    print('part 2')

    # TEST = True
    TEST = False
    MINX = 0
    MINY = 0

    if TEST:
        theFileName = "Resources/day14ResourceTraining.txt"
        # theFileName = "Resources/day14ResourceTraining2.txt"
        MAXX = 11
        MAXY = 7

    else:
        theFileName = "Resources/day14Resource.txt"
        MAXX = 101
        MAXY = 103

    datas = readTheFile(theFileName)

    positions_per_second = simulate(datas, width=MAXX, height=MAXY, max_seconds=100)
    animate_motion(positions_per_second, width=MAXX, height=MAXY)


    '''
    for round in range(100):
        #matrix = [[0 for _ in range(MAXY)] for _ in range(MAXX)]
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
            #matrix[x][y] = 1

    # find the lines
    verticalLine = math.floor(MAXX / 2)
    horizontalLine = math.floor(MAXY / 2)

    currentPositions = [entry['p'] for entry in datas]

    upperData = [entry for entry in currentPositions if entry[1] < horizontalLine]
    bottomData = [entry for entry in currentPositions if entry[1] > horizontalLine]

    leftUpperData = [entry for entry in upperData if entry[0] < verticalLine]
    rightUpperData = [entry for entry in upperData if entry[0] > verticalLine]

    leftBottomData = [entry for entry in bottomData if entry[0] < verticalLine]
    rightBottomData = [entry for entry in bottomData if entry[0] > verticalLine]

    print(len(leftUpperData) * len(rightUpperData) * len(leftBottomData) * len(rightBottomData))
    '''

import pygame
import math

# -----------------------------
# Konfiguration
# -----------------------------
WIDTH, HEIGHT = 101, 103  # Spielfeldgröße (für echtes Puzzle)
# WIDTH, HEIGHT = 11, 7    # für Testdaten
SCALE = 6                  # Vergrößerungsfaktor (Pixel pro Tile)
FPS = 60                   # Geschwindigkeit der Darstellung
SECONDS_PER_FRAME = 1      # wie viele "Simulationssekunden" pro Frame vergehen

# -----------------------------
# Datei einlesen (vereinfachte Version)
# -----------------------------
def read_data(filename):
    robots = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            p_part, v_part = line.split(" ")
            px, py = map(int, p_part[2:].split(","))
            vx, vy = map(int, v_part[2:].split(","))
            robots.append({"p": (px, py), "v": (vx, vy)})
    return robots

# -----------------------------
# Positionsupdate mit Wraparound
# -----------------------------
def update_positions(robots):
    for r in robots:
        x, y = r["p"]
        vx, vy = r["v"]
        x = (x + vx) % WIDTH
        y = (y + vy) % HEIGHT
        r["p"] = (x, y)

# -----------------------------
# Zeichnen
# -----------------------------
def draw(screen, robots, t):
    screen.fill((0, 0, 20))  # dunkler Hintergrund

    for r in robots:
        x, y = r["p"]
        px = x * SCALE
        py = y * SCALE
        pygame.draw.rect(screen, (0, 255, 80), (px, py, SCALE, SCALE))

    # Zeit anzeigen
    font = pygame.font.SysFont("consolas", 20)
    text = font.render(f"t = {t}s", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()


# -----------------------------
# Hauptprogramm
# -----------------------------
def part2pyGame():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH * SCALE, HEIGHT * SCALE))
    pygame.display.set_caption("Robot Swarm Simulation")

    clock = pygame.time.Clock()

    # Daten laden
    #filename = "Resources/day14ResourceTraining.txt"
    filename = "Resources/day14Resource.txt"
    robots = read_data(filename)

    running = True
    paused = False
    t = 0

    step_forward = False
    step_backward = False

    min_area = float("inf")
    best_time = 0
    best_positions = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                    print(f"{'⏸️ Pause' if paused else '▶️ Weiter'} bei t={t}")
                elif event.key == pygame.K_RIGHT:
                    step_forward = True
                elif event.key == pygame.K_LEFT:
                    step_backward = True
                elif event.key == pygame.K_ESCAPE:
                    running = False

        if not paused or step_forward:
            update_positions(robots)
            t += 1

            # --- 🧮 Bounding Box berechnen ---
            xs = [r["p"][0] for r in robots]
            ys = [r["p"][1] for r in robots]
            width = max(xs) - min(xs)
            height = max(ys) - min(ys)
            area = width * height

            # --- 📉 Wenn neues Minimum, speichern ---
            if area < min_area:
                min_area = area
                best_time = t
                best_positions = [(x, y) for x, y in zip(xs, ys)]
                print(f"🔎 Neue kleinste Fläche bei t={t} (Area={area})")

            # --- 🧠 Wenn die Fläche wieder wächst → vermutlich Baum erreicht ---
            elif area > min_area * 1.05:  # etwas Toleranz (5 %)
                paused = True
                print(f"🎄 Vermutlich Baum bei t={best_time} (Area={min_area})")
                # Optional: Roboter zurück auf den besten Zustand setzen
                for i, r in enumerate(robots):
                    r["p"] = best_positions[i]
                t = best_time

            step_forward = False

        elif step_backward:
            for r in robots:
                x, y = r["p"]
                vx, vy = r["v"]
                x = (x - vx) % WIDTH
                y = (y - vy) % HEIGHT
                r["p"] = (x, y)
            t -= 1
            if t < 0:
                t = 0
            print(f"t={t}")
            step_backward = False

        draw(screen, robots, t)
        clock.tick(FPS)


    pygame.quit()




if __name__ == '__main__':
    print('day 14')
    #part1()
    #part2()
    part2pyGame()