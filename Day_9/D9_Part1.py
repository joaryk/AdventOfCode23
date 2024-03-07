import re
import math

oasis_txt = list(open('OASIS_report.txt'))


next_values_of_histories = []
not_all_zeros = True
c = 0
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
    all_diff_lists = []
    diff_list = differences(line)
    all_diff_lists.append(diff_list)

    while not_all_zeros:
        diff_list = differences_(diff_list)
        if all([v == 0 for v in diff_list]):
            not_all_zeros = False
        all_diff_lists.append(diff_list)
    for a in reversed(all_diff_lists):
        new_value = a[-1]

    c += 1



print(c)


