from collections import defaultdict
from data.day12_data import *
import numpy as np
import heapq


class Grid:
    def __init__(self, grid, start, end):
        self.grid = grid
        self.start_idx = start
        self.end_idx = end

    def get_neighbours(self, idx):
        neighbours = [
            (idx[0] + 1, idx[1]),
            (idx[0] - 1, idx[1]),
            (idx[0], idx[1] + 1),
            (idx[0], idx[1] - 1)
        ]
        return [
            x for x in neighbours if
            all(y >= 0 for y in x)
            and x[0] < self.grid.shape[0]
            and x[1] < self.grid.shape[1]
            and (self.grid[x] - self.grid[idx]) <= 1
        ]

    def d_func(self, idx1: np.array, idx2: np.array) -> int:
        return np.sum(np.abs(np.array(idx2) - np.array(idx1)))

    def h_func(self, idx: np.array):
        return self.d_func(idx, self.end_idx)

    def get_start_positions(self):
        return np.argwhere(self.grid == np.min(self.grid))


def parse_data(data: str) -> Grid:
    start_idx = data.replace("\n", "").index("S")
    end_idx = data.replace("\n", "").index("E")
    data = data.replace("S", "a").replace("E", "z")
    grid = np.asarray([[ord(x) - ord("a") for x in row]
                      for row in data.split("\n")], dtype=int)

    start_idx = np.unravel_index(start_idx, grid.shape)
    end_idx = np.unravel_index(end_idx, grid.shape)

    return Grid(grid, start_idx, end_idx)


def reconstruct_path(previous, current):
    path = [current]
    while current in previous:
        current = previous[current]
        path.insert(0, current)
    return path


def a_star(grid: Grid) -> list:

    start = grid.start_idx
    queue = [(0, start)]
    heapq.heapify(queue)
    previous = {}
    g_scores = defaultdict(lambda: np.inf, {start: 0})
    f_scores = defaultdict(lambda: np.inf, {start: grid.h_func(start)})

    while len(queue) > 0:
        g_score, current_node = heapq.heappop(queue)
        if current_node == grid.end_idx:
            return reconstruct_path(previous, current_node)
        for neighbour in grid.get_neighbours(current_node):
            test_g_score = g_score + grid.d_func(current_node, neighbour)
            if test_g_score < g_scores[neighbour]:
                previous[neighbour] = current_node
                g_scores[neighbour] = test_g_score
                f_scores[neighbour] = test_g_score + grid.h_func(neighbour)
                heapq.heappush(queue, (f_scores[neighbour], neighbour))
    return None


def part1(data):
    grid = parse_data(data)
    path = a_star(grid)

    print(len(path) - 1)


part1(test_data)
part1(input_data)


def part2(data):
    grid = parse_data(data)
    best_path = np.inf
    for start in grid.get_start_positions():
        grid.start_idx = tuple(start)
        path = a_star(grid)
        if path and len(path) - 1 < best_path:
            best_path = len(path) - 1
            print(start, best_path)


part2(test_data)
part2(input_data)
