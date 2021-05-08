#  Write a Python program to count the number of characters (character frequency) in a string

string = "hello from python"
freq = {}

for i in string:
    count = 0
    for n in string:
        if i == n:
            count += 1
    freq[f"{i}"] = count

print(freq)
