from data.day4_data import *


def part1(data):
    data = [x.split(",") for x in data.split("\n")]
    num = 0
    for a, b in data:
        a = set(range(int(a.split("-")[0]), int(a.split("-")[1]) + 1))
        b = set(range(int(b.split("-")[0]), int(b.split("-")[1]) + 1))
        overlap = a.intersection(b)
        if len(overlap) == len(a) or len(overlap) == len(b):
            num += 1
    print(num)


part1(test_data)
part1(input_data)


def part2(data):
    data = [x.split(",") for x in data.split("\n")]
    num = 0
    for a, b in data:
        a = set(range(int(a.split("-")[0]), int(a.split("-")[1]) + 1))
        b = set(range(int(b.split("-")[0]), int(b.split("-")[1]) + 1))
        overlap = a.intersection(b)
        if len(overlap) > 0:
            num += 1
    print(num)


part2(test_data)
part2(input_data)
