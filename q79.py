
string = ''' Write a Python program to count number of substrings with same first and last characters of a given string. '''.split()

print(string)

ch = 0
sh = 0

for i, j in enumerate(string):
    if len(j) > ch:
        ch = len(j)
        sh = i
cl = ch
sl = 0
for i, j in enumerate(string):
    if len(j) < cl:
        cl = len(j)
        sl = i

print(string[sh], string[sl])
