from aocd.models import Puzzle
import re
import time

start = time.time()

puzzle = Puzzle(year=2022, day=19)
data = puzzle.input_data

rx = re.compile(r"\s(?P<id>\d+):.*\s(?P<ore_ore>\d+)\s.*\s(?P<clay_ore>\d+)\s.*\s(?P<obsidian_ore>\d+)\s.*\s(?P<obsidian_clay>\d+)\s.*\s(?P<geode_ore>\d+)\s.*\s(?P<geode_obsidian>\d+)\s", re.VERBOSE)
blueprints = {
    int(m.group("id")): {
        0: { 3: int(m.group("geode_ore")), 1: int(m.group("geode_obsidian")) },
        1: { 3: int(m.group("obsidian_ore")), 2: int(m.group("obsidian_clay")) },
        2: { 3: int(m.group("clay_ore")) },
        3: { 3: int(m.group("ore_ore")) }
    } for m in rx.finditer(data) 
}

def can_build(robot, blueprint, resources):
    return all([amount <= resources[resource] for resource, amount in blueprint[robot].items()])

def build(robot, blueprint, resources, robots):
    resources = resources.copy()
    for resource in range(4):
        if resource in blueprint[robot]:
            resources[resource] -= blueprint[robot][resource]
        resources[resource] += robots[resource]
    robots = robots.copy()
    robots[robot] += 1
    return resources, robots

def wait(resources, robots):
    resources = resources.copy()
    for resource in range(4):
        resources[resource] += robots[resource]
    return resources, robots.copy()

def check_quality(blueprint, time, cut):
    states = [([0, 0, 0, 0], [0, 0, 0, 1])]
    while time > 0:
        new = []
        for resources, robots in states:
            should_wait = not can_build(robot=0, blueprint=blueprint, resources=resources)
            robots_check = [0]
            if min(resources[1], robots[1]) < blueprint[0][1]:
                robots_check.append(1)
            if min(resources[2], robots[2]) < blueprint[1][2]:
                robots_check.append(2)
            if min(resources[3], robots[3]) < max(blueprint[0][3], blueprint[1][3], blueprint[2][3], blueprint[3][3]):
                robots_check.append(3)
            for robot in robots_check:
                if can_build(robot=robot, blueprint=blueprint, resources=resources):
                    state = build(robot=robot, blueprint=blueprint, resources=resources, robots=robots)
                    if state not in new:
                        new.append(state)
            if should_wait:
                after_wait = wait(resources=resources, robots=robots)
                if after_wait not in new:
                    new.append(after_wait)
        max_geode = max([state[0][0] for state in new])
        new = [state for state in new if max_geode - state[0][0] < 2]
        states = sorted(new, key=lambda x: tuple(i + j for i, j in zip(x[0], x[1])))[-cut:]
        time -= 1
    return sorted(states, key=lambda x: x[0][0])[-1][0][0]

quality_a = 0
quality_b = 1
for i, blueprint in blueprints.items():
    quality_a += i * check_quality(blueprint=blueprint, time=24, cut=100)
    if i < 4:
        quality_b *= check_quality(blueprint=blueprint, time=32, cut=1200)

answer_a = quality_a
answer_b = quality_b

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b