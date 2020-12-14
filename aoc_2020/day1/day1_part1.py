import numpy as np

with open ("d1p1.txt") as f:
    data = f.read().strip().split('\n')
    data = np.array(data).astype(int)

for i in range(len(data)):
    for j in range(len(data)):
        if i == j:
            continue
        if data[i] + data[j] == 2020:
            print(f"i:{i}, j:{j}, product: {data[i] * data[j]}")
