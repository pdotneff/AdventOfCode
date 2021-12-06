with open('day2_part1.txt', 'r') as f:
    instructions = [x.split() for x in f.read().strip().split('\n')]
    instructions = [(x[0], int(x[1])) for x in instructions]

# Part 1

horizontal = 0
depth = 0

for i in instructions:
    if i[0]=="forward":
        horizontal += i[1]
    elif i[0]=="down":
        depth += i[1]
    else:
        depth -= i[1]
        
print(f"part1 horitzontal = {horizontal}, depth = {depth}")
print(f"part1 h*d = {horizontal * depth}")


# Part 2
horizontal = 0
depth = 0
aim = 0

for i in instructions:
    if i[0]=="forward":
        horizontal += i[1]
        depth += aim * i[1]
    elif i[0]=="down":
        aim += i[1]
    else:
        aim -= i[1]
        
print(f"part2 horitzontal = {horizontal}, depth = {depth}")
print(f"part2 h*d = {horizontal * depth}")
