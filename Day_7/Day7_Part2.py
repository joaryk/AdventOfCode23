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
for h in hands_list:
    h.h_r = h.hand_rank()
sorted_hands_list = sorted(hands_list, key=lambda x: x.hand_rank())
#245674174
#255326326

n = 1
for s in sorted_hands_list:
    multiplied.append(int(s.bid) * n)
    n += 1
print(sum(multiplied))
