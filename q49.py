vowels = "aeiuoAEIOU"

string = input('enter the text: ')


freq = {}
for i in vowels:
    count = sum(1 for n in string if i == n)
    if count > 0:
        freq[i] = count

print(freq)
