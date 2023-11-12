from data.day6_data import *


def part1(data):
    # Assumes one marker is guaranteed
    for i in range(len(data)):
        if len(set(data[i:i+4])) == 4:
            break
    print(i + 4)


part1(test_data)
part1(input_data)


def part2(data, marker_size):
    # Assumes one marker is guaranteed
    for i in range(len(data)):
        if len(set(data[i:i+marker_size])) == marker_size:
            break
    print(i + marker_size)


part2(test_data)
part2(input_data, 14)
