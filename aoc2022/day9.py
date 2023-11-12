from data.day9_data import *
import numpy as np


def part1(data, verbose=False):
    data = data.split("\n")
    h = t = np.array((0, 0))
    visited = set([tuple(t)])
    if verbose:
        print(h, t)
    for line in data:
        direction, num_moves = line.split()
        d = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}[direction]
        if verbose:
            print(direction, num_moves)
        for _ in range(int(num_moves)):
            new_h = h + d
            if int(np.sqrt(sum((new_h - t) ** 2))) > 1:
                t = h
            h = new_h
            if verbose:
                print(h, t)
            visited.add(tuple(t))
    if verbose:
        print(visited)
    print(len(visited))


part1(test_data)
part1(input_data)


def sim_knot_movement(head, tail, movement, move_head: bool):
    new_h = head + movement if move_head else head
    new_tail = tail
    # Diagonal
    dist = int(np.sqrt(sum((new_h - tail) ** 2)))
    # print(dist)
    if np.sqrt(sum(movement ** 2)) > 1 and dist > 1:
        if new_h[0] == tail[0]:
            movement[0] = 0
        if new_h[1] == tail[1]:
            movement[1] = 0
        new_tail = tail + movement
    # Non-diadgonal
    elif dist > 1:
        new_tail = head
    return new_h, new_tail


def print_rope(rope, shape=(6, 6), offset=(0, 0)):
    a = np.zeros(shape)
    for i, coord in enumerate(reversed(rope)):
        # print(coord)
        num = len(rope) - i
        a[coord[0]+offset[0], coord[1]+offset[1]] = num
    for row in reversed(range(a.shape[0])):
        print(" ".join([str(int(x)) if x != 0 else "." for x in a.T[row]]))
    print()


def part2(data, board_shape=(10, 10), start_pos=(0, 0), length=2, verbose=False):
    data = data.split("\n")
    rope = np.zeros((length, 2), dtype=int)
    visited = set([tuple(x) for x in rope[1:]])
    if verbose:
        print(rope)
    for line in data:
        direction, num_moves = line.split()
        head_d = {"R": np.array([1, 0]), "U": np.array([0, 1]), "L": np.array(
            [-1, 0]), "D": np.array([0, -1])}[direction]
        if verbose:
            print(direction, num_moves)
            print(visited)
        for _ in range(int(num_moves)):
            d = head_d
            move = True
            for idx in range(1, rope.shape[0]):
                head, tail = rope[idx - 1].copy(), rope[idx].copy()
                if not move:
                    head -= d
                # print(idx, head, tail, d, move)

                new_head, new_tail = sim_knot_movement(
                    head, tail, d, move_head=True)
                # print(new_head, new_tail, d)
                rope[idx - 1] = new_head
                rope[idx] = new_tail
                # print(rope[idx - 1], rope[idx])
                # Check if the next one needs to move
                d = new_tail - tail
                move = False
                # print(d)
                if sum(np.absolute(d)) == 0:
                    break
            visited.add(tuple(rope[-1]))

            if verbose:
                print_rope(rope, shape=board_shape, offset=start_pos)
                # print(f"{rope}")
    if verbose:
        print(visited)
    print(len(visited))


# track_rope(test_data, length=5, verbose=True, board_shape=(6, 6), start_pos=(0, 0))
# track_rope(test_data_2, length=10, verbose=True, board_shape=(30, 30), start_pos=(12, 12))
part2(test_data, length=10)
part2(test_data_2, length=10)
part2(input_data, length=10)
