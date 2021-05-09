text = "meijasnpiasnvi"

n = input("enter the litter: ")


def new_func(text, n):
    if text[1] == n:
        print(f"started with {n}")
    else:
        print(f"not started with {n}")


new_func(text, n)
