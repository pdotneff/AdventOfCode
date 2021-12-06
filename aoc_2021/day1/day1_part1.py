with open('day1_part1.txt', 'r') as f:
    depths = [int(x) for x in f.read().strip().split()]

increases = 0

for reading in range(1, len(depths)):
    if depths[reading] - depths[reading - 1] > 0:
        increases += 1

print(f"part1 answer: {increases}")


# Part 2
increases = 0 

for reading in range(len(depths)):
    try:
        measure_2 = sum(depths[reading + 1 : reading + 4])
    except:
        break
    
    measure_1 = sum(depths[reading : reading + 3])
    
    if measure_2 > measure_1:
        increases += 1
        
print(f"part2 answer: {increases}")
