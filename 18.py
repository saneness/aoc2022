from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=18)
data = [tuple(map(int, item.split(","))) for item in puzzle.input_data.splitlines()]

x_min, x_max = min([x for x, _, _ in data]) - 2, max([x for x, _, _ in data]) + 2
y_min, y_max = min([y for _, y, _ in data]) - 2, max([y for _, y, _ in data]) + 2
z_min, z_max = min([z for _, _, z in data]) - 2, max([z for _, _, z in data]) + 2

grid = [[[0 for x in range(x_min, x_max)] for y in range(x_min, y_max)] for z in range(z_min, z_max)]
surface = 0
for x, y, z in data:
    grid[z][y][x] = 1
    for dx, dy, dz in zip([-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]):
        if (x + dx, y + dy, z + dz) not in data:
            surface += 1

unvisited = [(x_min, y_min, z_min)]
exterior_surface = 0
while len(unvisited) > 0:
    x, y, z = unvisited.pop()
    for dx, dy, dz in zip([-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]):
        dx, dy, dz = x + dx, y + dy, z + dz
        if x_min <= dx < x_max and y_min <= dy < y_max and z_min <= dz < z_max:
            if grid[dz][dy][dx] == 1:
                exterior_surface += 1
            elif grid[dz][dy][dx] == 0:
                if (dx, dy, dz) not in unvisited:
                    unvisited.append((dx, dy, dz))
    grid[z][y][x] = -1

answer_a = surface
answer_b = exterior_surface

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b