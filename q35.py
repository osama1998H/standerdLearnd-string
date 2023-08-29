number = input("enter the nubmer only: ")

numbers_list = list(number)
for i in numbers_list:
    print(i, end=",")
print("\n")
print("the cost is $ {:,}".format(int(number)))