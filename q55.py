string = input("enter the string: ").split()
freq = {}
for i in string:
    freq[i] = string.count(i)

for key, value in freq.items():
    if value > 1:
        print(f"{key} : {value}")
        break
