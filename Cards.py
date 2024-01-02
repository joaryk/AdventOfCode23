import re

cards_board = list(open('cards_schematic.txt'))

winning_numbers = {}
my_numbers = []

for n, line in enumerate(cards_board):
        x = re.split("[|]", line)[0]
        winning_numbers.append(re.split("[:]", x)[1])
        my_numbers.append(re.split("[|]", line)[1])

#zrobic split po spacji na obu listach (slownikach): x = re.split("\s", txt)
#porownywac liczby z obu list (slownikow) findall albo inaczej x = re.findall("[4][5]", txt)

