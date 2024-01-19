import itertools
import re

hands_txt = list(open('camel_cards.txt'))

strenght_of_labels = {"2":"A", "3":"B", "4":"C", "5":"D", "6":"E", "7":"F", "8":"G", "9":"H", "T":"I", "J":"J", "Q":"K", "K":"L", "A":"M"}
hands_labels_map = {}
hands_strenght_map = {}
hands_bid_map = {}

def hand_strenght(hand_labels_):

    if len(hand_labels) == 1: #Five of a kind
        return 7
    elif len(hand_labels) == 2 and ("4" in hand_labels.values()) : #Four of a kind
        return 6
    elif len(hand_labels) == 2 and ("2" in hand_labels.values()) and ("3" in hand_labels.values()) : #Full house
        return 5
    elif len(hand_labels) == 3 and ("3" in hand_labels.values()) and ("1" in hand_labels.values()): #Three of a kind
        return 4
    elif len(hand_labels) == 3 and ("2" in hand_labels.values()) and ("1" in hand_labels.values()): #Two pair
        return 3
    elif len(hand_labels) ==4: # One pair
        return 2
    elif len(hand_labels) ==5: # High card
        return 1



for line in hands_txt:
    hand = line.split()[0]
    bid = line.split()[1]
    hands_bid_map[hand] = bid

for n in hands_bid_map:
    hand_labels = {}
    labels_in_hand = sorted(n)
    label_counter = {}
    g = itertools.groupby(labels_in_hand, lambda x : x)
    for label, group in g:
        hand_labels[label] = len(list(group))
    hands_labels_map[n] = hand_labels
    print(n, hand_labels)



#stworzyć mapę hands_rank na podstawie
#na końcu porównać słowniki hands_map i hands_rank


