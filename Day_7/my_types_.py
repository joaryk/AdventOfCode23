import itertools


class CamelCards_:
    def __init__(self, hand, bid):
        self.hand = hand
        self.hand_ = self.checking_J_in_hand()
        self.bid = bid
        self.h_r = (0,'')

    def hand_rank(self):

        strenght_of_hand = self.hand_strenght()
        strenght_of_labels = self.strenght_of_labels()
        r = (strenght_of_hand, strenght_of_labels)
        return r

    def hand_labels_map(self):
        hand_labels = {}
        labels_in_hand = sorted(self.hand)
        g = itertools.groupby(labels_in_hand, lambda x: x)
        for label, group in g:
            hand_labels[label] = len(list(group))
        return hand_labels


    def hand_labels_map_(self):
        hand_labels = {}
        labels_in_hand = sorted(self.hand_)
        g = itertools.groupby(labels_in_hand, lambda x: x)
        for label, group in g:
            hand_labels[label] = len(list(group))
        return hand_labels

    def hand_strenght(self):

        hand_labels = self.hand_labels_map_()

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

        strenght_of_labels = {"J": "A", "2": "B", "3": "C", "4": "D", "5": "E", "6": "F", "7": "G", "8": "H", "9": "I",
                              "T": "J", "Q": "K", "K": "L", "A": "M"}
        new_labels = ''
        for h in self.hand:
            if h in strenght_of_labels.keys():
                new_labels = new_labels + strenght_of_labels.get(h)

        return new_labels

    def checking_J_in_hand(self):
        labels_max = []
        map = {}
        label_max = ''
        new_hand = ''
        strenght_of_labels = {"2": "A", "3": "B", "4": "C", "5": "D", "6": "E", "7": "F", "8": "G", "9": "H", "T": "I",
                              "J": "J", "Q": "K", "K": "L", "A": "M"}
        hand_labels = self.hand_labels_map()
        if "J" in hand_labels:
            #sprawdzama najliczniej występujące znaki, zapisuje je do listy labels_max
            #labels_max.append( k for k, v in hand_labels.items() if v == max(hand_labels.values()) and k != "J")
            for k, v in hand_labels.items():
                if (v == max(hand_labels.values())) and (k != 'J'):
                    labels_max.append(k)
            #jeśli jest ich więcej niż 1, sprawdzam, który znak ma większą rangę
            if len(labels_max) > 1:
                label_max = sorted(labels_max, key=lambda r: strenght_of_labels[r], reverse=True)[0]
            else:
                label_max = labels_max[0]
            hand = self.hand
            for h in hand:
                if h == "J":
                    new_hand += str(label_max)
                else:
                    new_hand += h
            return new_hand
        else:
            return self.hand




