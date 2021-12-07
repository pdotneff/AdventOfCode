with open("day7.txt", 'r') as f:
    data = [int(x) for x in f.read().strip().split(",")]
    
max_value = max(data)
min_value = min(data)

cost = max_value * len(data)
final_position = -1
for position in range(min_value, max_value + 1):
    temp_cost = 0
    
    for i in data:
        move_cost = abs(i - position)
        temp_cost += move_cost
    
    if temp_cost < cost:
        cost = temp_cost
        final_position = position
        
print(cost, final_position)
