#  Write a Python program to count the number of characters (character frequency) in a string

string = "hello from python"
freq = {}

for i in string:
    count = sum(1 for n in string if i == n)
    freq[f"{i}"] = count

print(freq)
