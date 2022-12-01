from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=1)
data = [sum([int(subitem) for subitem in item.splitlines()]) for item in puzzle.input_data.split("\n\n")]

answer_a = sorted(data)[-1]
answer_b = sum(sorted(data)[-3:])

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b