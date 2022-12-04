from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2022, day=4)
data = [np.array(line.replace('-', ',').split(',')).astype(int) for line in puzzle.input_data.splitlines()]

answer_a = sum([1 if line[0] <= line[2] <= line[3] <= line[1] or line[2] <= line[0] <= line[1] <= line[3] else 0 for line in data])
answer_b = sum([1 if line[0] <= line[2] <= line[1]            or line[2] <= line[0] <= line[3]            else 0 for line in data])

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b