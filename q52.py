from itertools import product


def all_col(string: str, n:int):
    return product(string, repeat=n)


# print(all_col('heol'))

for i in all_col("osama1998", 8):
    print(i)
