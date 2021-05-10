string = input("enter some text:  ")

print(string)
print(string.replace(" ", ""))


def chars_freq(string: str):
    string = string.replace(" ", "")
    string = [i for i in string]
    freq = {}
    for i in string:
        count = 0
        for s in string:
            if i == s:
                count += 1
        freq[i] = count

    return freq


freq = chars_freq(string).items()
sort_freq = sorted(freq)
for key, value in sort_freq:
    print(f"{key} : {value}")
