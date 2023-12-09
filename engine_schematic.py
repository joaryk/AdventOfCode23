import re
with open("engine_schematic.txt", "r") as file:
    engine_file = file.read()

def split_lines(l):
    return l.split('\n')

engine_file_txt = split_lines(engine_file)
engine_list = []
line_list = []
for line in engine_file_txt:
    line_list.append(line)
    engine_list.append(line_list)
count_list = 0
num_list = []
num = 0
sum = []

# def checking_chars(inx_line, ind_char):


for e in engine_list:
    for line in engine_list[count_list]:
        count_char = 0
        for char in line_list[count_char]:
            is_number = False
            is_digit = False
            is_symbol = False
            if char.isdigit():
                is_digit = True
                is_number = True
                inx_list = count_list+1
                inx_char = count_char+1
                if (engine_list[inx_list][inx_char]) != '.':
                    is_symbol = True
                    break

            if (is_number == False):
                str_num = ''
                if num_list:
                    for n in num_list:
                        str_num = str_num + str(n)
                        num = int(str_num)
                    sum.append(num)
                    num_list = []
                    num = 0
            if (is_digit == True):
                num_list.append(char)

            count_char += 1
    count_list += 1



