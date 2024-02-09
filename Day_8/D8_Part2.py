import re

l_r = "LLRLRRLLRLRRLLRLRRLRRRLRLRLRRRLLRLRRRLRLRRRLRLRLLLRRLRLRLLRLRRLRRRLRRRLLRRLRLRRRLRRLRRRLRLLRRLRRRLRRRLRRLRLRRLLLRLRLLRRRLRRLLRLRLRRLLRLRRLLRLRRLRRLLRRRLRLRLRRRLLRRRLRRLRRRLRRRLRLRRRLRRLLLRRRLRLLLRRRLRLLRLLRRRLLRRLRRRLRRRLRLLRLRLRRRLLRRLRRRLRRLRLLRRRLRRLRRRLRRRLRRRLRLRRRLRRRLRLRRRR"
l_r_instruction = [*l_r]

map_txt = list(open('map_to_escape.txt'))
dict_map = {}
steps = 0
not_finish = True
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


while not_finish:
    for n in l_r_instruction:
        steps += 1
        all = True
        for count, s in enumerate(range(6)):
            if n == "L":
                start[count] = dict_map[s][0]
            else:
                start[count] = dict_map[s][1]
            all = all and s[-1] == 'Z'
        # stop = [s for s in start if s[-1] == 'Z']
        if all:
            not_finish = False
            break

print(steps)
#9101102404326


