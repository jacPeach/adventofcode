from data.day7_data import *
from collections import defaultdict


def part1(data):
    data = [line.strip() for line in data.split("\n")]
    cdir = ("/", )
    tree = defaultdict(lambda: 0)
    for line in data:
        if line.startswith("$"):
            command = line.split()[1]
            if command == "cd":
                next_dir = line.split()[2]
                if next_dir == "..":
                    cdir = cdir[:-1]
                elif next_dir == "/":
                    cdir = ("/", )
                else:
                    cdir += (next_dir, )
        else:
            size, _ = line.split()
            try:
                size = int(size)
                tree[cdir] += size
            except ValueError:
                continue
    dirs = list(tree.keys())
    for cdir in dirs:
        for i in range(1, len(cdir)):
            prev_dir = cdir[:i]
            tree[prev_dir] += tree[cdir]
    print(sum(filter(lambda x: x < 100000, tree.values())))


part1(test_data)
part1(input_data)


def part2(data, total_size=70000000, required_size=30000000):
    data = [line.strip() for line in data.split("\n")]
    cdir = ("/", )
    tree = defaultdict(lambda: 0)
    for line in data:
        if line.startswith("$"):
            command = line.split()[1]
            if command == "cd":
                next_dir = line.split()[2]
                if next_dir == "..":
                    cdir = cdir[:-1]
                elif next_dir == "/":
                    cdir = ("/", )
                else:
                    cdir += (next_dir, )
        else:
            size, _ = line.split()
            try:
                size = int(size)
                tree[cdir] += size
            except ValueError:
                continue
    dirs = list(tree.keys())
    for cdir in dirs:
        for i in range(1, len(cdir)):
            prev_dir = cdir[:i]
            tree[prev_dir] += tree[cdir]
    free_space = total_size - tree[("/", )]
    delete_size = required_size - free_space
    print(sorted(filter(lambda x: x > delete_size, tree.values()))[0])


part2(test_data)
part2(input_data)
