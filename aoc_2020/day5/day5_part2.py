with open('d5p1.txt', 'r') as f:
    data = f.read().strip().split()
    
data = [(i[:-3], i[-3:]) for i in data]
id_list = []

for row, col in data:
    row = int(row.replace("F","0").replace("B","1"), 2)
    col = int(col.replace("R", "1").replace("L","0"), 2)
    
    ID = row *8 + col
    id_list.append(ID)
id_list.sort()

for i in range(len(id_list)):
    if id_list[i] + 1 != id_list[i+1]:
        print(id_list[i] + 1)
        break
    
