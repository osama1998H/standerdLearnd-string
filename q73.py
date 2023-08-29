string = input('enter some string : ')

lString = list(string)

upper = []
lower = []
nums = []
sympol = []

for i in lString:
    if i.isupper():
        upper.append(i)
    elif i.islower():
        lower.append(i)
    elif i.isnumeric():
        nums.append(i)
    else:
        sympol.append(i)

print((upper))
print((lower))
print((nums))
print((sympol))
