import re
import math

l_r = "LLRLRRLLRLRRLLRLRRLRRRLRLRLRRRLLRLRRRLRLRRRLRLRLLLRRLRLRLLRLRRLRRRLRRRLLRRLRLRRRLRRLRRRLRLLRRLRRRLRRRLRRLRLRRLLLRLRLLRRRLRRLLRLRLRRLLRLRRLLRLRRLRRLLRRRLRLRLRRRLLRRRLRRLRRRLRRRLRLRRRLRRLLLRRRLRLLLRRRLRLLRLLRRRLLRRLRRRLRRRLRLLRLRLRRRLLRRLRRRLRRLRLLRRRLRRLRRRLRRRLRRRLRLRRRLRRRLRLRRRR"
l_r_instruction = [*l_r]

map_txt = list(open('map_to_escape.txt'))
dict_map = {}
all_steps = []
start = []

next_step = ""

for line in map_txt:
    x = line.split(" = ")[0]
    lr = line.split("= (")[1]
    l = lr.split(", ")[0]
    r = lr.split(", ")[1][:3]
    step = (x,l,r)
    dict_map[x] = (l, r)

start = [d for d in dict_map if d[-1] == 'A']


for count, s in enumerate(start):
    loop = True
    steps_to_Z = 0
    steps_list = []
    while loop:
        for lr in l_r_instruction:
            steps_to_Z += 1
            if lr == "L":
                start[count] = dict_map[s][0]
            else:
                start[count] = dict_map[s][1]
            if start[count][-1] == 'Z':
                steps_list.append(steps_to_Z)
            if dict_map[s][0] == dict_map[s][1]:
                loop = False
                all_steps.append(steps_list)

                break
print(math(all_steps))
#metoda, która bierze kolejne start (z koncowka 'A') i zapisuje step w momencie 'Z' na koncu, konczy, kiedy trafia na ghosta


