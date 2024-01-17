import re

race_time = 59688274
max_distance = 543102016641022
ways_to_win = 0

for x in range(race_time - 1):
        distance_result = (x * race_time) - (x * x)
        if (distance_result > max_distance):
            ways_to_win += 1
print(ways_to_win)
    #optional_hold_button_time =

