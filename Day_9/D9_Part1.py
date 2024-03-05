import re
import math

oasis_txt = list(open('OASIS_report.txt'))


next_values_of_histories = []
not_all_zeros = True

def differences(line_of_oasis):
    list_of_differences = []
    list_of_values = line_of_oasis.split()
    for count_, value_ in enumerate(list_of_values):
        if (count_ > 0 and count_< len(list_of_values)):
            v = int(value_)
            y = int(list_of_values[count_ - 1])
            x = int(math.fabs(y - v))
            list_of_differences.append(x)
    return list_of_differences

def differences_(list):
    list_of_differences = []
    for count_, value_ in enumerate(list):
        if (count_ > 0 and count_< len(list)):
            v = int(value_)
            y = int(list[count_ - 1])
            x = int(math.fabs(y - v))
            list_of_differences.append(x)
    return list_of_differences

for line in oasis_txt:
    #zamiast last chars zrobic listę list i dodawac do niej kazda kolejna diff_list, podliczac na koncu linii
    last_chars = []
    diff_list = differences(line)
    last_char = diff_list[-1]
    last_chars.append(last_char)

    while not_all_zeros:
        diff_list = differences_(diff_list)
        if all([v == 0 for v in diff_list]):
            not_all_zeros = False
        last_char = diff_list[-1]
        last_chars.append(last_char)
    print(last_chars)
    c = 1
    #for l in reversed(last_chars):



print('we have next values from history')


