from pathlib import Path
import numpy as np
from copy import deepcopy

this_file = Path(__file__)
with open(this_file.parent / "input.txt") as file:
    depth_measurements = list()
    lines = file.readlines()
    while True:
        try:
            lines.remove("\n")
        except ValueError:
            break
    digits = np.array([0] * len(lines[0].strip()))
    for line in lines:
        try:
            digits += np.array([int(d) for d in line.strip()])
        except ValueError:
            break

entries = len(lines)
most_common_bits = ["1" if d > entries / 2 else "0" for d in digits]
least_common_bits = ["0" if d == "1" else "1" for d in most_common_bits]
gamma_rate = int("".join(most_common_bits), 2)
epsilon_rate = int("".join(least_common_bits), 2)
power_consumption = gamma_rate * epsilon_rate
print(power_consumption)


def calculate_oxygen_generator_rating(data):
    def recursion(data, position):
        if len(data) == 1:
            position += 1
            return int(data[0].strip(), 2)
        else:
            digits = np.array([0] * len(data[0].strip()))
            for line in data:
                try:
                    digits += np.array([int(d) for d in line.strip()])
                except ValueError:
                    break

        entries = len(data)
        common_bit = "1" if digits[position] >= entries / 2 else "0"

        filtered_data = deepcopy(data)
        for line in data:
            if line[position] != common_bit:
                filtered_data.remove(line)
        position += 1
        return recursion(filtered_data, position)

    return recursion(data, 0)


def calculate_co2_rating(data):
    def recursion(data, position):
        if len(data) == 1:
            position += 1
            return int(data[0].strip(), 2)
        else:
            digits = np.array([0] * len(data[0].strip()))
            for line in data:
                try:
                    digits += np.array([int(d) for d in line.strip()])
                except ValueError:
                    break

        entries = len(data)
        common_bit = "0" if digits[position] >= entries / 2 else "1"

        filtered_data = deepcopy(data)
        for line in data:
            if line[position] != common_bit:
                filtered_data.remove(line)
        position += 1
        return recursion(filtered_data, position)

    return recursion(data, 0)


print(calculate_oxygen_generator_rating(lines) * calculate_co2_rating(lines))
