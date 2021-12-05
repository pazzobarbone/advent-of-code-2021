from pathlib import Path
import numpy as np


def get_board_combinations_and_associated_board_ids(lines):
    combinations = list()
    board_ids = list()
    current_board_combinations = list()
    current_board_id = 0
    if lines[-1] != "\n":
        lines.append("\n")
    for line in lines:
        line = line.strip()
        if not line:
            if current_board_combinations:
                for c in range(len(current_board_combinations[0])):
                    combinations.append(
                        [current_board_combinations[r][c] for r in range(len(current_board_combinations))]
                    )
                    board_ids.append(current_board_id)
                current_board_combinations = []
                current_board_id += 1
        else:
            combinations.append([int(i) for i in line.split()])
            current_board_combinations.append([int(i) for i in line.split()])
            board_ids.append(current_board_id)
    return combinations, board_ids


def find_first_bingo_board_combinations_and_last_drawn_number(combinations, board_ids, drawn_numbers):
    last_number_drawn = None
    first_bingo_board_id = None
    scores = [0] * len(combinations)
    number_of_boards = len(set(board_ids))
    combinations = np.array(combinations)
    done = False
    for d in drawn_numbers:
        matches = np.where(combinations == d)
        for m in matches[0]:
            scores[m] += 1
            if scores[m] == len(combinations[0]):
                first_bingo_board_id = board_ids[m]
                last_number_drawn = d
                done = True
                break
        if done:
            break
    combinations_per_board = int(len(combinations) / number_of_boards)
    bingo_board_combinations = combinations[
        combinations_per_board * first_bingo_board_id : combinations_per_board * first_bingo_board_id
        + combinations_per_board
    ]
    return bingo_board_combinations, last_number_drawn


def calculate_answer(board_combinations, last_drawn_number):
    combination_length = len(board_combinations[0])
    unmarked_number_sum = 0
    last_number_drawn_idx = drawn_numbers.index(last_drawn_number)
    draw = drawn_numbers[: last_number_drawn_idx + 1]
    for r in range(combination_length):
        for c in range(combination_length):
            if not board_combinations[r][c] in draw:
                unmarked_number_sum += board_combinations[r][c]
    print(unmarked_number_sum * last_drawn_number)


def find_last_bingo_board_combinations_and_last_drawn_number(combinations, board_ids, drawn_numbers):
    last_number_drawn = None
    last_bingo_board_id = None
    scores = [0] * len(combinations)
    number_of_boards = max(board_ids) + 1
    won = [0] * number_of_boards
    rows_in_a_board = len(combinations[0])
    done = False
    combinations = np.array(combinations)
    for d in drawn_numbers:
        matches = np.where(combinations == d)
        for m in matches[0]:
            scores[m] += 1
            board_id = board_ids[m]
            if (scores[m] == rows_in_a_board) and (not won[board_id]):
                won[board_id] = 1
                if sum(won) == len(combinations) / 2 / rows_in_a_board:
                    last_bingo_board_id = board_id
                    last_number_drawn = d
                    done = True
                    break
        if done:
            break
    combinations_per_board = int(len(combinations) / number_of_boards)
    bingo_board_combinations = combinations[
        combinations_per_board * last_bingo_board_id : combinations_per_board * last_bingo_board_id
        + combinations_per_board
    ]
    return bingo_board_combinations, last_number_drawn


this_file = Path(__file__)
with open(this_file.parent / "input.txt") as file:
    lines = file.readlines()

drawn_numbers = [int(i) for i in lines[0].strip().split(",")]
lines.remove(lines[0])
combinations, board_ids = get_board_combinations_and_associated_board_ids(lines)

first_bingo_board, last_drawn_number = find_first_bingo_board_combinations_and_last_drawn_number(
    combinations, board_ids, drawn_numbers
)
calculate_answer(first_bingo_board, last_drawn_number)

last_bingo_board, last_drawn_number = find_last_bingo_board_combinations_and_last_drawn_number(
    combinations, board_ids, drawn_numbers
)
calculate_answer(last_bingo_board, last_drawn_number)