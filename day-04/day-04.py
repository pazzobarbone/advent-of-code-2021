from pathlib import Path
import numpy as np


class Board:
    def __init__(self, combinations):
        self._bingo = False
        self._combinations = np.array(combinations)
        self._score = [0] * len(combinations)
        self._combination_length = len(combinations[0])

    @property
    def bingo(self):
        return self._bingo

    def check_number(self, number):
        matches = np.where(self._combinations == number)
        for m in matches[0]:
            self._score[m] += 1
            if self._score[m] == len(self._combinations[0]):
                self._bingo = True
                break

    def get_puzzle_answer(self, draws):
        unmarked_number_sum = 0
        for r in range(self._combination_length):
            for c in range(self._combination_length):
                if not self._combinations[r][c] in draws:
                    unmarked_number_sum += self._combinations[r][c]
        return unmarked_number_sum * draws[-1]


def create_board_list(lines):
    boards = list()
    combinations = list()
    if lines[-1] != "\n":
        lines.append("\n")
    for line in lines:
        line = line.strip()
        if not line:
            if combinations:
                boards.append(Board(combinations + list(map(list, zip(*combinations)))))
                combinations = []
        else:
            combinations.append([int(i) for i in line.split()])
    return boards


def part1(boards, draws):
    done = False
    for d in draws:
        for board in boards:
            board.check_number(d)
            if board.bingo:
                drawn_so_far = draws[: draws.index(d) + 1]
                print(board.get_puzzle_answer(drawn_so_far))
                done = True
                break
        if done:
            break


def part2(boards, draws):
    done = False
    bingos = [0] * len(boards)
    for d in draws:
        for i, board in enumerate(boards):
            board.check_number(d)
            if board.bingo:
                bingos[i] = 1
                if sum(bingos) == len(boards):
                    drawn_so_far = draws[: draws.index(d) + 1]
                    print(board.get_puzzle_answer(drawn_so_far))
                    done = True
                    break
        if done:
            break


this_file = Path(__file__)
with open(this_file.parent / "input.txt") as file:
    lines = file.readlines()

draws = [int(i) for i in lines[0].strip().split(",")]
lines.remove(lines[0])

boards = create_board_list(lines)
part1(boards, draws)
boards = create_board_list(lines)
part2(boards, draws)
