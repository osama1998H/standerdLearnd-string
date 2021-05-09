
hasher = [
    "a", "b", "c", "d", "e",
    "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]

text = input("enter the text: ")

string = [i for i in text]
new_string = []
for n in string:

    new_string.append(hasher[hasher.index(n)+3])

x = ""
for i in new_string:
    x += i
print(x)
