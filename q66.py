str1 = input("str1: ")
str2 = input("str2: ")
new_str = ''
if len(str1) > len(str2):
    str1, str2 = str2, str1
elif len(str2) != len(str1):
    for _ in str1:
        for n in str2:
            new_str += n

print(str1)
print(new_str)