"""Homework 2, Exercise 5
William Morris
1/29/2019
This program generates random bounds using the numbers 0-20. The program then
attempts to guess the number within the random bounds generated. """

import random

lowerBound = 0
upperBound = 0

# function to return a random integer between two bounds
def randomInteger():
    return random.randint(0, 20)

# loop until lower bound is < upper bound
while lowerBound >= upperBound:
    lowerBound = randomInteger()
    upperBound = randomInteger()

# function for the program to make a guess
def myGuess():
    guess = random.randint(lowerBound, upperBound)
    return guess

# define the secret number to guess
secretNumber = random.randint(lowerBound, upperBound)

print("I am thinking of a number between %d and %d:" % (lowerBound, upperBound))
guessNumber = 0
counter = 0
# give the user 6 guesses
for x in range(1, 7):
    print("Guess the number: ")
    guessNumber = myGuess()

    print("You guessed the number %s!" % guessNumber)
    counter += 1

    if guessNumber > secretNumber:
        print('Too High!\n')
    elif guessNumber < secretNumber:
        print("Too Low!\n")
    else:
        break
# check if the secret number has been guessed correctly
if guessNumber == secretNumber:
    print("\nYou got it, nice job! You guessed the "
          "secret number %d, in %d guesses!" % (secretNumber, counter))
else:
    print("\nToo bad so sad, you ran out of tries! "
          "The secret number was %d!" % secretNumber)

