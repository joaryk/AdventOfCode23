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
possible_games = []
delimiters = [",", ";"]

result = 0

for line in games_txt:
    game_line = line.split(": ")
    games_map[game_line[0]] = game_line[1]
    game = game_line[1]
    rounds = game.split("; ")
    all_rounds_ok = True

    for r in rounds:
        cubes = r.split(", ")
        all_cubes_ok = True
        for c in cubes:
            throw = c.split(" ")
            colour = throw[1]
            value = int(throw[0])
            max_value = int(max_map[colour])
            #cubes_map[throw[1]] = throw[0]
            if value > max_value:
                all_cubes_ok = False
                break
        if all_cubes_ok == False:
            all_rounds_ok = False
            break
    if all_rounds_ok == True:
        possible_games.append(game_line[0])
        #print(game_line[0])
        num_of_game = int(game_line[0].split(" ")[1])
        result += num_of_game
print(result)
