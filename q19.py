string = "https://www.w3resource.com/python-exercises"


def get_last(string: str, char: str) -> str:
    """[summary]

    Args:
        string (str): [url ]
        char (str): [seprator e.x (/)]

    Returns:
        str: [Last Elment In String]
    """
    string = string.split(char)
    return(string[-1])


print(get_last(string, "-"))
