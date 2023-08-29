string = input('enter some text :').split()
nums = [int(i) for i in string if i.isdigit()]
print(nums)
