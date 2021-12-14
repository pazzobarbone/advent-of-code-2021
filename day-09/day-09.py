from pathlib import Path
import numpy as np


def process_raw_line(line):
    return [int(n) for n in line.strip()]


lines = list()
this_file = Path(__file__)
with open(this_file.parent / "input.txt") as file:
    while True:
        line = process_raw_line(file.readline())
        if not line:
            break
        lines.append(line)

heigth_map = np.array(lines)

risk_level = 0
basins = list()
low_points = list()
for r in range(heigth_map.shape[0]):
    for c in range(heigth_map.shape[1]):
        neighbours = [
            heigth_map[r - 1 if r > 0 else r][c],
            heigth_map[r + 1 if r < heigth_map.shape[0] - 1 else r][c],
            heigth_map[r][c - 1 if c > 0 else c],
            heigth_map[r][c + 1 if c < heigth_map.shape[1] - 1 else c],
        ]
        # print(neighbours)
        if heigth_map[r][c] <= min(neighbours + [8]):
            risk_level += 1 + heigth_map[r][c]
            low_points.append((r, c))
print(risk_level)


def neighbours(point):
    global heigth_map
    r = point[0]
    c = point[1]
    return [
        (r - 1 if r > 0 else r, c),
        (r + 1 if r < heigth_map.shape[0] - 1 else r, c),
        (r, c - 1 if c > 0 else c),
        (r, c + 1 if c < heigth_map.shape[1] - 1 else c),
    ]


basin_sizes = list()
for low_p in low_points:
    to_check = {low_p}
    checked = set()
    basin_size = 0
    while to_check:
        point = to_check.pop()
        checked.add(point)
        if heigth_map[point[0]][point[1]] < 9:
            basin_size += 1
            to_check = to_check.union(set(neighbours(point)).difference(checked))
    basin_sizes.append(basin_size)

area = 1
N = 3
for b in sorted(basin_sizes, reverse=True):
    if N > 0:
        area *= b
        N -= 1
    else:
        break
print(area)
