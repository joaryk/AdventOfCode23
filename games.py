import re
with open("games_input.txt", "r") as file:
    games_file = file.read()

def create_map_of_games(cube, colour):
    games_map = []
    for i in range(len(cube)):
        game = (cube[i], colour[i])
        games_list.append(game)
    return games_list

def create_list_of_rounds(cube, colour):
    games_list = []
    for i in range(len(cube)):
        games_dict = {cube[i] : colour[i]}
        games_list.append(games_dict)
    return games_list

def split_lines(l):
   return l.split('\n')
games_txt = split_lines(games_file)

numbers = []
colours = ["red","green","blue"]
n = 0
c = ''
for line in games_txt:

    #list_of_games = create_list_of_games2(n,c)




    # for char in line:
    #     if char == ":":
    #         key += char
    #     elif:
    #         break
    #     value += char