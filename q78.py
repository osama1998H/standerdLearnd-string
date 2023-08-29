def count_char_position(str1):
    return sum(
        1
        for i in range(len(str1))
        if i in [ord(str1[i]) - ord('A'), ord(str1[i]) - ord('a')]
    )


str1 = input("Input a string: ")
print("Number of characters of the said string at same position as in English alphabet:")
print(count_char_position(str1))
