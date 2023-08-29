
def bytearray_to_hexadecimal(list_val):
    return ''.join('{:02x}'.format(x) for x in list_val)


list_val = [710, 12, 45, 67, 109]
print("Original Bytearray :")
print(list_val)
print("\nHexadecimal string:")
print(bytearray_to_hexadecimal(list_val))