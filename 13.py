from aocd.models import Puzzle
import functools
import json

puzzle = Puzzle(year=2022, day=13)
data = [[json.loads(subitem) for subitem in item.splitlines()] for item in puzzle.input_data.split("\n\n")]

def compare_inner(a, b):
    if type(a) == list and type(b) == list:
        length = min(len(a), len(b))
        result = [compare_inner(ai, bi) for ai, bi in zip(a[:length], b[:length])]
        last = -1 if len(a) < len(b) else 1 if len(a) > len(b) else 0
        return result + [last]
    elif type(a) == int and type(b) == int:
        return -1 if a < b else 1 if a > b else 0
    elif type(a) == list and type(b) == int:
        return compare_inner(a, [b])
    elif type(a) == int and type(b) == list:
        return compare_inner([a], b)

def compare(a, b):
    comparison = str(compare_inner(a=a, b=b))
    less, more = comparison.find("-1"), comparison.find("1")
    return -1 if (0 < less < more or more < 0 < less) else 1 if (0 < more < less or less < 0 < more) else 0

ordered = 0
total = [[[2]], [[6]]]
for i, [first, second] in enumerate(data):
    ordered += i + 1 if compare(a=first, b=second) == -1 else 0
    total += first, second

total.sort(key=functools.cmp_to_key(compare))

answer_a = ordered
answer_b = (total.index([[2]]) + 1) * (total.index([[6]]) + 1)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b