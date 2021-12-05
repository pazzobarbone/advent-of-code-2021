from pathlib import Path
import numpy as np

this_file = Path(__file__)
with open(this_file.parent / "input.txt") as file:
    lines = file.readlines()

drawn_numbers = [int(i) for i in lines[0].strip().split(",")]
lines.remove(lines[0])
all_board_lines = list()
this_board_lines = list()
this_board_n = 0
board_ids = list()
if lines[-1] != "\n":
    lines.append("\n")
for line in lines:
    line = line.strip()
    if not line:
        if this_board_lines:
            for c in range(len(this_board_lines[0])):
                all_board_lines.append([this_board_lines[r][c] for r in range(len(this_board_lines))])
                board_ids.append(this_board_n)
            this_board_lines = []
            this_board_n += 1
    else:
        all_board_lines.append([int(i) for i in line.split()])
        this_board_lines.append([int(i) for i in line.split()])
        board_ids.append(this_board_n)

boards = np.array(all_board_lines)


done = False
scores = [0] * len(all_board_lines)
last_number_drawn = None
rows_in_a_board = len(all_board_lines[0])
for d in drawn_numbers:
    matches = np.where(boards == d)
    for m in matches[0]:
        scores[m] += 1
        if scores[m] == rows_in_a_board:
            winning_board_n = board_ids[m]
            last_number_drawn = d
            done = True
            break
    if done:
        break


winning_board = all_board_lines[
    2 * rows_in_a_board * winning_board_n : 2 * rows_in_a_board * winning_board_n + 2 * rows_in_a_board
]
columns_in_a_board = rows_in_a_board
unmarked_number_sum = 0
last_number_drawn_idx = drawn_numbers.index(last_number_drawn)
extraction = drawn_numbers[: last_number_drawn_idx + 1]
for r in range(rows_in_a_board):
    for c in range(columns_in_a_board):
        if not winning_board[r][c] in extraction:
            unmarked_number_sum += winning_board[r][c]
print(unmarked_number_sum * last_number_drawn)


done = False
scores = [0] * len(all_board_lines)
number_of_boards = max(board_ids) + 1
won = [0] * number_of_boards
last_number_drawn = None
rows_in_a_board = len(all_board_lines[0])
for d in drawn_numbers:
    matches = np.where(boards == d)
    for m in matches[0]:
        scores[m] += 1
        board_id = board_ids[m]
        if (scores[m] == rows_in_a_board) and (not won[board_id]):
            won[board_id] = 1
            if sum(won) == len(all_board_lines) / 2 / rows_in_a_board:
                last_winning_board_n = board_id
                last_number_drawn = d
                done = True
                break
    if done:
        break


winning_board_n = last_winning_board_n
winning_board = all_board_lines[
    2 * rows_in_a_board * winning_board_n : 2 * rows_in_a_board * winning_board_n + 2 * rows_in_a_board
]
columns_in_a_board = rows_in_a_board
unmarked_number_sum = 0
last_number_drawn_idx = drawn_numbers.index(last_number_drawn)
extraction = drawn_numbers[: last_number_drawn_idx + 1]
for r in range(rows_in_a_board):
    for c in range(columns_in_a_board):
        if not winning_board[r][c] in extraction:
            unmarked_number_sum += winning_board[r][c]
print(unmarked_number_sum * last_number_drawn)
