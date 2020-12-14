with open ("d2p1.txt") as f:
    data = f.read().strip().split('\n')

total = 0
for password in data:
    low_high, letter, pw = password.split()
    low_high = [int(x) for x in low_high.split("-")]
    letter = letter[0]
    
    if low_high[0] <= pw.count(letter) <= low_high[1]:
        total += 1
print(total)
