from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=23)
data = [[*line] for line in puzzle.input_data.splitlines()]

coordinates = {
    "N": { "dj": [-1, -1, -1], "di": [-1, 0, 1] },
    "S": { "dj": [1, 1, 1], "di": [-1, 0, 1] },
    "W": { "dj": [-1, 0, 1], "di": [-1, -1, -1] },
    "E": { "dj": [-1, 0, 1], "di": [1, 1, 1] }
}

def propose(elf, elves, directions):
    j, i = elf
    if sum([1 for dj, di in zip([-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]) if (j + dj, i + di) in elves]) > 0:
        for direction in directions:
            if sum([1 if (j + dj, i + di) in elves else 0 for dj, di in zip(*coordinates[direction].values())]) == 0:
                return j + coordinates[direction]["dj"][1], i + coordinates[direction]["di"][1]
    return j, i

def move(elves, directions):
    elves_new = []
    conflicts = []
    for elf in elves:
        j_new, i_new = propose(elf=elf, elves=elves, directions=directions)
        if (j_new, i_new) in elves_new and (j_new, i_new) not in conflicts:
            conflicts.append((j_new, i_new))
        elves_new.append((j_new, i_new))
    elves_new = [elf if elf_new in conflicts else elf_new  for elf, elf_new in zip(elves, elves_new)]
    return elves_new, directions[1:] + directions[:1]

def normalize(elves):
    min_j, min_i = min([j for j, _ in elves]), min([i for _, i in elves])
    return [(j - min_j, i - min_i) for j, i in elves]

def empty_tiles(elves):
    max_j, max_i = max([j for j, _ in elves]), max([i for _, i in elves])
    return (max_j + 1) * (max_i + 1) - len(elves)

elves = [(j, i) for i in range(len(data[0])) for j in range(len(data)) if data[j][i] == "#"]
directions = ["N", "S", "W", "E"]
elves_new, directions_new = move(elves=elves, directions=directions)

for _ in range(10):
    elves, directions = elves_new, directions_new
    elves_new, directions_new = move(elves=elves, directions=directions)
empty = empty_tiles(normalize(elves))

i = 10
while elves_new != elves:
    elves, directions = elves_new, directions_new
    elves_new, directions_new = move(elves=elves, directions=directions)
    i += 1

answer_a = empty
answer_b = i + 1

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b