from data.day8_data import *
import numpy as np


def part1(data):
    data = np.asarray([[x for x in y] for y in data.split("\n")], dtype=int)
    # All outside trees ok
    num = 2 * data.shape[0] + 2 * (data.shape[1] - 2)
    for i in range(1, data.shape[0] - 1):
        line = []
        for j in range(1, data.shape[1] - 1):
            val = data[i][j]
            visible = any([
                data[i, :j].max() < val,
                data[i, j+1:].max() < val,
                data[:i, j].max() < val,
                data[i+1:, j].max() < val,
            ])
            if visible:
                num += 1
            line.append(val)
    print(num)


part1(test_data)
part1(input_data)


def part2(data):
    data = np.asarray([[x for x in y] for y in data.split("\n")], dtype=int)
    # print(data)
    # All outside trees ok
    scores = []
    for i in range(1, data.shape[0] - 1):
        for j in range(1, data.shape[1] - 1):
            val = data[i][j]
            visible = [
                [np.where(data[i, :j][::-1] >= val), j],
                [np.where(data[i, j+1:] >= val), data.shape[1] - j - 1],
                [np.where(data[:i, j][::-1] >= val), i],
                [np.where(data[i+1:, j] >= val), data.shape[0] - i - 1],
            ]
            num_visible = []
            for x, default in visible:
                try:
                    y = x[0][0] + 1
                except IndexError:
                    y = default
                num_visible.append(y)
            score = np.prod(num_visible)
            # print(val, num_visible, score)
            scores.append(score)
    print(max(scores))


part2(test_data)
part2(input_data)
