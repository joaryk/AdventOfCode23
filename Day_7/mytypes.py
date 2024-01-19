import itertools


class CamelCards:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.h_r = self.hand_rank()

    def hand_rank(self):

        strenght_of_hand = self.hand_strenght()
        strenght_of_labels = self.strenght_of_labels()
        r = (strenght_of_hand, strenght_of_labels)
        return r

    def hand_labels_map(self):
        hand_labels = {}
        labels_in_hand = sorted(self.hand)
        label_counter = {}
        g = itertools.groupby(labels_in_hand, lambda x: x)
        for label, group in g:
            hand_labels[label] = len(list(group))
        return hand_labels

    # strenght to mapa strenght_of_labels

    def hand_strenght(self):

        hand_labels = self.hand_labels_map()

        if len(hand_labels) == 1:  # Five of a kind
            return 7
        elif len(hand_labels) == 2 and (4 in hand_labels.values()):  # Four of a kind
            return 6
        elif len(hand_labels) == 2 and (2 in hand_labels.values()) and (3 in hand_labels.values()):  # Full house
            return 5
        elif len(hand_labels) == 3 and (3 in hand_labels.values()) and (
                1 in hand_labels.values()):  # Three of a kind
            return 4
        elif len(hand_labels) == 3 and (2 in hand_labels.values()) and (1 in hand_labels.values()):  # Two pair
            return 3
        elif len(hand_labels) == 4:  # One pair
            return 2
        elif len(hand_labels) == 5:  # High card
            return 1

    def strenght_of_labels(self):

        strenght_of_labels = {"2": "A", "3": "B", "4": "C", "5": "D", "6": "E", "7": "F", "8": "G", "9": "H", "T": "I",
                              "J": "J", "Q": "K", "K": "L", "A": "M"}
        new_labels = ''
        for h in self.hand:
            if h in strenght_of_labels.keys():
                new_labels = new_labels + strenght_of_labels.get(h)

        return new_labels
