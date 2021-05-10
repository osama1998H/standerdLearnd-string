string = input("enter the text: ")
string = [i for i in string]
comma = string.index(',')
dot = string.index('.')

string[comma] = '.'
string[dot] = ','

text = ''
for i in string:
    text += i
print(text)
maketras = text.maketrans

print(text.translate(maketras(',.', '.,')))
