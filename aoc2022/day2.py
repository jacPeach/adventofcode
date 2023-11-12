from data.day2_data import *


def part1(data):
    data = [x.split() for x in data.split("\n") if x.strip() != ""]
    score = 0
    for game in data:
        a, b = ord(game[0]) - ord("A") + 1, ord(game[1]) - ord("X") + 1
        score += b
        if (b - a == 1 and b > a) or b - a == -2:
            score += 6
        elif b == a:
            score += 3
    print(score)


part1(test_data)
part1(input_data)


def part2(data):
    data = [x.split() for x in data.split("\n") if x.strip() != ""]
    score = 0
    for game in data:
        a, res = ord(game[0]) - ord("A") + 1, ord(game[1]) - ord("X") + 1
        score += (res - 1) * 3
        if res == 3:
            b = (a + 1) % 4 or 1
        elif res == 2:
            b = a
        elif res == 1:
            b = (a - 1) % 4 or 3
        score += b
    print(score)


part2(test_data)
part2(input_data)
