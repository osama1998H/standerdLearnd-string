string = input('enter the text : ')
x = list(string)
for i in x:
    if i.islower():
        x[x.index(i)] = i.upper()
    elif i.upper():
        x[x.index(i)] = i.lower()
text = ''.join(x)
print(text)
