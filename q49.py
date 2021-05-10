vowels = "aeiuoAEIOU"

string = input('enter the text: ')


freq = {}
for i in vowels:
    count = 0
    for n in string:
        if i == n:
            count += 1
    if count > 0:
        freq[i] = count

print(freq)
