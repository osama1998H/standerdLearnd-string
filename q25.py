
hasher = [
    "a", "b", "c", "d", "e",
    "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z"
]

text = input("enter the text: ")

string = list(text)
new_string = [hasher[hasher.index(n)+3] for n in string]
x = "".join(new_string)
print(x)
