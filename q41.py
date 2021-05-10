text = input("hit some keys: ")

chars = ["a", "b", "s"]


def strips(text, chars):
    return "".join(c for c in text if c not in chars)


print(strips(text, chars))
