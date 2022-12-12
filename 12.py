from aocd.models import Puzzle
from copy import deepcopy

puzzle = Puzzle(year=2022, day=12)
data = [[ord(char) for char in line] for line in puzzle.input_data.splitlines()]

def get_path(data, start):
    i_size = len(data)
    j_size = len(data[0])
    paths = [[-1 for _ in range(j_size)] for _ in range(i_size)]
    unvisited = []
    for i in range(i_size):
        for j in range(j_size):
                if chr(data[i][j]) in start:
                    paths[i][j] = 0
                    unvisited.append((i, j))
                if chr(data[i][j]) == "S":
                    data[i][j] = 96
                if chr(data[i][j]) == "E":
                    data[i][j] = 123
                    end = (i, j)

    while len(unvisited) > 0:
        unvisited.sort(key=lambda x: -paths[x[0]][x[1]])
        next = unvisited.pop()
        for (i, j) in zip([-1, 1, 0, 0], [0, 0, -1, 1]):
            if 0 <= next[0] + i < i_size and 0 <= next[1] + j < j_size and paths[next[0] + i][next[1] + j] == -1 and data[next[0] + i][next[1] + j] - data[next[0]][next[1]] <= 1:
                paths[next[0] + i][next[1] + j] = paths[next[0]][next[1]] + 1
                unvisited.append((next[0] + i, next[1] + j))

    return paths[end[0]][end[1]]

answer_a = get_path(deepcopy(data), start=["S"])
answer_b = get_path(deepcopy(data), start=["S", "a"])

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b