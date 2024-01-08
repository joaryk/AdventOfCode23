import re
with open("puzzle_input.txt", "r") as file:
    puzzle = file.read()
    '''
    for line in puzzle:
        line = print(puzzle.readline())
'''
def split_lines(l):
   return l.split('\n')
result = 0

lines = split_lines(puzzle)

dict_numbers = {"one":"1", "two":"2", "three":"3", "four":"4",
                "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

for line in lines:
    num = ""
    n = 0
    for key in dict_numbers:
        if (key in line):
            line = line.replace(key,key+dict_numbers[key]+key)
    for char in line:
        if char.isdigit():
            num = num + char
    n = num[0] + num[-1]
    n_int = int(n)
    result += + n_int

print(result) #53921 #54676







