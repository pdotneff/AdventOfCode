import copy 
import numpy as np

with open("day4.txt", 'r') as f:
    data = f.read().strip().split('\n\n')

number_order = [int(x) for x in data[0].split(',')]
data.pop(0)
boards = []
answer_found = False

for board in data:
    temp = [int(x) for x in board.split()]
    boards.extend(temp)
    
all_boards = np.array(boards)
all_boards = all_boards.reshape(-1,5,5)
marked_boards = copy.copy(all_boards)
    
for number in number_order:
    answer = np.where(all_boards == number)
    
    for i in range(len(answer[0])):
        x, y, z = answer[0][i], answer[1][i], answer[2][i]
        marked_boards[x][y][z] = -1
        
    row_sum = np.sum(marked_boards, axis=2)
    col_sum = np.sum(marked_boards, axis=1)
    
    if -5 in row_sum:
        print(f"row: {-5 in row_sum}")
        fin_answer = np.where(row_sum == -5)
        answer_found = True
    elif -5 in col_sum:
        print(f"col: {-5 in col_sum}")
        fin_answer = np.where(col_sum == -5)
        answer_found = True
    
    if answer_found:
        board_answer = fin_answer[0]
        
        board_sum = np.sum([x for x in marked_boards[board_answer].reshape(-1) if x != -1])
        final_answer = board_sum * number
        print(f"final_answer  = {final_answer}")
        break

