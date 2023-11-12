from data.day14_data import *
import numpy as np

EMPTY = 0
BLOCK = 1
SAND = 2
FINISHED_SOURCE = 3
SOURCE = 4


def parse_data(data):
    lines = []
    for idxa in data.split("\n"):
        for coord in idxa.split(" -> "):
            lines.append(tuple([int(x) for x in coord.split(",")]))
    data = [
        [
            tuple([int(x) for x in coord.split(",")])
            for coord in line.split(" -> ")
        ] for line in data.split("\n")
    ]
    ymin = 0
    ymax = max([x[1] for x in lines]) + 1
    xmin = min([x[0] for x in lines])
    xmax = max([x[0] for x in lines]) + 1
    offset = xmin

    shape = (xmax - offset, ymax - ymin)
    grid = np.zeros(shape, dtype=int)

    for row in data:
        for i, idxa in enumerate(row[:-1]):
            idxb = row[i+1]
            # May need to rewrite
            if any([x == y for x, y in zip(idxa, idxb)]):
                idx = sorted([idxa, idxb])
                grid[
                    idx[0][0]-offset:idx[1][0]+1-offset,
                    idx[0][1]:idx[1][1]+1
                ] = BLOCK

    grid[500-offset, 0] = SOURCE

    return grid, offset


def print_grid(grid):
    for row in range(grid.shape[1]):
        print_row = ""
        for col in range(grid.shape[0]):
            val = grid[col][row]
            print_val = ""
            if val == EMPTY:
                print_val = "."
            elif val == BLOCK:
                print_val = "#"
            elif val == SAND:
                print_val = "o"
            elif val == FINISHED_SOURCE:
                print_val = "~"
            elif val == SOURCE:
                print_val = "+"
            else:
                print("error")
            print_row += print_val
        print(print_row)


def sand_fall(grid, sand, expand=False):
    col = grid[sand[0], sand[1]+1:]
    if len(col) == 0:
        return None
    try:
        landing_spot = (sand[0], np.argwhere(col > EMPTY)[0][0] + sand[1])
    except IndexError:
        landing_spot = sand
    return sand_slide(grid, landing_spot, expand=expand)


def sand_slide(grid, sand, expand=False):
    next_y = sand[1]+1
    left = (sand[0]-1, next_y)
    right = (sand[0]+1, next_y)
    try:
        if grid[left] == EMPTY:
            return left
        if grid[right] == EMPTY:
            return right
    except IndexError as e:
        if expand:
            idx = int(e.args[0].split()[1])
            return (idx, next_y)
        return None
    return sand


def add_flow(grid, sand_idx):
    grid[tuple(sand_idx)] = FINISHED_SOURCE
    return grid


def sim_sand(grid, expand=False):
    sand_idx = np.argwhere(grid == SOURCE)[0]
    next_idx = sand_fall(grid, sand_idx)
    while not all([x == y for x, y in zip(sand_idx, next_idx)]):
        sand_idx = next_idx
        next_idx = sand_fall(grid, sand_idx, expand=expand)
        if next_idx is None:
            return add_flow(grid, np.argwhere(grid == SOURCE)[0])
        elif next_idx[0] < 0:
            next_idx = (0, next_idx[1])
            grid = np.pad(grid, ((3, 0), (0, 0)), constant_values=EMPTY)
        elif next_idx[0] >= grid.shape[0]:
            grid = np.pad(grid, ((0, 3), (0, 0)), constant_values=EMPTY)
        grid[:, -1] = BLOCK
    print(sand_idx)
    grid[sand_idx] = SAND
    return grid


def part1(data, rounds=None, verbose=True):
    grid, offset = parse_data(data)
    if verbose:
        print_grid(grid)
    if rounds is not None:
        for i in range(rounds):
            grid = sim_sand(grid)
            if verbose:
                print_grid(grid)
    else:
        while np.count_nonzero(grid == FINISHED_SOURCE) == 0:
            grid = sim_sand(grid)
        if verbose:
            print_grid(grid)
    print(np.count_nonzero(grid == SAND))


# part1(test_data)
# part1(input_data, verbose=False)


def add_bottom(grid):
    buffer_amount = (
        # Left / Right
        (0, 0),
        # Top / Bottom
        (0, 2)
    )
    grid = np.pad(grid, buffer_amount, constant_values=EMPTY)
    grid[:, -1] = BLOCK
    return grid


def part2(data, rounds=None, verbose=True):
    grid, offset = parse_data(data)
    grid = add_bottom(grid)
    if verbose:
        print_grid(grid)
    if rounds is not None:
        for i in range(rounds):
            grid = sim_sand(grid, expand=True)
            if verbose:
                print_grid(grid)
    else:
        while np.count_nonzero(grid == 3) == 0:
            grid = sim_sand(grid, expand=True)
        if verbose:
            print_grid(grid)
    print(np.count_nonzero(grid == 2))


part2(test_data)
