from typing import NoReturn
from colorama import Fore
string = input("enter the string: ").split()


def new_func(string: str) -> NoReturn:
    if "poor" in string and "not" in string:
        string.remove("not")
        string[string.index("poor")] = "good"
        new_string = ""
        for i in string:
            new_string += i+" "
        print(Fore.GREEN + f"case 1: {new_string}")
    else:
        new_string = ""
        for i in string:
            new_string += i+" "
        print(Fore.RED + f"case 2: {new_string}")


new_func(string)
