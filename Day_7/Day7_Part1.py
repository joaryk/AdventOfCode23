import itertools
import re

hands_txt = list(open('camel_cards.txt'))

strenght_of_labels = {"2":1, "3":2, "4":3, "5":4, "6":5, "7":6, "8":7, "9":8, "T":9, "J":10, "Q":11, "K":12, "A":13}
hands_labels_map = {}
hands_strenght_map = {}
hands_bid_map = {}


for line in hands_txt:
    hand = line.split()[0]
    bid = line.split()[1]
    hands_bid_map[hand] = bid


for n in hands_bid_map:
    hand_labels = []
    labels_in_hand = sorted(n)
    label_counter = {}
    g = itertools.groupby(labels_in_hand, lambda x : x)
    for label, group in g:
        label_counter = {label: len(list(group))}
        hand_labels.append(label_counter)
    hands_labels_map[n] = hand_labels
    print(n, label_counter)



#stworzyć mapę hands_rank na podstawie
#na końcu porównać słowniki hands_map i hands_rank


