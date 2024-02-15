import re

oasis_txt = list(open('OASIS_report.txt'))

def differences(line_of_oasis):
    list_of_differences = []
    list_of_values = line_of_oasis.split()
    for value_ in list_of_values:
        v = int(value_)
        print(v)

for line in oasis_txt:
    differences(line)


