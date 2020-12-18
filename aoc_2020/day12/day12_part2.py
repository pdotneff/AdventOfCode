with open('d12p1.txt', 'r') as f:
    data = f.read().strip().split()
    data= [(x[0], int(x[1:])) for x in data]

x_coord = 0
y_coord = 0

waypoint = [10, 1]

directions = ["E", "S", "W", "N"]
direct = "E"
for instruction, amount in data:
    if (instruction == "R" and amount == 90) or (instruction =="L" and amount == 270):
        waypoint = [waypoint[1], -waypoint[0]]
    elif (instruction == "R" and amount == 180) or (instruction =="L" and amount == 180):
        waypoint = [-waypoint[0], -waypoint[1]]
    elif (instruction == "R" and amount == 270) or (instruction =="L" and amount == 90):
            waypoint = [-waypoint[1], waypoint[0]]  
            
    elif instruction == "N":
        waypoint[1] += amount
    elif instruction == "E":
        waypoint[0] += amount
    elif instruction == "S":
        waypoint[1] -= amount
    elif instruction == "W":
        waypoint[0] -= amount
    else:
        x_mult = amount * waypoint[0]
        y_mult = amount * waypoint[1]
        
        x_coord += x_mult
        y_coord += y_mult
        
print(f'X_Coord = {x_coord} and Y_Coord = {y_coord}')
print(f'Sum = {abs(x_coord) + abs(y_coord)}')
