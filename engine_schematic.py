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
for e in engine_list:
    for line in engine_list[count_list]:

        count_char = 0
        for char in line_list[count_char]:
            is_digit = False
            if char.isdigit():
                is_digit = True
                is_number = True
            is_number = False

            if (is_number == False):
                str_num = ''
                for n in num_list:
                    str_num = str_num + str(n)
                    num = int(str_num)
                    sum.append(num)
                num = 0
                str_num = ''
            if (is_digit == True):
                num_list.append(char)
            count_char += 1
    count_list += 1



