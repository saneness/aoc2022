from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2022, day=8)
data = np.array([[*line] for line in puzzle.input_data.splitlines()]).astype(int)

def is_visible_to(trees, i, j):
    left = sum([0 if tree < trees[i][j] else 1 for tree in trees[i, :j]]) == 0
    right = sum([0 if tree < trees[i][j] else 1 for tree in trees[i, j+1:]]) == 0
    up = sum([0 if tree < trees[i][j] else 1 for tree in trees[:i, j]]) == 0
    down = sum([0 if tree < trees[i][j] else 1 for tree in trees[i+1:, j]]) == 0
    return left + right + up + down > 0

def is_visible_from(trees, i, j):
    left = [0 if tree < trees[i][j] else 1 for tree in trees[i, :j]][::-1]
    right = [0 if tree < trees[i][j] else 1 for tree in trees[i, j+1:]]
    up = [0 if tree < trees[i][j] else 1 for tree in trees[:i, j]][::-1]
    down = [0 if tree < trees[i][j] else 1 for tree in trees[i+1:, j]]
    left[-1], right[-1], up[-1], down[-1] = 1, 1, 1, 1
    return (left.index(1) + 1) * (right.index(1) + 1) * (up.index(1) + 1) * (down.index(1) + 1)

visible_to = 4 * (len(data) - 1)
visible_from = 0
for (i, j), tree in np.ndenumerate(data[1:-1, 1:-1]):
    visible_to += is_visible_to(data, i + 1, j + 1)
    visible_from = max(visible_from, is_visible_from(data, i + 1, j + 1))

answer_a = visible_to
answer_b = visible_from

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b