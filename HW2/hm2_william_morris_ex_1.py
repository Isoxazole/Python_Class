"""Homework2, Exercise 1
William Morris
1/29/2019
This program prints the collatz sequence of the number inputted by the user."""


def collatz(number):
    if number == 1:
        print(number)
        return 1
    elif number % 2 == 0:
        print(number)
        return collatz(int(number/2))
    else:
        print(number)
        return collatz(int((number*3) + 1))


print("Please enter an integer:")
userInput = int(input())

collatz(userInput)
