"""
Problem:  Find all pairs in an array of integers whose sum is equal to the given number.

Example 1   Input: [1, 2, 3], 5
            Output: [(2, 3), (3, 2)]

Example 2	Input: [1, 2, 3, 4, 5], 8
            Output: [(3, 5), (4, 4), (5, 3)]

Example 3	Input: [1, 2, 3], 8
            Output: []
"""


def find_pairs(array, num):
    returnArray = []
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] + array[j] == num:
                returnArray.append((array[i], array[j]))
    return returnArray
print(find_pairs([1, 2, 3, 4, 5], 8))

