# Part Two
# Find out which board will win last

import copy 
import numpy as np

with open("day4.txt", 'r') as f:
    data = f.read().strip().split('\n\n')

number_order = [int(x) for x in data[0].split(',')]
data.pop(0)
boards = []
answer_found = False
board_answer = -1

for board in data:
    temp = [int(x) for x in board.split()]
    boards.extend(temp)
    
all_boards = np.array(boards)
all_boards = all_boards.reshape(-1,5,5)
marked_boards = copy.copy(all_boards)
number_of_boards_minus_one = len(all_boards) - 1
all_board_set = set(range(len(all_boards)))

for number in number_order:
    answer = np.where(all_boards == number)
    
    for i in range(len(answer[0])):
        x, y, z = answer[0][i], answer[1][i], answer[2][i]
        marked_boards[x][y][z] = -1
        
    row_sum = np.sum(marked_boards, axis=2)
    col_sum = np.sum(marked_boards, axis=1)
    
    complete_rows = set(np.where(row_sum == -5)[0])
    complete_cols = set(np.where(col_sum == -5)[0])
    combined_set = complete_rows.union(complete_cols)
    
    if len(combined_set) == number_of_boards_minus_one:        
        board_answer = all_board_set.difference(combined_set)
        board_answer = [x for x in board_answer][0]
        answer_found = True
        
    if answer_found:
        answer_row_sum = np.sum(marked_boards[board_answer], axis= 1)
        answer_col_sum = np.sum(marked_boards[board_answer], axis = 0)
        
        if (-5 in answer_row_sum) or (-5 in answer_col_sum):
            board_sum = np.sum([x for x in marked_boards[board_answer].reshape(-1) if x != -1])
            final_answer = board_sum * number
            print(f"final_answer  = {final_answer}")
            break

