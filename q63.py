from typing import Text


string = input('text ip: ')


string = [i for i in string]
print(string)
for i in string:
    if i.isdigit():
        if int(i) == 0 and string[string.index(i)+1] != ".":
            string.remove(i)

x = ''
for i in string:
    x += i
print(x)
