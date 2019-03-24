"""
Homework 5, Exercise 4
William Morris
3/04/19
This program uses regular expressions to make sure the password string
is a strong password where there is at least 8 characters long, contains
both upper and lowercase characters, and has at least 1 digit.
"""
import re

passwordRegex = re.compile(
    r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")

def testPassword(password):
    if passwordRegex.match(password):
        return True
    else:
        return False
