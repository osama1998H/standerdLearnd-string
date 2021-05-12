def nonCommon(a, b):

    a = set(a)
    b = set(b)

    common = [a & b]

    result = [f for f in a if f not in common] + [f for f in b if f not in common]

    return ''.join(result)


print(nonCommon('osama', 'muhammed'))
