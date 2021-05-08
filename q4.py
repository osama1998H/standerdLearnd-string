#  Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

string = input("enter the string: ")

f = string[0]
for i in string:
    if i == f:
        x = string.replace(i, "$")


print(x)
