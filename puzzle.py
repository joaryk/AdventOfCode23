import re
with open("puzzle_input.txt", "r") as file:
    puzzle = file.read()
    '''
    for line in puzzle:
        line = print(puzzle.readline())
'''
def split_lines(l):
   return l.split('\n')

lines = split_lines(puzzle)
result = 0
for line in lines:
    num = ""
    n = 0
    for char in line:
        if char.isdigit():
            num = num + char
    #print(num)
    n = num[0] + num[-1]
    n_int = int(n)
    #print(n_int)
    result += + n_int
print(result)







