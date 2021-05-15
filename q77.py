def number_of_substring(string):
    str_len = len(string)

    return (str_len * (str_len + 1)/2)


print(number_of_substring("w3resource"))
