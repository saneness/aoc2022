from aocd.models import Puzzle
from copy import deepcopy

puzzle = Puzzle(year=2022, day=12)
data = [[ord(char) for char in line] for line in puzzle.input_data.splitlines()]

def get_path(grid, start):
    i_size = len(grid)
    j_size = len(grid[0])
    paths = [[-1 for _ in range(j_size)] for _ in range(i_size)]
    unvisited = []
    for i in range(i_size):
        for j in range(j_size):
                if chr(grid[i][j]) in start:
                    paths[i][j] = 0
                    if chr(grid[i][j]) == "S":
                        grid[i][j] = 96
                    unvisited.append((i, j, grid[i][j], 0))
                if chr(grid[i][j]) == "E":
                    grid[i][j] = 123
                    end = (i, j)

    while len(unvisited) > 0:
        unvisited.sort(key=lambda x: -paths[x[0]][x[1]])
        current = unvisited.pop()
        for (i, j) in zip([-1, 1, 0, 0], [0, 0, -1, +1]):
            i += current[0]
            j += current[1]
            if 0 <= i < i_size and 0 <= j < j_size and paths[i][j] == -1 and grid[i][j] - current[2] <= 1:
                paths[i][j] = current[3] + 1
                unvisited.append((i, j, grid[i][j], paths[i][j]))

    return paths[end[0]][end[1]]

answer_a = get_path(grid=deepcopy(data), start=["S"])
answer_b = get_path(grid=deepcopy(data), start=["S", "a"])

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b