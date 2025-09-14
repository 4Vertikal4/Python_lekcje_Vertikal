import time
import os

# Labirynt Makłowicza
maze_template = [
    "##########",
    "#........#",
    "#.######.#",
    "#........#",
    "#.######.#",
    "#........#",
    "#######..#",
    "#........X",
    "##########"
]

def display(maze, row, col):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nKUCHNIA MAKŁOWICZA\n")
    
    for i, line in enumerate(maze):
        if i == row:
            line_list = list(line)
            line_list[col] = '@'
            print(' '.join(line_list))
        else:
            print(' '.join(line))
    print()

# GŁÓWNY PROGRAM
print("Proszę państwa, utknąłem w labiryncie własnej kuchni!")
time.sleep(2)

row, col = 1, 1
kroki = 0

# Prosty algorytm: preferuj dół i prawo
while maze_template[row][col] != 'X':
    display(maze_template, row, col)
    kroki += 1
    
    # Priorytet: dół > prawo > lewo > góra
    if row + 1 < len(maze_template) and maze_template[row + 1][col] in '.X':
        row += 1
        print("Schodzę w dół, jak temperatura przy blanszowaniu!")
    elif col + 1 < len(maze_template[0]) and maze_template[row][col + 1] in '.X':
        col += 1
        print("W prawo, jak przy mieszaniu risotto!")
    elif col - 1 >= 0 and maze_template[row][col - 1] in '.X':
        col -= 1
        print("W lewo, zawsze pod prąd!")
    elif row - 1 >= 0 and maze_template[row - 1][col] in '.X':
        row -= 1
        print("W górę, jak suflety w piekarniku!")
    
    time.sleep(1)

display(maze_template, row, col)
print("Eureka! Znalazłem wyjście! Czas na aperitif!")
print(f"\nMakłowicz dotarł do wyjścia w {kroki} krokach!")

