str1 = input("str1: ")
str2 = input("str2: ")
common = []
for i in str1:
    for n in str2:
        if i == n:
            if i not in common:
                common.append(i)
                break

print(common)
