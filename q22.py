string = input("enter the name below: ")


def generate_user(string: str) -> tuple:
    """[summary]

    Args:
        string (tuple): [the orginal string]

    Returns:
        str: [return tuble of 3 values (orginal string, new string, out value)]
    """
    old_string = string
    string = list(string)
    new_string = sorted(string)
    out = "".join(new_string)
    return(string, new_string, out)


print(generate_user(string))

# help(generate_user)
