
string = input("enter the text: ")


def remove_th_voice(string: str) -> str:
    string = [i for i in string]
    new_string,  n = "", "t"
    for i in string:
        if (string.index(i)+1) <= len(string):
            if i == n and string[string.index(i)+1] == "h":
                string.remove(string[string.index(i)+1])
    for n in string:
        new_string += n
    return new_string


new_string = remove_th_voice(string)
print(new_string)
