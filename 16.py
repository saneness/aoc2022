from aocd.models import Puzzle
import re

puzzle = Puzzle(year=2022, day=16)
data = puzzle.input_data
rx = re.compile(r"Valve\ (?P<in>\w{2})\ has\ flow\ rate\=(?P<rate>\d+);\ tunnels?\ leads?\ to\ valves?\ (?P<out>\w{2}(\,\ \w{2})*)", re.VERBOSE)
valves = {
    m.group("in"):
    {
        "id": m.group("in"),
        "rate": int(m.group("rate")),
        "out": m.group("out").split(", ")
    } for m in rx.finditer(data)}

def get_distance(valves, _from, _to, parents=[]):
    if _to["id"] in _from["out"]:
        return 2
    else:
        _from_out = [_out for _out in _from["out"] if _out not in parents]
        if len(_from_out) > 0:
            return min([1 + get_distance(valves=valves, _from=valves[_out], _to=_to, parents=parents.copy() + [_from["id"]]) for _out in _from_out])
        else:
            return 1e12

def get_paths(distances, valves, start, time):
    pressures = []
    paths = []
    states = [([start], 0, time)]
    while len(states) > 0:
        path, pressure, time = states.pop()
        current = path[-1]
        new = []
        for valve, distance in distances[current].items():
            if distance <= time and valve not in path:
                dtime = time - distance
                dpressure = pressure + valves[valve]["rate"] * dtime
                new.append((path + [valve], dpressure, dtime))
        if len(new) > 0:
            states += new
        else:
            pressures.append(pressure)
            paths.append(path[1:])
    return pressures, paths

start = 'AA'
valve_list = [start] + [m.group("in") for m in rx.finditer(data) if int(m.group("rate")) > 0]
n = len(valve_list)

distances = {a: {b: -1 for b in valve_list if b != a} for a in valve_list}
for i in valve_list:
    for j in valve_list:
        if i != j:
            distances[i][j] = distances[j][i] = get_distance(valves=valves, _from=valves[i], _to=valves[j])

pressures, paths = get_paths(distances, valves, start, 30)
with_help = sorted(zip(*get_paths(distances, valves, start, 26)))[::-1]
i = 1
while len(set(with_help[0][1]) & set(with_help[i][1])) > 0:
    i += 1
with_help_max = with_help[0][0] + with_help[i][0]
with_help_range = [(pressure, path) for pressure, path in with_help if pressure >= with_help[i][0]]
for _i in range(len(with_help_range) - 1):
    for _j in range(_i + 1, len(with_help_range)):
        if len(set(with_help[_j][1]) & set(with_help[_i][1])) == 0:
            with_help_max = max(with_help_max, with_help[_i][0] + with_help[_j][0])

answer_a = max(pressures)
answer_b = with_help_max

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b