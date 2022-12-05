from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2022, day=4)
data = [np.array(line.replace('-', ',').split(',')).astype(int) for line in puzzle.input_data.splitlines()]

answer_a = sum([1 if from1 <= from2 <= to2 <= to1 or from2 <= from1 <= to1 <= to2 else 0 for [from1, to1, from2, to2] in data])
answer_b = sum([1 if from1 <= from2        <= to1 or from2 <= from1        <= to2 else 0 for [from1, to1, from2, to2] in data])

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b