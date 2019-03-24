"""
Homework 4, Exercise 3
William Morris
2/22/19
This program uses a generator comprehension expression to find any n
pythogorian triplets.
"""

import math

def integers():
    i = 1
    while True:

        yield i
        i = i + 1


pyt = ((x, y, int(math.sqrt(x * x + y * y))) for y in integers()
       for x in range(1, y) if (math.sqrt(x * x + y * y)) % 1 == 0)


def take(n, seq):
    seq = iter(seq)

    result = []

    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result


print(take(10, pyt))
