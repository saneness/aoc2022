from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=6)
data = puzzle.input_data

def marker(message, n):
    return min([i + n for i in range(len(message)-n) if len(set(message[i:i+n])) == n])

answer_a = marker(message=data, n=4)
answer_b = marker(message=data, n=14)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b