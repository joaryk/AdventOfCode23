import re
import math

oasis_txt = list(open('OASIS_report.txt'))

next_values_of_histories = []

def split_line(line):
    list = line.split()
    return list

def differences(list):
    list_of_differences = []
    for count_, value_ in enumerate(list):
        if (count_ > 0 and count_< len(list)):
            v = int(value_)
            y = int(list[count_ - 1])
            x = int(v - y)
            list_of_differences.append(x)
    return list_of_differences

for line in oasis_txt:
    not_all_zeros = True
    all_diff_lists = []
    diff_list = differences(split_line(line))
    all_diff_lists.append(diff_list)

    while not_all_zeros:
        diff_list = differences(diff_list)
        if all([v == 0 for v in diff_list]):
            not_all_zeros = False
        all_diff_lists.append(diff_list)

    new_value = 0

    # for a in all_diff_lists:
    #         print(a)

    for count, a in reversed(list(enumerate(all_diff_lists))):
        new_value = new_value + all_diff_lists[count][-1]

    print('new value = ', new_value)
    next_values_of_histories.append(new_value)

print(sum(next_values_of_histories))


#927927514

