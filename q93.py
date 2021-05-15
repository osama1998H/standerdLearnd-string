string = input('enter some text :').split()
nums = []
for i in string:
    if i.isdigit():
        nums.append(int(i))
print(nums)
