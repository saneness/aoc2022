from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=4)
data = puzzle.input_data.splitlines()

answer_a = 0
answer_b = 0

for line in data:
    line = [int(item) for item in line.replace('-', ',').split(',')]
    first, second = [set(range(line[0], line[1] + 1)), set(range(line[2], line[3] + 1))]
    answer_a += 1 if len(set.intersection(first, second)) in [len(first), len(second)] else 0
    answer_b += 1 if len(set.intersection(first, second)) > 0 else 0

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b