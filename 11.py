from aocd.models import Puzzle
from copy import deepcopy
import math
import numpy as np
import re

puzzle = Puzzle(year=2022, day=11)
data = puzzle.input_data

rx = re.compile(r'''
    Monkey\ (?P<id>\d+):\s*
      Starting\ items\:\ (?P<items>\d+(,\ \d+)*)\s*
      Operation\:\ new \ \=\ (?P<operation>.*)\s*
      Test\:\ divisible\ by\ (?P<test>\d+)\s*
        If\ true\:\ throw\ to\ monkey\ (?P<true>\d+)\s*
        If\ false\:\ throw\ to\ monkey\ (?P<false>\d+)
''', re.VERBOSE)

monkeys = { 
    int(m.group("id")): {
        "items": list(np.array(m.group("items").split(",")).astype(int)),
        "operation": m.group("operation"),
        "test": int(m.group("test")),
        "to": m.group("true") + " if new % " + m.group("test") + " == 0 else " + m.group('false')
    } for m in rx.finditer(data)
}

def predict(monkeys, iterations, mod=1):
    lcm = math.prod([monkey["test"] for monkey in monkeys.values()])
    stats = [0 for i in range(len(monkeys))]
    for _ in range(iterations):
        for id, monkey in monkeys.items():
            stats[id] += len(monkey["items"])
            while len(monkey["items"]) > 0:
                old = monkey["items"].pop()
                new = int(eval(monkey["operation"])) // mod
                monkeys[eval(monkey["to"])]["items"].append(new % lcm)
    return math.prod(sorted(stats)[-2:])

answer_a = predict(deepcopy(monkeys), iterations=20, mod=3)
answer_b = predict(deepcopy(monkeys), iterations=10000)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b