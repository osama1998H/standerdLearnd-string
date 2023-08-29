string = input("enter the string: ")

def del_odd(string: str) -> str:
    string = list(string)
    for i in string:
        if string.index(i) % 2 != 0:
            string.remove(i)
    return "".join(string)

new_string = del_odd(string)

print(new_string)
