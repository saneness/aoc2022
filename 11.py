from aocd.models import Puzzle
from copy import deepcopy
import math
import numpy as np
import re

puzzle = Puzzle(year=2022, day=11)
data = puzzle.input_data

rx = re.compile(r'''
    Monkey\ (?P<id>\d+):\s*
      Starting\ items\:\ *(?P<items>\d*(,\ \d+)*)\s*
      Operation\:\ new \ \=\ (?P<operation>(old|\d+)\s[\+\-\*\/]\s(old|\d+))\s*
      Test\:\ divisible\ by\ (?P<test>\d+)\s*
        If\ true\:\ throw\ to\ monkey\ (?P<true>\d+)\s*
        If\ false\:\ throw\ to\ monkey\ (?P<false>\d+)
''', re.VERBOSE)

monkeys = { 
    int(m.group("id")): {
        "items": list(np.array(m.group("items").split(",") if len(m.group("items")) > 0 else []).astype(int)),
        "operation": m.group("operation"),
        "test": int(m.group("test")),
        "to": m.group("true") + " if new % " + m.group("test") + " == 0 else " + m.group('false')
    } for m in rx.finditer(data)
}

def predict(players, iterations, mod=1):
    players = deepcopy(players)
    lcm = math.prod([player["test"] for player in players.values()])
    stats = [0 for i in range(len(players))]
    for _ in range(iterations):
        for id, player in players.items():
            stats[id] += len(player["items"])
            while len(player["items"]) > 0:
                old = player["items"].pop()
                new = int(eval(player["operation"])) // mod
                players[eval(player["to"])]["items"].append(new % lcm)

    return math.prod(sorted(stats)[-2:])

answer_a = predict(players=monkeys, iterations=20, mod=3)
answer_b = predict(players=monkeys, iterations=10000)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b