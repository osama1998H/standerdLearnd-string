string = input("enter the string: ")
freq = {}
for i in string:
    freq[i] = string.count(i)

count = 0
for key, value in freq.items():
    if value > count:
        count = value

def get_key(val):
    for k,v in freq.items():
        if val == v:
            return k

print(get_key(count))