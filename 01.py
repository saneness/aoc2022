from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2022, day=1)
data = [sum(np.array(item.splitlines()).astype(int)) for item in puzzle.input_data.split("\n\n")]

answer_a = max(data)
answer_b = sum(sorted(data)[-3:])

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b