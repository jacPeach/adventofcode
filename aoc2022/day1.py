from data.day1_data import *


def part1(data):
    elfs = [0]
    for line in data.split("\n"):
        if line.strip() == "":
            elfs.append(0)
        else:
            elfs[-1] += int(line)
    print(max(elfs))


part1(test_data)
part1(input_data)


def part2(data):
    elfs = [0]
    for line in data.split("\n"):
        if line.strip() == "":
            elfs.append(0)
        else:
            elfs[-1] += int(line)
    print(sum(sorted(elfs)[-3:]))


part2(test_data)
part2(input_data)
