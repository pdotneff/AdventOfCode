with open('d6p1.txt', 'r') as f:
    data = f.read().strip().split("\n\n")
    data = [item.split("\n") for item in data ]

total = []
for answers in data:
    uniques = []
    for person in answers:
        characters = [char for char in person]
        uniques.extend(characters)
    total.append(len(set(uniques)))
            
print(sum(total))
