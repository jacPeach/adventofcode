from itertools import zip_longest
from functools import cmp_to_key
from data.day13_data import *


def parse_data(data):
    return [
        [eval(line) for line in pair.split("\n")]
        for pair in data.split("\n\n")
    ]


def right_order(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return "equal"
        return a < b

    else:
        if isinstance(a, list) and isinstance(b, int):
            b = [b]
            if len(a) == 0:
                a = [0]
        elif isinstance(a, int) and isinstance(b, list):
            a = [a]
            if len(b) == 0:
                b = [0]
        for sub_a, sub_b in zip_longest(a, b, fillvalue=-1):
            order = right_order(sub_a, sub_b)
            if order != "equal":
                return order
        return "equal"
    # return True


def part1(data, verbose=False):
    data = parse_data(data)
    packets = []
    for i, pair in enumerate(data):
        a, b = pair
        order = right_order(a, b)
        if verbose:
            print(a)
            print(b)
            print(order)
        if order:
            packets.append(i + 1)

    print(sum(packets))


part1(test_data_1)
part1(test_data)
part1(input_data)


def sort_key(a, b):
    return -1 if right_order(a, b) else 1


def part2(data, verbose=False):
    data = parse_data(data)
    packets = [y for x in data for y in x]
    key1 = [[2]]
    key2 = [[6]]
    packets += [key1, key2]
    packets.sort(key=cmp_to_key(sort_key))

    print((packets.index(key1) + 1) * (packets.index(key2) + 1))


part2(test_data)
part2(input_data)
