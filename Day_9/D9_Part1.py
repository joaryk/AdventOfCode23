import re

oasis_txt = list(open('OASIS_report.txt'))

def differences(line_of_oasis):
    list_of_differences = []
    list_of_values = line_of_oasis.split()

    for count_, value_ in enumerate(list_of_values):
        v = int(value_)
        y = int(list_of_values[count_ - 1])
        x = v - y
        list_of_differences.append(x)

for line in oasis_txt:
    differences(line)


