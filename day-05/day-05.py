from pathlib import Path
import re
import time

this_file = Path(__file__)
with open(this_file.parent / "input.txt") as file:
    lines = file.readlines()

vertices = list()
for line in lines:
    line = line.strip()
    if line:
        vertices.append([int(v) for v in re.findall(r"\d+", line)])


map_size = max(max(vertices)) + 1
map = list()
for _ in range(map_size):
    map.append([0] * map_size)


def print_map(map):
    for line in map:
        print(*line)
    print("\n")


overlaps = 0
for v in vertices:
    x1, y1, x2, y2 = v
    if x1 == x2:
        ymin = min(y1, y2)
        ymax = max(y1, y2)
        while ymin <= ymax:
            map[ymin][x1] += 1
            if map[ymin][x1] == 2:
                overlaps += 1
            ymin += 1
    elif y1 == y2:
        xmin = min(x1, x2)
        xmax = max(x1, x2)
        while xmin <= xmax:
            map[y1][xmin] += 1
            if map[y1][xmin] == 2:
                overlaps += 1
            xmin += 1
    else:
        if (x2 - x1) / (y2 - y1) > 0:
            xmin = min(x1, x2)
            xmax = max(x1, x2)
            ymin = min(y1, y2)
            while xmin <= xmax:
                map[ymin][xmin] += 1
                if map[ymin][xmin] == 2:
                    overlaps += 1
                xmin += 1
                ymin += 1
        else:
            xmin = min(x1, x2)
            xmax = max(x1, x2)
            ymax = max(y1, y2)
            while xmin <= xmax:
                map[ymax][xmin] += 1
                if map[ymax][xmin] == 2:
                    overlaps += 1
                xmin += 1
                ymax -= 1
    # print_map(map)
    # time.sleep(1)


print(overlaps)
