
string = input("enter the string: ")


def change_given_string(string: str) -> str:
    """[summary]

    Args:
        string (str): [Input The Text To Swap First An Last Char]

    Returns:
        str: [Return New Generated String]
    """
    string = [i for i in string]
    new_string = ""
    first = string[0]
    last = string[-1]
    temp = string[0]  # ? this is temprory varible
    string[0] = last
    string[-1] = temp
    for i in string:
        new_string += i
    return new_string


print(change_given_string(string=string))
