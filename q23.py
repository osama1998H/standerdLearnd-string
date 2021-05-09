text = "hello from new line\n man on city\n this is my life"

def remove_new_line(text:str):
    return text.replace("\n", "")


print(text)
print("==============")
print(remove_new_line(text))
