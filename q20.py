string = input("Enter The Text: ")


def r4r(text):
    return text[::-1] if len(text) % 4 == 0 else text


print(r4r(string))
