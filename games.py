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

delimiters = [",", ";"]

result = 0
multiplication_results = []

for line in games_txt:

    highest_map = {"red": "0", "green": "0", "blue": "0"}
    game_line = line.split(": ")
    games_map[game_line[0]] = game_line[1]
    game = game_line[1]
    rounds = game.split("; ")
    multiplication = 1

    for r in rounds:
        cubes = r.split(", ")
        for c in cubes:
            throw = c.split(" ")
            colour = throw[1]
            value = int(throw[0])
            highest_value = int(highest_map[colour])
            if value > highest_value:
                highest_map[colour] = value

    for h in highest_map:
        multiplication = multiplication * highest_map[h]
        if h == 'blue':
            multiplication_results.append(multiplication)

# for f in range(len(multiplication_results)):
#     print(multiplication_results[f])

result = sum(multiplication_results)
print("Wynik: ", result)