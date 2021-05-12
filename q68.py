from typing import Counter

string = input('enter some text : ')
a = Counter(string)
d = []
nd = []
for key, value in a.items():
    # print(key, value)
    if value > 1:
        d.append(key)
    else:
        nd.append(key)

text1 = ''
text2 = ''

for i in d:
    text1 += i

for i in nd:
    text2 += i

print(text1)
print(text2)
