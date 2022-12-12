from aocd.models import Puzzle
from copy import deepcopy

puzzle = Puzzle(year=2022, day=5)
data = [item.splitlines() for item in puzzle.input_data.split("\n\n")]

containers_data = [[]*3 for i in range(len(data[0][-1])//4+1)]
for line in data[0]:
    for i in range(len(line)):
        if "A" <= line[i] <= "Z":
            containers_data[i//4].insert(0, line[i])

actions_data = []
for line in data[1]:
    line = line.split()
    actions_data.append((int(line[1]), int(line[3]) - 1, int(line[5]) - 1))

def move_one(containers, actions):
    containers = deepcopy(containers)
    for action in actions:
        (_repeat, _from, _to) = action
        for i in range(_repeat):
            container = containers[_from].pop()
            containers[_to].append(container)
    return containers

def move_batch(containers, actions):
    containers = deepcopy(containers)
    for action in actions:
        (_batch, _from, _to) = action
        batch = containers[_from][-_batch:]
        containers[_from] = containers[_from][:-_batch]
        containers[_to] += batch
    return containers

def top(containers):
    return ''.join([container[-1] for container in containers])

answer_a = top(move_one(containers=containers_data, actions=actions_data))
answer_b = top(move_batch(containers=containers_data, actions=actions_data))

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b