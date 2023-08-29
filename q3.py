# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

string = input("enter the string: ")

new_string = string[:2] + string[-2:] if len(string) >= 2 else "empty string"
print(new_string)
