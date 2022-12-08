from aocd.models import Puzzle
import numpy as np
import math

puzzle = Puzzle(year=2022, day=8)
data = np.array([[*line] for line in puzzle.input_data.splitlines()]).astype(int)

def is_visible(trees, i, j):
    sides = [[tree >= trees[i][j] for tree in side] for side in [trees[i, :j], trees[i, j+1:], trees[:i, j], trees[i+1:, j]]]
    return not math.prod([sum(side) for side in sides]), math.prod([((side[::-1] if sides.index(side) % 2 == 0 else side)[:-1] + [1]).index(1) + 1 for side in sides])

visible_to = 4 * (len(data) - 1)
visible_from = 0
for (i, j), tree in np.ndenumerate(data[1:-1, 1:-1]):
    _to, _from = is_visible(data, i + 1, j + 1)
    visible_to += _to
    visible_from = max(visible_from, _from)

answer_a = visible_to
answer_b = visible_from

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b