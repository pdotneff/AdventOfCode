with open('d12p1.txt', 'r') as f:
    data = f.read().strip().split()
    data = [(x[0], int(x[1:])) for x in data]

x_coord = 0
y_coord = 0

directions = ["E", "S", "W", "N"]
direct = "E"
for instruction, amount in data:
    if instruction == "R":
        rotate = int(((amount/90) + directions.index(direct)) % 4)
        direct = directions[rotate]
        continue
    elif instruction == "L":
        rotate = int(directions.index(direct) - (amount/90))
        direct = directions[rotate:][0]
        continue

    if instruction == "F":
        instruction = direct
    
    if instruction == "E":
        x_coord += amount
    elif instruction == "W":
        x_coord -= amount
    elif instruction == "S":
        y_coord -= amount
    else:
        y_coord += amount
        
print(f'X_Coord = {x_coord} and Y_Coord = {y_coord}')
print(f'Sum = {abs(x_coord) +abs(y_coord)}')
