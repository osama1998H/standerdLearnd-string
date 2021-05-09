

string = input("enter the string:\n::- ")


def new_func(string: str):
    count = 0
    for i in string:
        if string.index(i) <= 3 and i.isupper():
            count += 1
    if count >= 2:
        return string.upper()
    else:
        return string


print(new_func(string))
