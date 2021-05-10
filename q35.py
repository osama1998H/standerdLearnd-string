number = input("enter the nubmer only: ")

numbers_list = [i for i in number]
for i in numbers_list:
    print(i, end=",")
print("\n")
print("the cost is $ {:,}".format(int(number)))