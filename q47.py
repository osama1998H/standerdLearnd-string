string = input("enter the text: ")


string_list = [i for i in string]

string_list[0] = string_list[0].lower()
text = ""
for i in string_list:
    text += i
print(text)
