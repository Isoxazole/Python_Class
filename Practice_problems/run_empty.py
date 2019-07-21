"""
Problem: Write a function to find if two strings are rotations of each other.

Example 1   Input: "ABC", "BCA"
            Output: True

Example 2	Input: "ABC", "CAB"
            Output: True

Example 3	Input: "ABC", "CBA"
            Output: False
"""

def string_rotation(var1, var2):
    print(var1[::-1])
    if var1[::-1] == var2:
        return True

print(string_rotation("ABC", "BCA"))
