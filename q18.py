
string = input("enter the text: ")


def first_three(text: str):
    if len(text) <= 3:
        return text
    new_text = text[:3]
    return new_text.capitalize()


print(first_three(string))
