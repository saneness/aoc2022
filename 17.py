from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=17)
data = puzzle.input_data

def spawn_rock(height, n):
    match n % 5:
        case 0:
            return [(2, height), (3, height), (4, height), (5, height)]
        case 1:
            return [(3, height), (2, height + 1), (3, height + 1), (4, height + 1), (3, height + 2)]
        case 2:
            return [(2, height), (3, height), (4, height), (4, height + 1), (4, height + 2)]
        case 3:
            return [(2, height), (2, height + 1), (2, height + 2), (2, height + 3)]
        case 4:
            return [(2, height), (3, height), (2, height + 1), (3, height + 1)]

def move_rock(grid, rock, direction):
    x_min = min([x for x, _ in rock])
    x_max = max([x for x, _ in rock])
    if direction == "<" and x_min > 0:
        new = [(x - 1, y) for x, y in rock]
    elif direction == ">" and x_max < 6:
        new = [(x + 1, y) for x, y in rock]
    else:
        new = rock
    if sum([1 for x, y in new if (x, y) in grid]) == 0:
        rock = new
    under = [(x, y - 1) for x, y in rock]
    if sum([1 for x, y in under if (x, y) in grid]) == 0:
        return False, under
    else:
        for x, y in rock:
            grid.add((x, y))
        return True, rock

def play(moves, count):
    grid = {(i, 0) for i in range(7)}
    step = 0
    rocks = 0
    height = 0
    height_skip = 0
    states = {}
    while rocks < count:
        rock = spawn_rock(height=height+4, n=rocks)
        placed = False
        while not placed:
            placed, rock = move_rock(grid=grid, rock=rock, direction=moves[step])
            step = (step + 1) % len(moves)
        height = max(height, max([y for _, y in rock]))
        top = tuple(max([y for x, y in grid if x == i]) for i in range(7))
        top = tuple(y - min(top) for y in top)
        current_state = (top, rocks % 5, step)
        if current_state in states:
            rocks_old, height_old = states[current_state]
            rocks_diff, height_diff = rocks - rocks_old, height - height_old
            cycles = (count - rocks) // rocks_diff
            rocks += rocks_diff * cycles
            height_skip += height_diff * cycles
        states.update({current_state: (rocks, height)})
        rocks = rocks + 1
    return height + height_skip

answer_a = play(moves=data, count=2022)
answer_b = play(moves=data, count=1000000000000)

print(answer_a)
print(answer_b)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b