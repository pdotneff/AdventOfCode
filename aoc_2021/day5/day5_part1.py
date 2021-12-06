from collections import Counter

with open("day5.txt", 'r') as f:
    data = [x.split('->') for x in f.read().strip().split('\n')]
    
grid_dict = {}

for location in data:
    x1, y1 = [int(x) for x in location[0].strip().split(',')]
    x2, y2 = [int(x) for x in location[1].strip().split(',')]

    if x1==x2 or y1==y2:
        x_distance = x2 - x1
        y_distance = y2 - y1
        
        start_x, end_x = min(x1, x2), max(x1, x2)
        start_y, end_y = min(y1, y2), max(y1, y2)
        
        if abs(x_distance) > 0:
            for i in range(start_x, end_x +1):
                grid_dict[(i, y1)] = grid_dict.get((i, y1), 0) + 1
                
        elif abs(y_distance) > 0:
            for i in range(start_y, end_y +1):
                grid_dict[(x1, i)] = grid_dict.get((x1, i), 0) + 1
                
grid_values = [x for x in Counter(grid_dict.values()).values()]
answers = [x for x in grid_values if x != max(grid_values)]

print(f"{sum(answers)} grid points greater than or equal to 2")
