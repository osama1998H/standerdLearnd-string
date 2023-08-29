string = input('enter sonme text: ')

a = list(string)
count = sum(1 for i in a if i == " ")
string = string.replace(" ", "")

print(" " * count + string)
