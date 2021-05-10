string = input("enter your text: ").split()

rev_string = string[::-1]

text = ""
for i in rev_string:
    text += i + " "


print(text)
