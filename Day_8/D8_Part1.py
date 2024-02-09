import re

l_r = "LLRLRRLLRLRRLLRLRRLRRRLRLRLRRRLLRLRRRLRLRRRLRLRLLLRRLRLRLLRLRRLRRRLRRRLLRRLRLRRRLRRLRRRLRLLRRLRRRLRRRLRRLRLRRLLLRLRLLRRRLRRLLRLRLRRLLRLRRLLRLRRLRRLLRRRLRLRLRRRLLRRRLRRLRRRLRRRLRLRRRLRRLLLRRRLRLLLRRRLRLLRLLRRRLLRRLRRRLRRRLRLLRLRLRRRLLRRLRRRLRRLRLLRRRLRRLRRRLRRRLRRRLRLRRRLRRRLRLRRRR"
l_r_instruction = [*l_r]

map_txt = list(open('map_to_escape.txt'))
dict_map = {}
steps = 0
not_finish = True
start = "AAA"
stop = "ZZZ"
next_step = ""

for line in map_txt:
    x = line.split(" = ")[0]
    lr = line.split("= (")[1]
    l = lr.split(", ")[0]
    r = lr.split(", ")[1][:3]
    step = (x,l,r)
    dict_map[x] = (l, r)

while not_finish:
    for n in l_r_instruction:
        steps += 1
        if n == "L":
            start = dict_map[start][0]
        else:
            start = dict_map[start][1]
        if start == stop:
            not_finish = False
            break

print(steps)
#18827


