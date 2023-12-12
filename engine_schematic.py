import re
with open("engine_schematic.txt", "r") as file:
    engine_file = file.read()

def split_lines(l):
    return l.split('\n')

engine_file_txt = split_lines(engine_file)
engine_list = []
line_list = []
for line in engine_file_txt:
    i_char = 0
    for char in line:
        line_list.append(char)
    engine_list.append(line_list)
    line_list = []
count_list = 0
num_list = []
num = 0
sum = []
is_dot = True
result = 0
def checking_if_dot(engine_list,inx_list, inx_char):

    if (inx_char != 0) and (char.isdigit() == False) and (engine_list[inx_list][inx_char-1]) != '.':
        is_dot = False
    elif (inx_char < 139) and (char.isdigit() == False) and (engine_list[inx_list][inx_char+1]) != '.':
         is_dot = False
    elif (inx_list > 0):
        if (inx_char != 0) and (engine_list[inx_list-1][inx_char-1]) != '.':
            is_dot = False
        elif (engine_list[inx_list-1][inx_char]) != '.':
            is_dot = False
        elif (inx_char < 139) and (engine_list[inx_list-1][inx_char+1]) != '.':
            is_dot = False
    elif (inx_list < 139):
        if (engine_list[inx_list+1][inx_char]) != '.':
            is_dot = False
        elif (engine_list[inx_list+1][inx_char]) != '.':
            is_dot = False
        elif (inx_char < 139) and (engine_list[inx_list+1][inx_char+1]) != '.':
            is_dot = False
    else:
        is_dot = True
    return is_dot
#def check_same_line(list,ind_tuple):

for line in engine_list:
    count_char = 0
    for char in engine_list[count_list]:
        is_number = False
        is_digit = False

        if char.isdigit():
            is_digit = True
            is_number = True
            is_dot = checking_if_dot(engine_list, count_list, count_char)

        if (is_number == False):
            str_num = ''
            if num_list:
                for n in num_list:
                    str_num = str_num + str(n)
                num = int(str_num)
                if (is_dot == False):
                    sum.append(num)
                    num_list = []
                    num = 0
        if (is_digit == True):
            num_list.append(char)
            index_of_digits = (count_list,count_char)

        count_char += 1
count_list += 1
for s in sum:
    result += s

print(result)


