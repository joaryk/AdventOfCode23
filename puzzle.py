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

for line in lines:
    num = ""
    for char in line:
        if char.isdigit():
            num = num + char
    print(num)







