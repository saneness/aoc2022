from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=9)
data = puzzle.input_data.splitlines()

directions = {
    "R": [1, 0],
    "L": [-1, 0],
    "U": [0, 1],
    "D": [0, -1]
}

rope = [[0, 0] for i in range(10)]
visited = [set() for i in range(10)]

for line in data:
    side, repeat = line.split()[0], int(line.split()[1])
    for i in range(repeat):
        rope[0] = [pos + chg for pos, chg in zip(rope[0], directions[side])]
        for i in range(1, len(rope)):
            diff = [new - old for new, old in zip(rope[i-1], rope[i])]
            if abs(diff[0]) * abs(diff[1]) > 1:
                move = [(1 if pos > 0 else - 1) for pos in diff]
            elif abs(diff[0]) > 1 or abs(diff[1]) > 1:
                move = [(1 if pos > 1 else - 1) if abs(pos) > 1 else 0 for pos in diff]
            else:
                move = [0, 0]
            rope[i] = [pos + chg for pos, chg in zip(rope[i], move)]
        for i in range(10):
            visited[i].add((*rope[i],))

answer_a = len(visited[1])
answer_b = len(visited[9])

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b