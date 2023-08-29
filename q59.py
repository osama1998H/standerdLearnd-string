string = input("enter the string: ")
freq = {i: string.count(i) for i in string}
count = 0
for value in freq.values():
    if value > count:
        count = value

def get_key(val):
    for k,v in freq.items():
        if val == v:
            return k

print(get_key(count))