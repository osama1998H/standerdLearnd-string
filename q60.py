string = input("enter some text: ")

string = list(string)

string[0] = string[0].upper()
string[-1] = string[-1].upper()

text = ''.join(string)
print(text)
