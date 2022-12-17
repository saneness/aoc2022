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
    if sum([1 for x, y in new if grid[y][x] == "#"]) == 0:
        rock = new
    under = [(x, y - 1) for x, y in rock]
    if sum([1 for x, y in under if grid[y][x] == "#"]) == 0:
        return False, under
    else:
        for x, y in rock:
            grid[y][x] = "#"
        return True, rock

grid = [['#' for _ in range(7)]] + [['.' for _ in range(7)] for _ in range(10000)]
moves = [*data]
step = 0
rocks = 0
height = 0

while rocks < 2022:
    rock = spawn_rock(height=height+4, n=rocks)
    placed = False
    while not placed:
        placed, rock = move_rock(grid=grid, rock=rock, direction=moves[step % len(moves)])
        step += 1
    height = max(height, max([y for _, y in rock]))
    rocks += 1

answer_a = height

puzzle.answer_a = answer_a