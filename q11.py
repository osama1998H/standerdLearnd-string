string = input("enter the string: ")

def del_odd(string: str)->str:
    new_string = ""
    string = [i for i in string]
    for i in string:
        if string.index(i) % 2 != 0:
            string.remove(i)
    for i in string:
        new_string += i
    return new_string

new_string = del_odd(string)

print(new_string)
