from aocd.models import Puzzle
import functools

puzzle = Puzzle(year=2022, day=13)
data = [[eval(subitem) for subitem in item.splitlines()] for item in puzzle.input_data.split("\n\n")]

def _compare(a, b):
    if type(a) == list and type(b) == list:
        length = min(len(a), len(b))
        result = [_compare(ai, bi) for ai, bi in zip(a[:length], b[:length])]
        last = -1 if len(a) < len(b) else 1 if len(a) > len(b) else 0
        return result + [last]
    elif type(a) == int and type(b) == int:
        return -1 if a < b else 1 if a > b else 0
    elif type(a) == list and type(b) == int:
        return _compare(a, [b])
    elif type(a) == int and type(b) == list:
        return _compare([a], b)

def compare(a, b):
    comparison = str(_compare(a=a, b=b))
    first, second = comparison.find("-1"), comparison.find("1")
    return -1 if (0 < first < second or second < 0 < first) else 1 if (0 < second < first or first < 0 < second) else 0

ordered = 0
total = [[[2]], [[6]]]
for i, [first, second] in enumerate(data):
    total.append(first)
    total.append(second)
    result = compare(a=first, b=second)
    ordered += i + 1 if result == -1 else 0

total.sort(key=functools.cmp_to_key(compare))

answer_a = ordered
answer_b = (total.index([[2]]) + 1) * (total.index([[6]]) + 1)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b