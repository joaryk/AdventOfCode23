import re

cards_board = list(open('cards_schematic.txt'))

winning_numbers = {}
my_numbers = {}
winning_from_my_numbers = []
winning_from_my_numbers_ = []
results_in_card = []

counting_cards = {}
for i in range(220):
        counting_cards[i] = 1

for n, line in enumerate(cards_board):
        x = (re.split("[|]", line)[0]).strip()
        winning_numbers[n] = (re.split("\s", (re.split("[:]", x)[1]).strip()))
        my_numbers[n] = (re.split("\s", (re.split("[|]", line)[1]).strip()))

for r in range(220):
        winning_from_my_numbers = set(winning_numbers[r]) & set(my_numbers[r])
        winning_from_my_numbers_ = [ x for x in winning_from_my_numbers if x.isdigit() ]
        l = len(winning_from_my_numbers_)
        check_card = counting_cards[r]
        if r == 219:
                break
        for c_c in range(check_card):
                for y in range(l):
                        counting_cards[r + (y + 1)] += 1
result = 0
for c in counting_cards:
        result += counting_cards[c]
print(result)

