from pathlib import Path

this_file = Path(__file__)
with open(this_file.parent / "input.txt") as file:
    depth_measurements = list()
    for line in file.readlines():
        try:
            depth_measurements.append(int(line))
        except ValueError:
            break

i = 0
increments = 0
while i < len(depth_measurements) - 1:
    dep0 = depth_measurements[i]
    dep1 = depth_measurements[i + 1]
    if dep1 > dep0:
        increments += 1
    i += 1
print(increments)

i = 0
win_size = 3
increments = 0
while i + win_size < len(depth_measurements):
    sum0 = sum(depth_measurements[i : i + win_size])
    sum1 = sum(depth_measurements[i + 1 : i + 1 + win_size])
    if sum1 > sum0:
        increments += 1
    i += 1
print(increments)
