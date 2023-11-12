from data.day15_data import test_data, input_data
import re


def part1(data, line_num=10, verbose=False):
    sensors = {}
    beacons = []
    for line in data.split("\n"):
        x = re.findall(r"x=-?(\d+)", line)
        y = re.findall(r"y=-?(\d+)", line)
        sensor = int(x[0]), int(y[0])
        beacon = int(x[1]), int(y[1])
        distance = sum([abs(sensor[0] - beacon[0]),
                       abs(sensor[1] - beacon[1])])
        sensors[sensor] = distance
        beacons.append(beacon)
    beacons = set(beacons)

    # Overlap points
    xs = []
    for sensor, beacon_dist in sensors.items():
        x, y = sensor
        line_dist = abs(y - line_num)
        if line_dist < beacon_dist:
            # Number of points on the line that would overlap
            x_size = beacon_dist - line_dist
            xs_sensor = range(x - x_size, x + x_size + 1)
            if verbose:
                print(sensor, beacon_dist)
                print(line_dist, x_size)
                print(xs_sensor)
            xs.extend(xs_sensor)

    if verbose:
        print(sensors)
    print(len(set(xs)) - len([x for x in beacons if x[1] == line_num]))


part1(test_data, line_num=10)
part1(input_data, line_num=2000000)


def part2(data, line_num=4000000, verbose=False):
    sensors = {}
    beacons = []
    for line in data.split("\n"):
        x = re.findall(r"x=-?(\d+)", line)
        y = re.findall(r"y=-?(\d+)", line)
        sensor = int(x[0]), int(y[0])
        beacon = int(x[1]), int(y[1])
        distance = sum([abs(sensor[0] - beacon[0]),
                       abs(sensor[1] - beacon[1])])
        sensors[sensor] = distance
        beacons.append(beacon)
    beacons = set(beacons)

    # Overlap points
    for line in range(line_num):
        xs = []
        for sensor, beacon_dist in sensors.items():
            x, y = sensor
            line_dist = abs(y - line)
            if line_dist < beacon_dist:
                # Number of points on the line that would overlap
                x_size = beacon_dist - line_dist
                xs_sensor = range(x - x_size, x + x_size + 1)
                if verbose:
                    print(sensor, beacon_dist)
                    print(line_dist, x_size)
                    print(xs_sensor)
                xs.extend(xs_sensor)

        if verbose:
            print(sensors)
        spaces = sorted([x for x in set(xs) if x >= 0 and x <= line_num])
        print(line, spaces)
        # if spaces != 0:
        #     print(line, spaces)


part1(test_data, line_num=11)
part2(test_data, line_num=20)
