import re

with open('./day16_list.txt', 'r') as f:
    file = f.read().strip().split('\n')


def get_digits(line):
    digits = [int(match[0]) for match in re.finditer(r'\d+',line)]
    return digits


def build_lists(data):
    bef_list = []
    codes = []
    after_list = []

    for i in range(len(data)):
        if data[i].startswith("B"):
            bef_list.append(get_digits(data[i]))
        elif data[i].startswith("A"):
            after_list.append(get_digits(data[i]))
        elif data[i] is "":
            continue
        else:
            codes.append(get_digits(data[i]))
    return bef_list, codes, after_list


def addr__(before, codes, after, integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if before[integer][code_1] + before[integer][code_2] == after[integer][code_3]:
        return True


def addi__(before, codes, after, integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if before[integer][code_1] + code_2 == after[integer][code_3]:
        return True


def mulr__(before, codes, after, integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if before[integer][code_1] * before[integer][code_2] == after[integer][code_3]:
        return True


def muli__(before, codes, after, integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if before[integer][code_1] * code_2 == after[integer][code_3]:
        return True


def banr__(before, codes, after, integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if before[integer][code_1] & before[integer][code_2] == after[integer][code_3]:
        return True


def bani__(before, codes, after, integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if before[integer][code_1] & code_2 == after[integer][code_3]:
        return True


def borr__(before, codes, after, integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if before[integer][code_1] | before[integer][code_2] == after[integer][code_3]:
        return True


def bori__(before, codes, after, integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if before[integer][code_1] | code_2 == after[integer][code_3]:
        return True


def setr__(before, codes, after, integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if before[integer][code_1] == after[integer][code_3]:
        return True


def seti__(before, codes, after, integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if code_1 == after[integer][code_3]:
        return True


def gtir__(before, codes, after, integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if ((after[integer][code_3] == 1) and (code_1 > before[integer][code_2])) or \
            (after[integer][code_3] == 0):
        return True


def gtri__(before, codes, after, integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if ((after[integer][code_3] == 1) and (before[integer][code_1] > code_2)) or \
            (after[integer][code_3] == 0):
        return True


def gtrr_(before, codes, after, integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if ((after[integer][code_3] == 1) and (before[integer][code_1] > before[integer][code_2])) or \
            (after[integer][code_3] == 0):
        return True


def eqir__(before, codes, after, integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if ((after[integer][code_3] == 1) and (code_1 == before[integer][code_2])) or \
            (after[integer][code_3] == 0):
        return True


def eqri__(before, codes, after, integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if ((after[integer][code_3] == 1) and (before[integer][code_1] == code_2)) or \
            (after[integer][code_3] == 0):
        return True


def eqrr__(before, codes, after, integer):
    code_1 = codes[integer][1]
    code_2 = codes[integer][2]
    code_3 = codes[integer][3]
    if ((after[integer][code_3] == 1) and
        (before[integer][code_1] == before[integer][code_2])) or (after[integer][code_3] == 0):
        return True


def main(data):
    before, codes, after = build_lists(data)
    count = 0
    functions = [addr__, addi__, mulr__, muli__, banr__, bani__, borr__, bori__, setr__,
                 seti__, gtir__, gtri__, gtrr_, eqir__, eqri__, eqrr__]
    
    for i in range(len(before)):
        num_func = [x for x in functions if x(before,codes,after,i) == True]
        if len(num_func) >= 3:
            count += 1
    
    print(count) 


def part_2_setup(data):
    before, codes, after = build_lists(data)
    func_dict = {}
    functions = [addr__, addi__, mulr__, muli__, banr__, bani__, borr__, bori__, setr__, seti__,
                 gtir__, gtri__, gtrr_, eqir__, eqri__, eqrr__]
    
    for i in range(len(before)):
        num_func = []
        for f,x in enumerate(functions):
            if (x(before, codes, after, i) == True) and (x not in func_dict.values()):
                num_func.append((f,x))
        if len(num_func) == 1:
            func_dict[codes[i][0]] = num_func[0][1]
    return func_dict


main(file)
part_2_setup(file)
