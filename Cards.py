import re

cards_board = list(open('cards_schematic.txt'))

winning_numbers = {}
my_numbers = {}

for n, line in enumerate(cards_board):
        x = (re.split("[|]", line)[0]).strip()
        winning_numbers[n] = (re.split("\s", (re.split("[:]", x)[1]).strip()))

        my_numbers[n] = (re.split("\s", (re.split("[|]", line)[1]).strip()))
my_numbers = []

#porownywac liczby z obu list (slownikow) findall albo inaczej x = re.findall("[4][5]", txt)

