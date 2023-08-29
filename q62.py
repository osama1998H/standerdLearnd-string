string = input("enter some text : ")


count = sum(int(i) for i in string if i.isnumeric())
print(count)
