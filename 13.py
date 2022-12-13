from aocd.models import Puzzle
import json
import math

puzzle = Puzzle(year=2022, day=13)
data = [[json.loads(subitem) for subitem in item.splitlines()] for item in puzzle.input_data.split("\n\n")]
# data = [[json.loads(subitem) for subitem in item.splitlines()] for item in open("test").read().split("\n\n")]

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
dividers = [1, 2]
for i, [first, second] in enumerate(data):
    ordered += i + 1 if compare(a=first, b=second) == -1 else 0
    dividers[0] += sum([1 for number in [first, second] if compare(a=[[2]], b=number) == 1])
    dividers[1] += sum([1 for number in [first, second] if compare(a=[[6]], b=number) == 1])

answer_a = ordered
answer_b = math.prod(dividers)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b
