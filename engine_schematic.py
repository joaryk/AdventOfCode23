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
def checking_if_dot(e_l,inx_list, inx_char):
    check = False
    if (inx_char != 0) and (e_l[inx_list][inx_char-1]) != '.' and ((e_l[inx_list][inx_char-1]).isdigit() == False):
        is_dot = False
        check = True
    elif check == False:
        is_dot = True
    if is_dot and (inx_char < 139) and (e_l[inx_list][inx_char+1]) != '.' and (e_l[inx_list][inx_char+1].isdigit() == False):
        is_dot = False
        check = True
    elif check == False:
        is_dot = True
    if (inx_list > 0):
        if (inx_char != 0) and (e_l[inx_list-1][inx_char-1]) != '.':
            is_dot = False
            check = True
        elif check == False:
            is_dot = True
        if is_dot and (e_l[inx_list-1][inx_char]) != '.':
            is_dot = False
            check = True
        elif check == False:
            is_dot = True
        if is_dot and (inx_char < 139) and (e_l[inx_list-1][inx_char+1]) != '.':
            is_dot = False
            check = True
        elif check == False:
            is_dot = True
    if (inx_list < 139):
        if (e_l[inx_list+1][inx_char-1]) != '.':
            is_dot = False
            check = True
        elif check == False:
            is_dot = True
        if (e_l[inx_list+1][inx_char]) != '.':
            is_dot = False
            check = True
        elif check == False:
            is_dot = True
        if (inx_char < 139) and (e_l[inx_list+1][inx_char+1]) != '.':
            is_dot = False
            check = True
        elif check == False:
            is_dot = True
    return is_dot
#def check_same_line(list,ind_tuple):

for line in engine_list:
    count_char = 0
    for char in line:
        is_number = False
        is_digit = False
        num_to_sum = False
        if char.isdigit():
            is_digit = True
            is_number = True
            # is_dot = checking_if_dot(engine_list, char, count_list, count_char)
        if (is_number == False):
            str_num = ''
            if num_list:
                for n in num_list:
                    str_num = str_num + str(n[0])
                for n in num_list:
                    is_dot = checking_if_dot(engine_list, n[1], n[2])
                    if is_dot == False:
                        num_to_sum = True
                        break
                num = int(str_num)
                if (num_to_sum == True):
                    sum.append(num)
                num_list = []
                num = 0
        if (is_digit == True):
            x = len(num_list)
            num_list.append((char, count_list, count_char))
        count_char += 1
    count_list += 1
for s in sum:
    result += s

print(result)


