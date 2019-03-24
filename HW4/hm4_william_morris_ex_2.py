"""
Homework 4, Exercise 2
William Morris
2/22/19
This program uses an iterator class that takes a list and iterates it
from the reverse direction.
"""

class Reverseiter:
    def __init__(self, n):
        self.i = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.n)+1:
            result = self.n[-self.i]
            self.i += 1
            return result
        else:
            raise StopIteration()

something = Reverseiter([1, 2, 3, 4])

yo = Reverseiter([1, 2, 3, 4])

print(next(yo))
print(next(yo))
print(next(yo))
print(next(yo))