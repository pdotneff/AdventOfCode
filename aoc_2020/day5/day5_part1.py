with open('d5p1.txt', 'r') as f:
    data = f.read().strip().split()
    
data = [(i[:-3], i[-3:]) for i in data]

maxID = 0

for row, col in data:
    row = int(row.replace("F","0").replace("B","1"), 2)
    col = int(col.replace("R", "1").replace("L","0"), 2)
    
    ID = row *8 + col
    
    if ID > maxID:
        maxID = ID
print(f"Max ID = {maxID}")
