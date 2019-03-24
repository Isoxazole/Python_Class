"""Homework2, Exercise 3
William Morris
1/29/2019
This program takes a list value as an argument and returns a string with all the
items separated by a comma and a space, with 'and' inserted before the last item"""


def spacer(listValues):
    listValues[-1] = "and " + listValues[-1]
    return ", ".join(listValues)


spam = ['apples', 'bananas', 'tofu', 'cats']

print(spacer(spam))


