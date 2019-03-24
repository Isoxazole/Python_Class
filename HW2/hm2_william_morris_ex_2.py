

"""Homework2, Exercise 2
William Morris
1/29/2019
This program prints the collatz sequence of the number inputted by the user. User input is checked to make sure it
is an integer"""


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


continueLoop = True

print("Please enter an integer:")

# loop until user enters a valid integer, check if user inputs string
while continueLoop:
    userInput = input()
    try:
        int(userInput)
    except ValueError:
        print("Please enter a valid integer!")
    else:
        continueLoop = False
        collatz(int(userInput))



