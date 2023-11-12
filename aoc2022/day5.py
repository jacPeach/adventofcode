from data.day5_data import *


def part1(data):
    instructions = [x for x in data.split("\n\n")[1].split("\n")]
    data = [x[1::4] for x in reversed(data.split("\n\n")[0].split("\n"))]
    names, data = data[0], data[1:]
    state = {name: [] for name in names}
    for row in data:
        for name, box in zip(names, row):
            if box != " ":
                state[name].append(box)
    for line in instructions:
        _, num, _, f, _, t = line.split()
        num = int(num)
        state[t].extend(state[f][-num:][::-1])
        state[f] = state[f][:-num]
    print("".join([state[name][-1] for name in names]))


part1(test_data)
part1(input_data)


def part2(data):
    instructions = [x for x in data.split("\n\n")[1].split("\n")]
    data = [x[1::4] for x in reversed(data.split("\n\n")[0].split("\n"))]
    names, data = data[0], data[1:]
    state = {name: [] for name in names}
    for row in data:
        for name, box in zip(names, row):
            if box != " ":
                state[name].append(box)
    for line in instructions:
        _, num, _, f, _, t = line.split()
        num = int(num)
        state[t].extend(state[f][-num:])
        state[f] = state[f][:-num]
    print("".join([state[name][-1] for name in names]))


part2(test_data)
part2(input_data)
