# Part One
import numpy as np

with open("day9.txt", 'r') as f:
    data = f.read().strip().split()
    data = np.array(data)
    
risk_levels = 0
spot = 0
board_dict = {}

for i, row in enumerate(data):
    for j in range(len(row)):
        board_dict[(i,j)] = data[i][j]
        
board_height = len(data)
board_width = len(data[0])

for i in range(board_height):
    for j in range(board_width):
        value = int(board_dict[(i,j)])
        top = int(board_dict.get((i-1, j), 100))
        bottom = int(board_dict.get((i+1, j), 100))
        left = int(board_dict.get((i, j-1), 100))
        right = int(board_dict.get((i, j+1), 100))
        
        if value < top and value < bottom and value < left and value < right:
            spot += 1
            risk = value + 1
            risk_levels += risk
            
print(f"Part One Risk Level = {risk_levels}")

