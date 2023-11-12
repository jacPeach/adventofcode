from tqdm import tqdm
from data.day11_data import *


def parse_data_part1(data):
    monkeys = {}

    monkey = 0
    current_data = {}
    for line in data.split("\n"):
        line = line.strip()
        if line.startswith("Monkey"):
            monkey = int(line.split()[1][:-1])
            current_data["inspections"] = 0
        elif line.startswith("Starting items"):
            current_data["items"] = [
                int(x) for x in line.split(": ")[1].split(", ")
            ]
        elif line.startswith("Operation"):
            current_data["inspection"] = lambda old, f=line.split(" = ")[
                1]: eval(f)
        elif line.startswith("Test"):
            current_data["test"] = lambda x, val=line.split(" by ")[1]: (
                x % int(val)) == 0
        elif line.startswith("If true"):
            current_data["true"] = int(line.split(" to monkey ")[1])
        elif line.startswith("If false"):
            current_data["false"] = int(line.split(" to monkey ")[1])

            monkeys[monkey] = current_data
            current_data = {}

    return monkeys


def print_monkeys(monkeys):
    for monkey in monkeys:
        print(f"{monkey=}")
        for k, v in monkeys[monkey].items():
            print(f"{k} = {v}")
        print()


def get_monkey_business(monkeys):
    counts = []
    for monkey in monkeys:
        counts.append(monkeys[monkey].get("inspections", 0))
    top = sorted(counts, reverse=True)[:2]
    print(f"Shenanigans = {top[0] * top[1]}")


def part1(data, rounds=20, verbose=False):
    monkeys = parse_data_part1(data)
    if verbose:
        print_monkeys(monkeys)
    num_monkeys = len(monkeys)

    for round in range(rounds):
        for monkey in range(num_monkeys):
            d = monkeys[monkey]
            monkeys[monkey]["inspections"] += len(d["items"])
            for item in d["items"]:
                worry = d["inspection"](item) // 3
                if d["test"](worry):
                    monkeys[d["true"]]["items"].append(worry)
                else:
                    monkeys[d["false"]]["items"].append(worry)
            monkeys[monkey]["items"] = []
        if verbose:
            print(f"Round {round}")
            print_monkeys(monkeys)
    get_monkey_business(monkeys)


part1(test_data, rounds=20)
part1(input_data)


class Item:
    def __init__(self, val, factors):
        self.vals = [val % factor for factor in factors]
        self.factors = factors

    def __str__(self):
        return f"Item({self.vals})"

    def __repr__(self) -> str:
        return self.__str__()

    def update(self, func):
        self.vals = [
            func(val) % factor for val, factor in zip(self.vals, self.factors)
        ]

    def test(self, factor):
        idx = self.factors.index(factor)
        return self.vals[idx] == 0


def parse_data_part2(data):
    monkeys = {}

    monkey = 0
    current_data = {}
    for line in data.split("\n"):
        line = line.strip()
        if line.startswith("Monkey"):
            monkey = int(line.split()[1][:-1])
            current_data["inspections"] = 0
        elif line.startswith("Starting items"):
            current_data["items"] = [
                int(x) for x in line.split(": ")[1].split(", ")
            ]
        elif line.startswith("Operation"):
            current_data["inspection"] = lambda old, f=line.split(" = ")[
                1]: eval(f)
        elif line.startswith("Test"):
            current_data["test"] = lambda x, val=line.split(" by ")[1]: (
                x % int(val)) == 0
            current_data["factor"] = int(line.split(" by ")[1])
        elif line.startswith("If true"):
            current_data["true"] = int(line.split(" to monkey ")[1])
        elif line.startswith("If false"):
            current_data["false"] = int(line.split(" to monkey ")[1])

            monkeys[monkey] = current_data
            current_data = {}

    # Reduce numbers
    factors = [monkey["factor"] for monkey in monkeys.values()]
    for monkey in monkeys:
        monkeys[monkey]["items"] = [
            Item(val, factors) for val in monkeys[monkey]["items"]
        ]

    return monkeys


def part2(data, rounds=10000, verbose=False):
    monkeys = parse_data_part2(data)
    if verbose:
        print_monkeys(monkeys)
    num_monkeys = len(monkeys)

    for round in tqdm(range(rounds)):
        for monkey in range(num_monkeys):
            d = monkeys[monkey]
            monkeys[monkey]["inspections"] += len(d["items"])
            for item in d["items"]:
                item.update(d["inspection"])
                if item.test(d["factor"]):
                    monkeys[d["true"]]["items"].append(item)
                else:
                    monkeys[d["false"]]["items"].append(item)
            monkeys[monkey]["items"] = []
        if verbose:
            print(f"Round {round}")
            print_monkeys(monkeys)
    get_monkey_business(monkeys)


part2(test_data)
part2(input_data)
