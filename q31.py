number = -12.999999
n_string = str(number)


def find_dot(num):
    num = str(num)
    return num.find(".")


print(find_dot(number))

if int(n_string[find_dot(number)+1]) < 5:
    print("%+.2f" % number)
else:
    print("%.2f" % number)
