import itertools
import re
import my_types

hands_txt = list(open('camel_cards.txt'))

multiplied = []
hands_list = []
sorted_hands_list = []

for line in hands_txt:
    hand = line.split()[0]
    bid = line.split()[1]
    hands_list.append(my_types.CamelCards(hand, bid))

sorted_hands_list = sorted(hands_list, key=lambda x: x.h_r)

n = 1
for s in sorted_hands_list:
    multiplied.append(int(s.bid) * n)
    n += 1
print(sum(multiplied))
