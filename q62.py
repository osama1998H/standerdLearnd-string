string = input("enter some text : ")


count = 0

for i in string:
    if i.isnumeric():
        count += int(i)

print(count)
