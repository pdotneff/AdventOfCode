# Updated code for part 1 in order to get part 2
# and didn't save copy.  Only have  Part II code

with open('d8p1.txt', 'r') as f:
    data = [p.split() for p in f.read().strip().split('\n')]

accumulator = 0
visited = {}
start = 0
next_code = 1
stop_code = False
last_index = len(data) - 1
occurrances = 0

while not stop_code:
    if start == last_index:
        stop_code = True
    instruction, value = data[start][0], int(data[start][1])
    
    if instruction in ["jmp", "nop"]:
        occurrances += 1
        if instruction == 'jmp' and occurrances == next_code:
            instruction = 'nop'
        elif instruction == "nop" and occurrances == next_code:
            instruction = 'jmp'

        
    if start in visited:
        visited = {}
        next_code += 1
        accumulator = 0
        start = 0
        occurrances = 0
        
    else:
        visited[start] = 1

        if instruction == 'acc':
            start += 1
            accumulator += value
        elif instruction == 'jmp':
            start += value
        else:
            start += 1

print(f'value of accumulator: {accumulator}')
    
