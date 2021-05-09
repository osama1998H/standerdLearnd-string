# Write a Python function to insert a string in the middle of a string.

def add_blade(blade: str, content: str) -> str:
    """[summary]

    Args:
        blade (str): [the blade directive like ( {{}}, [[]], <<>> )]
        content (str): [text want to add in the blade]

    Returns:
        str: [return blade template]
    """
    blade = [i for i in blade]
    middle = int(len(blade)/2)
    new_blade = ""
    blade.insert(middle, content)
    for b in blade:
        new_blade += b
    return(new_blade)


print(add_blade("{{}}", "php"))
