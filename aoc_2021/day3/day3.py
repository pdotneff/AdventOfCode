with open("day3.txt", 'r') as f:
    data = f.read().strip().split()
    
    num_length = len(data[0])
    data = [int(x, 2) for x in data]
    
gamma = ""
epsilon = ""

for i in range(num_length):
    ones = 0
    zeros = 0
    
    for number in data:
        if number >> i & 1:
            ones += 1
        else:
            zeros += 1
    
    if ones > zeros:
        gamma = "1" + gamma
        epsilon = "0" + epsilon
    else:
        gamma = "0" + gamma
        epsilon = "1" + epsilon
        
print(f"gamma = {gamma}, epsilon = {epsilon}")

gamma_dec = int(gamma, 2)
epsilon_dec = int(epsilon, 2)

print(f"gamma decimal = {gamma_dec}, epsilon decimal = {epsilon_dec}")
print(f"answer = {gamma_dec * epsilon_dec}")
