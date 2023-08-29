from colorama import Fore

string = input(f"{Fore.GREEN}Enter The Text: ")


def new_func(string: str):
    string = string.split()
    count = 0
    for i in string:
        if len(i) > count:
            count = len(i)
            index = string.index(i)
    return string, count, index


string, count, index = new_func(string)

print("largest word: ", Fore.BLUE + string[index])
print("length of word: ", Fore.BLUE + str(count))
