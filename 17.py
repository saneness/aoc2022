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
    pass

step = 0
grid = ['#' for _ in range(7)] + [['.' for _ in range(7)] for _ in range(10000)]