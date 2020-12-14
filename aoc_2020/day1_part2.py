import numpy as np

# Not the elegant way of doing this, but was a few days late in getting started
# on Advent of Code so was trying to catch up :-)

with open ("d1p1.txt") as f:
    data = f.read().strip().split('\n')
    data = np.array(data).astype(int)

for i in range(len(data)):
    for j in range(len(data)):
        for k in range(len(data)):
            if i == j == k:
                continue
            if data[i] + data[j] + data[k] == 2020:
                print(f"i:{i}, j:{j}, product: {data[i] * data[j] * data[k]}")
            
    

