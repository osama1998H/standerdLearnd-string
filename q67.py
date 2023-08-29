from itertools import groupby


def remove_all_consecutive(str1):
    result_str = [key for key, group in groupby(str1)]
    return ''.join(result_str)


str1 = 'xxxxxyyyyy'
print(f"Original string:{str1}")
print(f"After removing consecutive duplicates: {str1}")
print(remove_all_consecutive(str1))
