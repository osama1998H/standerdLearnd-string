string = input("Enter The Text: ")


def r4r(text):
    if len(text) % 4 == 0:
        return text[::-1]
    else:
        return text


print(r4r(string))
