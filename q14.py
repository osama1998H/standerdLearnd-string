string = input("enter the color with comma seprated: ")

string = string.split(",")

print(sorted(string, key=lambda x: len(x)))  # ? Sorted With Small Length
print(sorted(string))  # ? Sorted With Alphbetcaly
