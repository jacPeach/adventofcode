from collections import defaultdict
import numpy as np
from data.day10_data import *


def check_strengths(check_cycles, cycle, strengths, verbose=False):
    if cycle + 1 in check_cycles:
        if verbose:
            print(cycle, strengths)
        return {k: v * (cycle + 1) for k, v in strengths.items()}
    return None


def part1(data, verbose=False):

    check_cycles = list(range(20, 221, 40))

    interesting_strengths = []

    instructions = [x.strip() for x in data.split("\n")]
    instruction = None
    cycle = 0
    buffer = defaultdict(list)
    strength = defaultdict(lambda: 1)
    has_items = True
    while has_items:
        cycle += 1
        if all([len(x) == 0 for x in buffer.values()]):
            if instruction is None:
                has_items = False
            try:
                instruction = instructions.pop(0)
                has_items = True
            except IndexError:
                instruction = None
            if instruction and instruction != "noop":
                register, val = instruction.split()
                register = register[-1]
                val = int(val)
                buffer[register].append(val)
        else:
            for register in buffer:
                val = 0
                if len(buffer[register]) > 0:
                    val = buffer[register].pop(0)
                    strength[register] += val

        s = check_strengths(check_cycles, cycle, strength, verbose)
        if s is not None:
            interesting_strengths.append(s)
        if verbose:
            print(cycle, dict(strength), dict(buffer))
    if verbose:
        print(interesting_strengths)
    print(sum([sum(x.values()) for x in interesting_strengths]))


part1(test_data_0)
part1(test_data)
part1(input_data)


def draw_pixel(screen, cycle, positions):
    register = "x"
    line_width = screen.shape[1]
    sprite_pos = positions[register]
    draw_pos = (cycle // line_width, cycle % line_width)
    if draw_pos[1] in [sprite_pos-1, sprite_pos, sprite_pos+1]:
        screen[draw_pos] = "#"

    return screen


def print_screen(screen):
    for x in range(screen.shape[0]):
        print("".join(screen[x, :]))


def part2(data, verbose=False, screen_shape=(6, 40)):

    screen = np.full(screen_shape, ".")

    instructions = [x.strip() for x in data.split("\n")]
    instruction = None
    cycle = 0
    buffer = defaultdict(list)
    strength = defaultdict(lambda: 1)
    has_items = True
    while has_items:
        cycle += 1
        if all([len(x) == 0 for x in buffer.values()]):
            if instruction is None:
                has_items = False
            try:
                instruction = instructions.pop(0)
                has_items = True
            except IndexError:
                instruction = None
            if instruction and instruction != "noop":
                register, val = instruction.split()
                register = register[-1]
                val = int(val)
                buffer[register].append(val)
        else:
            for register in buffer:
                val = 0
                if len(buffer[register]) > 0:
                    val = buffer[register].pop(0)
                    strength[register] += val

        draw_pixel(screen, cycle, strength)
        if verbose:
            print(cycle, dict(strength), dict(buffer))
    print_screen(screen)


part2(test_data)
part2(input_data)
