string = input("enter the text: ").split()
sub_string = input("text for search: ")

count = 0

for i in string:
    if i == sub_string:
        count += 1
print(f"({sub_string}) repeat {count} times")
