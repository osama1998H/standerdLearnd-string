string = "1001000000110000"

x = string.split('1')

count = 0
for i in x:
    if len(i) > count:
        count = len(i)

print(count)
