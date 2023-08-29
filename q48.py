string = input("enter the text: ")
string = list(string)
comma = string.index(',')
dot = string.index('.')

string[comma] = '.'
string[dot] = ','

text = ''.join(string)
print(text)
maketras = text.maketrans

print(text.translate(maketras(',.', '.,')))
