unwanted_chars = ["#", "*", "!", "^", "%"]
string = "so!!me*tect%#"
for i in string:
    for n in unwanted_chars:
        if i == n:
            string = string.replace(i, '')
print(string)
