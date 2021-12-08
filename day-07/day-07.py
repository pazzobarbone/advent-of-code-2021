from pathlib import Path

this_file = Path(__file__)
with open(this_file.parent / "input.txt") as file:
    line = file.readline()

initial_positions = [int(p) for p in line.strip().split(",")]


def calculate_cost(initial_positions, cost_function):
    compact_positions = {}
    for p in initial_positions:
        if p not in compact_positions:
            compact_positions[p] = 1
        else:
            compact_positions[p] += 1

    cost = 0
    for end_position in range(max(initial_positions)):
        new_cost = 0
        for start_position in compact_positions.keys():
            new_cost += cost_function(start_position, end_position, compact_positions[start_position])
        if new_cost < cost or cost == 0:
            cost = new_cost
    return cost


def cost_function_part_1(start, end, n_of_submarines):
    return abs(start - end) * n_of_submarines


def cost_function_part_2(start, end, n_of_submarines):
    return sum(range(abs(start - end) + 1)) * n_of_submarines


#print(calculate_cost(initial_positions, cost_function_part_1))
#print(calculate_cost(initial_positions, cost_function_part_2))


# Median variant Part 1

initial_positions = sorted([int(p) for p in line.strip().split(",")])
initial_positions.sort()
N = len(initial_positions)
if N % 2 == 1:
    median_position = int((N + 2 - 1) / 2)
    median = initial_positions[median_position]
else:
    median_position = int(N / 2)
    median = int((initial_positions[median_position] + initial_positions[median_position + 1]) / 2)

target_position = median
cost = 0
for ship_position in initial_positions:
    cost += abs(ship_position - target_position)
print(cost)
