from collections import OrderedDict


def remove_dublication(string: str):
    return ''.join(OrderedDict.fromkeys(string))


print(remove_dublication('osama muhammed'))
