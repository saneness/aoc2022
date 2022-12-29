from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2022, day=22)
data = puzzle.input_data.split("\n\n")

def unfolded(grid, pos, move, action):
    j, i = pos
    dj, di = move
    match action:
        case "R":
            dj, di = di, -dj
        case "L":
            dj, di = -di, dj
        case _:
            action = int(action)
            while action > 0:
                if j + dj >= len(grid) or i + di >= len(grid[0]) or j + dj < 0 or i + di < 0 or grid[j+dj][i+di] == " ":
                    if dj == 0 and di > 0:
                            hash_i = min([_i for _i, c in enumerate(grid[j]) if c == "#"])
                            dot_i = min([_i for _i, c in enumerate(grid[j]) if c == "."])
                            if hash_i < dot_i:
                                action = 0
                            else:
                                i = dot_i
                    elif dj == 0 and di < 0:
                            hash_i = max([_i for _i, c in enumerate(grid[j]) if c == "#"])
                            dot_i = max([_i for _i, c in enumerate(grid[j]) if c == "."])
                            if hash_i > dot_i:
                                action = 0
                            else:
                                i = dot_i
                    elif di == 0 and dj > 0:
                        hash_j = min([_j for _j in range(len(grid)) if grid[_j][i] == "#"])
                        dot_j = min([_j for _j in range(len(grid)) if grid[_j][i] == "."])
                        if hash_j < dot_j:
                            action = 0
                        else:
                            j = dot_j
                    elif di == 0 and dj < 0:
                        hash_j = max([_j for _j in range(len(grid)) if grid[_j][i] == "#"])
                        dot_j = max([_j for _j in range(len(grid)) if grid[_j][i] == "."])
                        if hash_j > dot_j:
                            action = 0
                        else:
                            j = dot_j
                elif grid[j+dj][i+di] == "#":
                    action = 0
                else:
                    j += dj
                    i += di
                action -= 1
    return (j, i), (dj, di)

def folded(grid, pos, move, action):
    j, i = pos
    dj, di = move
    match action:
        case "R":
            dj, di = di, -dj
        case "L":
            dj, di = -di, dj
        case _:
            action = int(action)
            while action > 0:
                if j + dj == 200 or i + di == 150 or j + dj == -1 or i + di == -1 or grid[j+dj][i+di] == " ":
                    if j == 0 and 50 <= i < 100 and dj == -1:
                        j_new, i_new = i + 100, 0
                        dj_new, di_new = 0, 1
                    elif j == 0 and 100 <= i < 150 and dj == -1:
                        j_new, i_new = 200 - 1, i - 100
                        dj_new, di_new = -1, 0
                    elif 0 <= j < 50 and i == 150 - 1 and di == 1:
                        j_new, i_new = 150 - 1 - j , 100 - 1
                        dj_new, di_new = 0, -1
                    elif j == 50 - 1 and 100 <= i < 150 and dj == 1:
                        j_new, i_new = i - 50, 100 - 1
                        dj_new, di_new = 0, -1
                    elif 50 <= j < 100 and i == 100 - 1 and di == 1:
                        j_new, i_new = 50 - 1, j + 50
                        dj_new, di_new = -1, 0
                    elif 100 <= j < 150 and i == 100 - 1 and di == 1:
                        j_new, i_new = 150 - 1 - j, 150 - 1
                        dj_new, di_new = 0, -1
                    elif j == 150 - 1 and 50 <= i < 100 and dj == 1:
                        j_new, i_new = i + 100, 50 - 1
                        dj_new, di_new = 0, -1
                    elif 150 <= j < 200 and i == 50 - 1 and di == 1:
                        j_new, i_new = 150 - 1, j - 100
                        dj_new, di_new = -1, 0
                    elif j == 200 - 1 and 0 <= i < 50 and dj == 1:
                        j_new, i_new = 0, i + 100
                        dj_new, di_new = 1, 0
                    elif 150 <= j < 200 and i == 0 and di == -1:
                        j_new, i_new = 0, j - 100
                        dj_new, di_new = 1, 0
                    elif 100 <= j < 150 and i == 0 and di == -1:
                        j_new, i_new = 150 - 1 - j, 50
                        dj_new, di_new = 0, 1
                    elif j == 100 and 0 <= i < 50 and dj == -1:
                        j_new, i_new = i + 50, 50
                        dj_new, di_new = 0, 1
                    elif 50 <= j < 100 and i == 50 and di == -1:
                        j_new, i_new = 100, j - 50
                        dj_new, di_new = 1, 0
                    elif 0 <= j < 50 and i == 50 and di == -1:
                        j_new, i_new = 150 - 1 - j, 0
                        dj_new, di_new = 0, 1
                    if grid[j_new][i_new] == "#":
                        action = 0
                    else:
                        j, i, dj, di = j_new, i_new, dj_new, di_new
                elif grid[j+dj][i+di] == "#":
                    action = 0
                else:
                    j += dj
                    i += di
                action -= 1
    return (j, i), (dj, di)

def score(pos, move):
    decode = { (0, 1): 0, (1, 0): 1, (-1, 0): 2, (0, -1): 3 }
    return (pos[0] + 1) * 1000 + (pos[1] + 1) * 4 + decode[move]

def solve(grid, path, cube=False):
    start = (0, min([i for i, c in enumerate(grid[0]) if c == "."]))
    pos, move = start, (0, 1)
    path = path.copy()
    while path:
        action = path.pop()
        if not cube:
            pos, move = unfolded(grid=grid, pos=pos, move=move, action=action)
        else:
            pos, move = folded(grid=grid, pos=pos, move=move, action=action)
    return score(pos, move)

size, n_j, n_i = 50, 4, 3
rx_path = re.compile(r"(?P<action>(\d+|\w))")
grid, path = [[*(line + ' ' * (n_i * size - len(line)))] for line in data[0].splitlines()], [m.group("action") for m in rx_path.finditer(data[1])][::-1]

answer_a = solve(grid=grid, path=path)
answer_b = solve(grid=grid, path=path, cube=True)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b