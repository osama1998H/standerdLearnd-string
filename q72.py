string = input('enter sonme text: ')
char = input('enter char: ')

a = list(string)
b = list(string)
for i in b:
    if i != char:
        a.remove(i)

text = ''.join(a)
print(text)
