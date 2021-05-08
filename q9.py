

string = input("enter the text: ")
string1 = None
for i in range(len(string)):
    if i+1 == len(string):
        if string[i] == "t" and string[i+1] == "h":
            string1 = string.replace("h", "")
    else:
        pass
print(string1)
    