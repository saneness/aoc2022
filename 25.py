from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=25)
data = puzzle.input_data.splitlines()

def to_snafu(number):
    result, i = [], 1
    while number // 5 > 0:
        result.append(number % 5)
        number, i = number // 5, i + 1
    if number % 5 > 0:
        result.append(number % 5)
    r = 0
    for i in range(len(result)):
        result[i], r = (result[i] + r - 5, 1) if result[i] + r > 2 else (result[i] + r, 0)
    if r > 0:
        result.append(r)
    code = { -2: "=", -1: "-", 0: "0", 1: "1", 2: "2" }
    return ''.join([code[c] for c in result][::-1])

def from_snafu(line):
    decode = { "=": -2, "-": -1, "0": 0, "1": 1, "2": 2 }
    return sum([5**i * decode[c] for i, c in enumerate([*line][::-1])])

answer_a = to_snafu(sum([from_snafu(line) for line in data]))

puzzle.answer_a = answer_a