

string = input("enter the string:\n::- ")


def new_func(string: str):
    count = sum(1 for i in string if string.index(i) <= 3 and i.isupper())
    return string.upper() if count >= 2 else string


print(new_func(string))
