string = input("input two string: ").split()
str1, str2 = string


def generate_string(str1: str, str2: str) -> str:
    """[summary]

    Args:
        str1 (str): [First String]
        str2 (str): [Second String]

    Returns:
        str: [Generated String]
    """
    str1_n = str2[:2] + str1[2:]
    str2_n = str1[:2] + str2[2:]
    new_string = str1_n + " " + str2_n
    return new_string


new_string = generate_string(str1, str2)


print(new_string)
