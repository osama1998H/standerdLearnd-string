string = input('enter sonme text: ')
char = input('enter char: ')

a = [i for i in string]
b = [i for i in string]
for i in b:
    if i != char:
        a.remove(i)

# string = string.replace(" ", "")
text = ''
# print(" " * count + string)
for i in a:
    text += i
print(text)
