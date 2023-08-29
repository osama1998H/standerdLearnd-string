string = input("enter the text: ").split()
sub_string = input("text for search: ")

count = sum(1 for i in string if i == sub_string)
print(f"({sub_string}) repeat {count} times")
