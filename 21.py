from aocd.models import Puzzle
import re
from copy import deepcopy

puzzle = Puzzle(year=2022, day=21)
data = puzzle.input_data

rx_node = re.compile(r"^(?P<id>\w{4}):\s(?P<left>\w{4})\s(?P<op>[\+\-\*\/])\s(?P<right>\w{4})$", re.MULTILINE)
rx_leaf = re.compile(r"^(?P<id>\w{4}):\s(?P<number>\d+)$", re.MULTILINE)
operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}

def build_tree(nodes, root="root", humn=None):
    tree = nodes.pop(root)
    if type(tree) is dict:
        for child in ["left", "right"]:
            if type(tree[child]) is not complex and tree[child] in nodes:
                tree[child] = build_tree(nodes=nodes, root=tree[child], humn=humn) if humn is None or tree[child] != "humn" else humn
    return tree

def calculate(tree):
    left = tree["left"] if type(tree["left"]) is complex else calculate(tree["left"])
    right = tree["right"] if type(tree["right"]) is complex else calculate(tree["right"])
    return operators[tree["op"]](left, right)

nodes = { m.group("id"): { "left": m.group("left"), "right": m.group("right"), "op": m.group("op") } for m in rx_node.finditer(data) }
nodes.update({ m.group("id"): complex(m.group("number")) for m in rx_leaf.finditer(data) })

expression = build_tree(nodes=deepcopy(nodes))
equation = build_tree(nodes=deepcopy(nodes), humn=1j)
equation = calculate(equation["left"]) - calculate(equation["right"])

answer_a = int(calculate(expression).real)
answer_b = int(equation.real / -equation.imag)

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b