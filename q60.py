string = input("enter some text: ")

string = [i for i in string]

string[0] = string[0].upper()
string[-1] = string[-1].upper()

text = ''
for i in string:
    text += i

print(text)
