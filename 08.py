from aocd.models import Puzzle
import numpy as np
import math

puzzle = Puzzle(year=2022, day=8)
data = np.array([[*line] for line in puzzle.input_data.splitlines()]).astype(int)

visible_to = 4 * (len(data) - 1)
visible_from = 0
for (i, j), tree in np.ndenumerate(data[1:-1, 1:-1]):
    sides = [[tree >= data[i+1][j+1] for tree in side] for side in [data[i+1, :j+1], data[i+1, j+2:], data[:i+1, j+1], data[i+2:, j+1]]]
    visible_to += not math.prod([sum(side) for side in sides])
    visible_from = max(visible_from, math.prod([((side[::-1] if sides.index(side) % 2 == 0 else side)[:-1] + [1]).index(1) + 1 for side in sides]))

answer_a = visible_to
answer_b = visible_from

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b