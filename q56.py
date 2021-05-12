string = input("enter the string: ").split()
freq = {}
for i in string:
    freq[i] = string.count(i)

data = []
for key, value in freq.items():
    if value > 1:
        data.append(key)
print(data[1])
