from data.day3_data import *


def calc_ord_score(c) -> int:
    p = ord(c) - ord("A") + 1
    if p > 26:
        p -= (ord("a") - ord("A"))
    else:
        p += 26
    return p


def part1(data):
    data = data.split("\n")
    priority = 0
    for line in data:
        a, b = line[:len(line)//2], line[-len(line)//2:]
        intersection = list(set(a).intersection(set(b)))
        if len(intersection) != 1:
            raise ValueError("Wrong lengths")
        c = intersection[0]
        priority += calc_ord_score(c)
    print(priority)


part1(test_data)
part1(input_data)


def part2(data):
    data = data.split("\n")
    priority = 0
    for i in range(0, len(data), 3):
        a, b, c = data[i:i+3]
        intersection = list(set(a).intersection(set(b)).intersection(set(c)))
        if len(intersection) != 1:
            raise ValueError("Wrong lengths")
        c = intersection[0]
        priority += calc_ord_score(c)
    print(priority)


part2(test_data)
part2(input_data)
