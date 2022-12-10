from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2022, day=10)
data = re.sub("addx", "noop\naddx", puzzle.input_data).splitlines()

def decode(coded):
    decoder = {
        "111110-001001-001001-111110": "A",
        "111111-100101-100101-011010": "B",
        "011110-100001-100001-010010": "C",
        # "": "D",
        "111111-100101-100101-100001": "E",
        "111111-000101-000101-000001": "F",
        "011110-100001-101001-111010": "G",
        "111111-000100-000100-111111": "H",
        # "": "I",
        "010000-100000-100001-011111": "J",
        "111111-000100-011010-100001": "K",
        "111111-100000-100000-100000": "L",
        # "": "M",
        # "": "N",
        "011110-100001-100001-011110": "O",
        "111111-001001-001001-000110": "P",
        "011110-100001-100011-011111": "Q",
        "111111-001001-011001-100110": "R",
        "010010-100101-101001-010010": "S",
        # "": "T",
        "011111-100000-100000-011111": "U",
        # "": "V",
        # "": "W",
        # "": "X",
        # "": "Y",
        "110001-101001-100101-100011": "Z"
    }

    coded_list = []
    for i in range(len(coded[0]) // 5):
        temp = []
        for j in range(4):
            temp.append("".join([coded[k][i*5+j] for k in range(6)][::-1]).replace("#", "1").replace(".", "0"))
        coded_list.append("-".join(temp))

    return "".join(decoder[coded] for coded in coded_list)

cycle, x = 0, 1
signals, pixels = [], []
row = ''
for line in data:
    cycle += 1
    row += '#' if abs(cycle % 40 - x - 1) <= 1 else '.'
    if cycle % 40 == 20:
        signals.append(x * cycle)
    if cycle % 40 == 0:
        pixels.append(row)
        row = ''
    x += 0 if line == "noop" else int(line.split()[1])

answer_a = sum(signals)
answer_b = decode(pixels)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b