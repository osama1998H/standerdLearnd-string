# Write a Python function to insert a string in the middle of a string.

def add_blade(blade: str, content: str) -> str:
    """[summary]

    Args:
        blade (str): [the blade directive like ( {{}}, [[]], <<>> )]
        content (str): [text want to add in the blade]

    Returns:
        str: [return blade template]
    """
    blade = list(blade)
    middle = len(blade) // 2
    blade.insert(middle, content)
    return "".join(blade)


print(add_blade("{{}}", "php"))
