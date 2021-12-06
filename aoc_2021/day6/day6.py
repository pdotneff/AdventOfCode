from collections import Counter
import copy
import sys

def main(num_days):
    with open("day6.txt", 'r') as f:
        data = [int(x) for x in f.read().strip().split(',')]

    fish_groups = Counter(data)
    temp_groups = copy.copy(fish_groups)

    for day in range(1, num_days+1): 
        fish_groups[8] = temp_groups[0]
        fish_groups[7] = temp_groups[8]
        fish_groups[6] = temp_groups[7] + temp_groups[0]
        fish_groups[5] = temp_groups[6]
        fish_groups[4] = temp_groups[5]
        fish_groups[3] = temp_groups[4]
        fish_groups[2] = temp_groups[3]
        fish_groups[1] = temp_groups[2]
        fish_groups[0] = temp_groups[1]

        temp_groups = copy.copy(fish_groups)

    print(f"number of lanternfish = {sum(fish_groups.values())}")

if __name__ == "__main__":
    assert len(sys.argv) == 2, "Specify only one integer argument >= 1"

    num_days = int(sys.argv[1])
    main(num_days)
