from os import pathsep
from pathlib import Path
import numpy as np
from abc import abstractmethod


class State:
    @abstractmethod
    def parse_line(self, line, context):
        pass


class DotEntry(State):
    def parse_line(self, line, context):
        line = line.strip()
        if line:
            dots = [int(d) for d in line.split(",")]
            context._dots.append(dots)
        else:
            context.set_new_state(FoldEntry())


class FoldEntry(State):
    def parse_line(self, line, context):
        line = line.strip()
        if line:
            line = line.replace("fold along ", "")
            fold = line.split("=")
            context._folds.append((fold[0], int(fold[1])))
        else:
            context._done = True


class LineParser:
    def __init__(self, initial_state):
        self._state = initial_state
        self._dots = []
        self._folds = []
        self._done = False

    @property
    def state(self):
        return self._state

    @property
    def done(self):
        return self._done

    @property
    def dots(self):
        return self._dots

    @property
    def folds(self):
        return self._folds

    def set_new_state(self, state):
        self._state = state

    def parse_line(self, line):
        self._state.parse_line(line, self)


this_file = Path(__file__)
line_parser = LineParser(DotEntry())
with open(this_file.parent / "input.txt") as file:
    while not line_parser.done:
        line_parser.parse_line(file.readline())

dots = line_parser.dots
folds = line_parser.folds


def print_paper(paper):
    for row in paper:
        line = "".join([p for p in row])
        print(line)
    print()


def update_paper(dots):
    xmax = max([d[0] for d in dots])
    ymax = max([d[1] for d in dots])

    paper = np.array([["."] * (xmax + 1)] * (ymax + 1))
    for d in dots:
        paper[d[1]][d[0]] = "#"
    return paper


def count_dots(paper):
    condition = paper == "#"
    return np.count_nonzero(condition)


part1 = True
for fold in folds:
    fold_axis = fold[0]
    fold_coord = fold[1]
    if "y" == fold_axis:
        for dot in dots:
            y = dot[1]
            if y > fold_coord:
                dot[1] = fold_coord - abs(dot[1] - fold_coord)
        ymin = min([d[1] for d in dots])
        if ymin < 0:
            dots = [[d[0], d[1] - ymin] for d in dots]
    else:
        for dot in dots:
            x = dot[0]
            if x > fold_coord:
                dot[0] = fold_coord - abs(dot[0] - fold_coord)
        xmin = min([d[0] for d in dots])
        if xmin < 0:
            dots = [[d[0] - xmin, d[1]] for d in dots]
    if part1:
        print(count_dots(update_paper(dots)))
        part1 = False

print_paper(update_paper(dots))
