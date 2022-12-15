from aocd.models import Puzzle
import re
import time

start_time = time.time()

puzzle = Puzzle(year=2022, day=15)
data = puzzle.input_data

rx = re.compile(r"Sensor\ at\ x=(?P<sx>\-?\d+),\ y=(?P<sy>\-?\d+):\ closest\ beacon\ is\ at\ x=(?P<bx>\-?\d+),\ y=(?P<by>\-?\d+)", re.VERBOSE)
data = [tuple(map(int, [m.group("sx"), m.group("sy"), m.group("bx"), m.group("by")])) for m in rx.finditer(data)]

row = 2000000
col = 4000000

areas = []
sensors = []
beacons = []
for line in data:
    sensor = (line[0], line[1])
    beacon = (line[2], line[3])
    diff = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    area = {
        "from": (sensor[0], sensor[1]-diff),
        "to": (sensor[0], sensor[1]+diff)
    }
    sensors.append(sensor)
    if beacon not in beacons:
        beacons.append(beacon)
    areas.append(area)

def get_lines(areas, n):
    lines = []
    min_left = None
    max_right = None
    for area in areas:
        if area["from"][1] <= n <= area["to"][1]:
            diff = min(area["to"][1] - n, n - area["from"][1])
            left = area["from"][0]-diff
            right = area["from"][0]+diff
            lines.append((left, right))
            min_left = left if min_left is None else min(min_left, left)
            max_right = right if max_right is None else max(max_right, right)
    return lines

def merge_lines(lines, left=None, right=None):
    lines = sorted(lines.copy())
    if left is not None and lines[0][0] < left:
        result = (0, lines[0][1])
    else:
        result = lines[0]
    for line in lines[1:]:
        if left is not None and line[0] < left:
            line = (0, line[1])
        if result[0] <= line[0] <= result[1] <= line[1] or result[0] <= line[0] - 1 <= result[1] <= line[1]:
            if right is not None and line[1] > right:
                return (result[0], right)
            else:
                result = (result[0], line[1])
        elif result[1] < line[0]:
            return result[1] + 1
    return result

lines = get_lines(areas=areas, n=row)
target = merge_lines(lines=lines)

for i in range(row*2+1):
    lines=get_lines(areas=areas, n=i)
    merged=merge_lines(lines=lines, left=0, right=col)
    if type(merged) == int:
        location = (i, merged)
        break

answer_a = target[1] - target[0] + 1 - sum([1 for filled in sensors + beacons if filled[1] == row])
answer_b = location[1] * 4000000 + location[0]

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b