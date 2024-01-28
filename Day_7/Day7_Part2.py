import itertools
import re
import my_types_

hands_txt = list(open('camel_cards.txt'))

multiplied = []
hands_list = []
sorted_hands_list = []

for line in hands_txt:
    hand = line.split()[0]
    bid = line.split()[1]
    hands_list.append(my_types_.CamelCards_(hand, bid))
# coś się dzieje przy 2giej hand wywołaniu metodzie
sorted_hands_list = sorted(hands_list, key=lambda x: x.hand_rank())

n = 1
for s in sorted_hands_list:
    multiplied.append(int(s.bid) * n)
    n += 1
print(sum(multiplied))
