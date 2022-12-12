from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=7)
data = [line.split() for line in puzzle.input_data.splitlines()]

def get_parent(path):
    return "/".join(path.split("/")[:-2 if path[-1] == "/" else -1]) + "/"

files = {}
for line in data:
    if line[0] == "$" and line[1] == "cd":
        if line[2] == "/":
            directory = "/"
        elif line[2] == "..":
            directory = get_parent(directory)
        else:
            directory += line[2] + "/"
    elif line[0].isdigit():
        files.update({ directory + line[1]: int(line[0]) })

directories = {}
for name in files:
    parent = name
    while get_parent(parent) != parent:
        parent = get_parent(parent)
        directories.update({parent: directories.get(parent, 0) + files[name] })

used = sum(files.values()) - 40000000

answer_a = sum([directories[name] for name in directories if directories[name] <= 100000])
answer_b = sorted([directories[name] for name in directories if directories[name] >= used])[0]

puzzle.answer_a = answer_a
puzzle.answer_b = answer_b