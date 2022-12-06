from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=6)
data = puzzle.input_data

def marker(message, n):
    for i in range(len(data)-n):
        packet = data[i:i+n]
        if len(set(packet)) == len(packet):
            return i + n

answer_a = marker(data, 4)
answer_b = marker(data, 14)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b