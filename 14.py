from aocd.models import Puzzle
from copy import deepcopy

puzzle = Puzzle(year=2022, day=14)
data = [[list(map(int, subitem.split(","))) for subitem in item.split(" -> ")] for item in puzzle.input_data.splitlines()]

y_size_to = max([max([subitem[1] for subitem in item]) for item in data]) + 2
x_size_from = 499 - y_size_to
x_size_to = 501 + y_size_to
x_start = 500 - x_size_from

normalized_data = [[[subitem[0] - x_size_from, subitem[1]] for subitem in item] for item in data]
grid = [['.' for i in range(x_size_from, x_size_to)] for j in range(y_size_to)] + [['#' for i in range(x_size_from, x_size_to)]]

for rock in normalized_data:
    for i, [x_to, y_to] in enumerate(rock[1:], start=1):
        [x_from, x_to] = sorted([rock[i-1][0], x_to])
        [y_from, y_to] = sorted([rock[i-1][1], y_to])
        for x in range(x_from, x_to + 1):
            for y in range(y_from, y_to + 1):
                grid[y][x] = "#"

def add_unit(cave, x, y):
    try:
        if cave[y+1][x] not in ["#", "o"]:
            return add_unit(cave=cave, x=x, y=y+1)
        elif cave[y+1][x-1] not in ["#", "o"]:
            return add_unit(cave=cave, x=x-1, y=y+1)
        elif cave[y+1][x+1] not in ["#", "o"]:
            return add_unit(cave=cave, x=x+1, y=y+1)
        else:
            return x, y
    except IndexError:
        return None, None

def count(cave, x_start, y_max):
    cave=deepcopy(cave)
    count = 0
    while True:
        x, y = add_unit(cave=cave, x=x_start, y=0)
        if x is not None and y is not None and y < y_max and cave[y][x] == ".":
            cave[y][x] = "o"
            count += 1
        else:
            break
    return count

answer_a = count(cave=grid, x_start=x_start, y_max=y_size_to-2)
answer_b = count(cave=grid, x_start=x_start, y_max=y_size_to) 

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b