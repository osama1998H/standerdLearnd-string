def intersection_of_two_string(str1, str2):
    result = ""
    for ch in str1:
        if ch in str2 and ch not in result:
            result += ch
    return result


str1 = 'Python3'
str2 = 'Python2.7'
print("Original strings:")
print(str1)
print(str2)
print("\nIntersection of two said String:")
print(intersection_of_two_string(str1, str2))
