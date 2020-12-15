with open('d6p1.txt', 'r') as f:
    data = f.read().strip().split("\n\n")
    data = [item.split("\n") for item in data ]

total = []
for answers in data:
    unique = set()
    for i, person in enumerate(answers):
        characters = [char for char in person]

        if i == 0:
            unique = unique.union(set(characters))
        else:
            unique = unique.intersection(set(characters))
    total.append(len(unique))
        
print(sum(total))
