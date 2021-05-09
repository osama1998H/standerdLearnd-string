# string = input("enter the string: ")

def insert_end(text, n):
    new_text = text[-n:] * 4
    print(new_text)


insert_end("python", 2)
