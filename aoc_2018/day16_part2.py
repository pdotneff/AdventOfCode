import re

with open('./day16_list_part_2.txt', 'r') as f:
    data_2 = f.read().strip().split('\n')


def get_digits(line):
    digits = [int(match[0]) for match in re.finditer(r'\d+', line)]
    return digits


def addr__(before, codes):
    code_1 = codes[1]
    code_2 = codes[2]
    code_3 = codes[3]
    after = before
    after[code_3] = before[code_1] + before[code_2]
    return after


def addi__(before, codes):
    code_1 = codes[1]
    code_2 = codes[2]
    code_3 = codes[3]
    after = before
    after[code_3] = before[code_1] + code_2
    return after


def mulr__(before, codes):
    code_1 = codes[1]
    code_2 = codes[2]
    code_3 = codes[3]
    after = before
    after[code_3] = before[code_1] * before[code_2]
    return after


def muli__(before, codes):
    code_1 = codes[1]
    code_2 = codes[2]
    code_3 = codes[3]
    after = before
    after[code_3] = before[code_1] * code_2
    return after


def banr__(before, codes):
    code_1 = codes[1]
    code_2 = codes[2]
    code_3 = codes[3]
    after = before
    after[code_3] = before[code_1] & before[code_2]
    return after


def bani__(before, codes):
    code_1 = codes[1]
    code_2 = codes[2]
    code_3 = codes[3]
    after = before
    after[code_3] = before[code_1] & code_2
    return after


def borr__(before, codes):
    code_1 = codes[1]
    code_2 = codes[2]
    code_3 = codes[3]
    after = before
    after[code_3] = before[code_1] | before[code_2]
    return after
    

def bori__(before, codes):
    code_1 = codes[1]
    code_2 = codes[2]
    code_3 = codes[3]
    after = before
    after[code_3] = before[code_1] | code_2
    return after
 

def setr__(before, codes):
    code_1 = codes[1]
    code_2 = codes[2]
    code_3 = codes[3]
    after = before
    after[code_3] = before[code_1]
    return after


def seti__(before, codes):
    code_1 = codes[1]
    code_2 = codes[2]
    code_3 = codes[3]
    after = before
    after[code_3] = code_1
    return after

        
def gtir__(before, codes):
    code_1 = codes[1]
    code_2 = codes[2]
    code_3 = codes[3]
    after = before
    if (code_1 > before[code_2]):
        after[code_3] = 1
    else:
        after[code_3] = 0
    return after


def gtri__(before, codes):
    code_1 = codes[1]
    code_2 = codes[2]
    code_3 = codes[3]
    after = before
    if before[code_1] > code_2:
        after[code_3] = 1
    else:
        after[code_3] = 0
    return after


def gtrr_(before, codes):
    code_1 = codes[1]
    code_2 = codes[2]
    code_3 = codes[3]
    after = before
    if before[code_1] > before[code_2]:
        after[code_3] = 1
    else:
        after[code_3] = 0
    return after


def eqir__(before, codes):
    code_1 = codes[1]
    code_2 = codes[2]
    code_3 = codes[3]
    after = before
    if code_1 == before[code_2]:
        after[code_3] = 1
    else:
        after[code_3] = 0
    return after                   


def eqri__(before, codes):
    code_1 = codes[1]
    code_2 = codes[2]
    code_3 = codes[3]
    after = before
    if before[code_1] == code_2:
        after[code_3] = 1
    else:
        after[code_3] = 0
    return after


def eqrr__(before, codes):
    code_1 = codes[1]
    code_2 = codes[2]
    code_3 = codes[3]
    after = before
    if before[code_1] == before[code_2]:
        after[code_3] = 1
    else:
        after[code_3] = 0
    return after


# func_dict output from Registers Part 1
func_dict = {14: muli__, 13: addi__, 15: mulr__, 1: addr__, 8: borr__, 5: bori__, 7: seti__,
             11: eqrr__, 2: eqri__, 10: eqir__, 12: gtri__, 4: gtrr_, 6: gtir__,
             3: setr__, 0: banr__, 9: bani__}


def part_2(func_dict, data):
    instructions = [get_digits(x) for x in data]
    start = [0, 0, 0, 0]
    for i in instructions:
        opcode = i[0]
        formula = func_dict[opcode]
        after = formula(start, i)
        start = after
    print(start)


part_2(func_dict, data_2)
