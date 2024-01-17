import re

race_time = [59, 68, 82, 74]
max_distance = [543, 1020, 1664, 1022]
races_map = {59:543, 68:1020, 82:1664, 74:1022}
multiply = 1
ways_to_win = []

for x in races_map:
    ways_to_win_race = 0
    for y in range(10, x - 1):
        distance_result = (y * x) - (y * y)
        if (distance_result > races_map[x]):
            ways_to_win_race += 1
            print(distance_result)
    ways_to_win.append(ways_to_win_race)
    ways_to_win_race = 0

for w in ways_to_win:
    multiply = multiply * w

print(multiply)
    #optional_hold_button_time =

