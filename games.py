import re
with open("games_input.txt", "r") as file:
    games_file = file.read()

def split_lines(l):
    return l.split('\n')

games_txt = split_lines(games_file)

games_map = {}
game_line = ""
game = ""
rounds = ""
cubes = ""
cubes_map = {}
max_map = {"red" : "12", "blue" : "14", "green" : "13"}
is_possible = 0
delimiters = [",", ";"]

for line in games_txt:
    game_line = line.split(": ")
    games_map[game_line[0]] = game_line[1]
for g in games_map:
    #print(g, ":", games_map[g])
    game = games_map[g]
    rounds = game.split("; ")

    for r in rounds:
        cubes = r.split(", ")
    for c in cubes:
        throw = c.split(" ")
        cubes_map[throw[1]] = throw[0]
    for x in cubes_map:
        print(x, ":", cubes_map[x])

    # for key in cubes_map:
    #     if cubes_map[key] <= max_map[key]:
    #         is_possible += 1
#print(is_possible)