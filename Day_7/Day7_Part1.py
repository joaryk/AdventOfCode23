import itertools
import re

hands_txt = list(open('camel_cards.txt'))
hands_map = {}
print(hands_txt)
for line in hands_txt:
    hand = line.split()[0]
    bid = line.split()[1]
    hands_map[hand] = bid

for n in hands_map:
    h = sorted(n)
    label_counter = {}
    g = itertools.groupby(h, lambda x : x)
    for label, group in g:
        label_counter = {label: len(list(group))}
        print(n, label_counter)



# grupowanie elementów
# n = [5,5,2,2,5,2,5]
# n.sort()
# g = itertools.groupby(n, lambda x : x)
# for key, group in g:
#     key_and_group = {key : list(group)}
#     print(key_and_group)


