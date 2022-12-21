from aocd.models import Puzzle
import re
from copy import deepcopy

puzzle = Puzzle(year=2022, day=21)
data = puzzle.input_data

rx_node = re.compile(r"^(?P<id>\w{4}):\s(?P<left>\w{4})\s(?P<op>[\+\-\*\/])\s(?P<right>\w{4})$", re.MULTILINE)
rx_leaf = re.compile(r"^(?P<id>\w{4}):\s(?P<number>\d+)$", re.MULTILINE)
operators = {
    "+": lambda x, y: int(x + y),
    "-": lambda x, y: int(x - y),
    "*": lambda x, y: int(x * y),
    "/": lambda x, y: int(x / y)
}

def build_tree(nodes, leafs, root="root", humn=None):
    tree = nodes.pop(root)
    for child in ["left", "right"]:
        if not child.isdigit():
            if tree[child] in nodes:
                tree[child] = build_tree(nodes=nodes, leafs=leafs, root=tree[child], humn=humn)
            elif tree[child] in leafs:
                if humn is not None and tree[child] == "humn":
                    tree[child] = humn
                else:
                    tree[child] = leafs.pop(tree[child])
    return tree

def calculate(tree):
    left = tree["left"] if type(tree["left"]) == int else calculate(tree["left"])
    right = tree["right"] if type(tree["right"]) == int else calculate(tree["right"])
    return operators[tree["op"]](left, right)

nodes = { m.group("id"): { "left": m.group("left"), "right": m.group("right"), "op": m.group("op") } for m in rx_node.finditer(data) }
leafs = { m.group("id"): int(m.group("number")) for m in rx_leaf.finditer(data) }
tree = build_tree(nodes=deepcopy(nodes), leafs=deepcopy(leafs))

cycle_length = 150
equation = build_tree(nodes=deepcopy(nodes), leafs=deepcopy(leafs), humn=0)
l1, r1 = calculate(equation['left']), calculate(equation['right'])
equation = build_tree(nodes=deepcopy(nodes), leafs=deepcopy(leafs), humn=cycle_length)
l2, r2 = calculate(equation['left']), calculate(equation['right'])
diff, x, value = (abs(l2 - l1), "left", r1) if r1 == r2 else (abs(r2 - r1), "right", l1)
iterations = abs(l1 - r1) // diff
for i in range(cycle_length):
    humn = cycle_length * iterations + i
    equation = build_tree(nodes=deepcopy(nodes), leafs=deepcopy(leafs), root=nodes["root"][x], humn=humn)
    if calculate(equation) == value:
        break

answer_a = calculate(tree)
answer_b = humn

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b