string = input("enter your text: ").split()

rev_string = string[::-1]

text = "".join(f"{i} " for i in rev_string)
print(text)
