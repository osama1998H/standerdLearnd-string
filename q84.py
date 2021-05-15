string = input('enter the text : ')
x = [i for i in string]
for i in x:
    if i.islower():
        x[x.index(i)] = i.upper()
    elif i.upper():
        x[x.index(i)] = i.lower()
    else:
        pass

text = ''
for i in x:
    text += i


print(text)
