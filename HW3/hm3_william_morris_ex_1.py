"""
Homework 3, Exercise 1
William Morris
2/12/19
This program counts the number of occurrences of each letter in a
string.
"""

import pprint

message = 'It was a bright cold day in April, ' \
          'and the clocks were striking thirteen'

count = {}

# adds the letter in the string to a hash and sets value equal to the count
for letter in message:
    letter = letter.upper()
    count.setdefault(letter, 0)
    count[letter] += 1
# print hash in pretty format
pprint.pprint(count)


