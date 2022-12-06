from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=3)
data = puzzle.input_data.splitlines()

def intersection(items):
    return ''.join([''.join(set.intersection(*item)) for item in items])

def priority(items):
    return sum([ord(char) - ord('a') + 1 if char.lower() == char else ord(char) - ord('A') + 27 for char in items])

compartments = [[set(item[:len(item)//2]), set(item[len(item)//2:])] for item in data]
groups = [[set(item) for item in data[i:i+3]] for i in range(0, len(data), 3)]

answer_a = priority(intersection(compartments))
answer_b = priority(intersection(groups))

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b
