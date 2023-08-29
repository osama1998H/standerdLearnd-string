from typing import NoReturn
from colorama import Fore
string = input("enter the string: ").split()


def new_func(string: str) -> NoReturn:
    new_string = ""
    if "poor" in string and "not" in string:
        string.remove("not")
        string[string.index("poor")] = "good"
        for i in string:
            new_string += f"{i} "
        print(f"{Fore.GREEN}case 1: {new_string}")
    else:
        for i in string:
            new_string += f"{i} "
        print(f"{Fore.RED}case 2: {new_string}")


new_func(string)
