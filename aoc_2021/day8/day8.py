with open("day8.txt", 'r') as f:
    data = [x.strip().split() for x in f.read().strip().split('\n')]

# Part One 
unique_numbers = 0
for line in data:
    for value in line[-4:]:
        if len(value) in [2,3,4,7]:
            unique_numbers += 1

print(f"Part One Answer: total occurs: {unique_numbers}")

final_numbers = []
for row, codes in enumerate(data):

    num_dict = {}
    number = ""

    one = [x for x in codes[:10] if len(x)==2][0]
    seven = [x for x in codes[:10] if len(x)==3][0]
    eight = [x for x in codes[:10] if len(x)==7][0]
    four = [x for x in codes[:10] if len(x)==4][0]

    four_diff_one = list(set(four).difference(one))
    five_parts = [x for x in codes[:10] if len(x)==5]
    six_parts = [x for x in codes[:10] if len(x)==6]

    # Find Value for Zero
    for index, value in enumerate(six_parts):
        for part in four_diff_one:
            if part in value:
                pass
            else:
                zero = value
                six_parts.pop(index)

    # Find Six and Nine
    for index, value in enumerate(six_parts):
        if one[0] in value and one[1] in value:
            nine = value
            six = [x for x in six_parts if x != nine][0]
            break
        else:
            six = value
            nine = [x for x in six_parts if x != six][0]
            break

    # Find two, three, five
    for index, value in enumerate(five_parts):
        for part in four_diff_one:
            if four_diff_one[0] in value and four_diff_one[1] in value:
                five = value
                five_parts.pop(index)
                break

    for index, value in enumerate(five_parts):
        if one[0] in value and one[1] in value:
            three = value
            two = [x for x in five_parts if x != three][0]
            break
        else:
            two = value
            three = [x for x in five_parts if x != two][0]
            break

    num_dict = {"".join(sorted(one)): "1", "".join(sorted(two)): "2",
                "".join(sorted(three)): "3", "".join(sorted(four)): "4",
                "".join(sorted(five)): "5", "".join(sorted(six)): "6",
                "".join(sorted(seven)): "7", "".join(sorted(eight)): "8",
                "".join(sorted(nine)): "9", "".join(sorted(zero)): "0", }

    for value in codes[-4:]:
        sorted_value = "".join(sorted(value))
        number += num_dict[sorted_value]

    final_numbers.append(int(number))


print()
print(f"Part 2 Final Answer: {sum(final_numbers)}")

