string = input("enter the string: ")
freq = {i: string.count(i) for i in string}
for key, value in freq.items():
    if value > 1:
        print(f"{key} : {value}")
        break
