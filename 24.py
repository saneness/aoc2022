from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=24)
data = [[*line][1:-1] for line in puzzle.input_data.splitlines()[1:-1]]

def blizzard_state(blizzard, j_max, i_max, time):
    move = {
        "N": { "dj": -1, "di": 0 },
        "S": { "dj": 1, "di": 0 },
        "W": { "dj": 0, "di": -1 },
        "E": { "dj": 0, "di": 1 }
    }
    return list(set([((j + time * move[direction]["dj"]) % j_max, (i + time * move[direction]["di"]) % i_max) for j, i, direction in blizzard]))

def new_moves(blizzard_next, j, i, j_max, i_max):
    common = [(j + dj, i + di) for dj, di in zip([1, 0, -1, 0, 0], [0, 1, 0, -1, 0]) if 0 <= j + dj < j_max and 0 <= i + di < i_max and (j + dj, i + di) not in blizzard_next]
    if (j, i) == (-1, 0):
        return [(j, i)] + ([(0, 0)] if (0, 0) not in blizzard_next else [])
    elif (j, i) == (j_max, i_max - 1):
        return [(j, i)] + ([(j_max - 1, i_max - 1)] if (j_max - 1, i_max - 1) not in blizzard_next else [])
    elif (j, i) == (0, 0):
        return [(-1, 0)] + common
    elif (j, i) == (j_max - 1, i_max - 1):
        return [(j_max, i_max - 1)] + common
    else:
        return common

def path(blizzard, start, end, time):
    j_start, i_start = start
    j_end, i_end = end
    j_max, i_max = max(end[0], start[0]), max(end[1], start[1]) + 1
    time += 1
    blizzard_next = blizzard_state(blizzard=blizzard, j_max=j_max, i_max=i_max, time=time)
    to_check = new_moves(blizzard_next=blizzard_next, j=j_start, i=i_start, j_max=j_max, i_max=i_max)
    while len(to_check) > 0:
        new = []
        time += 1
        blizzard_next = blizzard_state(blizzard=blizzard, j_max=j_max, i_max=i_max, time=time)
        for j, i in to_check:
            new += (new_moves(blizzard_next=blizzard_next, j=j, i=i, j_max=j_max, i_max=i_max))
            new = list(set(new))
        if len(new) > 0:
            to_check = sorted(new.copy(), key=lambda x: abs(x[0]-j_end) + abs(x[1] - i_end))[:100]
        if end in to_check:
            return time
    return -1

blizzard = []
j_max, i_max = len(data), len(data[0])
for j in range(j_max):
    for i in range(i_max):
        match data[j][i]:
            case "^":
                blizzard.append((j, i, "N"))
            case "v":
                blizzard.append((j, i, "S"))
            case "<":
                blizzard.append((j, i, "W"))
            case ">":
                blizzard.append((j, i, "E"))

start, end = (-1, 0), (j_max, i_max - 1)
t1 = path(blizzard=blizzard, start=start, end=end, time=0)
t2 = path(blizzard=blizzard, start=end, end=start, time=t1)
t3 = path(blizzard=blizzard, start=start, end=end, time=t2)

answer_a = t1
answer_b = t3

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b