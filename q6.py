string = input("input the string: ")


def new_func_ing(string: str) -> str:
    if len(string) < 3:
        return("enter a longer text")
    elif string[-3] + string[-2] + string[-1] == "ing":
        return f"{string}ly"
    else:
        return f"{string}ing"


print(new_func_ing(string))
