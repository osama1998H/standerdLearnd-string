string = input("enter the text: ")


string_list = list(string)

string_list[0] = string_list[0].lower()
text = "".join(string_list)
print(text)
