string = input('enter sonme text: ')

a = [i for i in string]
count = 0
for i in a:
    if i == " ":
        count += 1

string = string.replace(" ", "")

print(" " * count + string)
