import re

cards_board = list(open('cards_schematic.txt'))

winning_numbers = {}
my_numbers = {}
winning_from_my_numbers = []
winning_from_my_numbers_ = []
results_in_card = []

for n, line in enumerate(cards_board):
        x = (re.split("[|]", line)[0]).strip()
        winning_numbers[n] = (re.split("\s", (re.split("[:]", x)[1]).strip()))
        my_numbers[n] = (re.split("\s", (re.split("[|]", line)[1]).strip()))
result = 0

for r in range(220):
        winning_from_my_numbers = set(winning_numbers[r]) & set(my_numbers[r])
        winning_from_my_numbers_ = [ x for x in winning_from_my_numbers if x.isdigit() ]
        l = len(winning_from_my_numbers_)
        if l == 0:
                p = 0
        elif l == 1:
                p = 1
        else:
                p = 2 ** (l - 1)
        #print(r, l, p)
        result += p
print(result)

