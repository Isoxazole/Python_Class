"""
Homework 4, Exercise 4
William Morris
2/22/19
This program generates the same sequences of values as range(),
without creating a list object
"""



def genrange(stop, start = 0, step = 1):
    while start < stop:
        yield start
        start += step

