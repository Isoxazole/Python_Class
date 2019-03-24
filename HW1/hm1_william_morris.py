"""Homework1
William Morris
1/29/2019
This is a 'security program' that will loop through a series of questions until the user answers all the questions
successfully. If the user fails to answer a question correctly, the program will restart. After answering all the
questions successfully, the secret message will be displayed!"""

import random

hasNotSucceeded = True
stagesComplete = 0

print("Hello, welcome to the new Security2000 system. This system is designed to protect a \nsecret message with the"
      "utmost protection. The secret message will be displayed only \nafter answer each "
      "and every question successfully. Good luck!\n")

print("Please enter your name: ")
userName = input()

print("\nHello %s, you seem to be new in our system, we'll go ahead \nand ask you a few question to make "
      "sure you have access to the secret message.\n" % userName)


# returns a random number between 1 and 9
def randomInt():
    return random.randint(1, 9)


# loops until
while hasNotSucceeded:

    word = "supercalifragilisticexpialidocious"
    print("Question 1: How many letters does the word '%s' have  in it?\n" % word)

    # get user input for how many letters and store as int
    userGuess = int(input())
    # Block 1 start / check if user guess is correct
    if userGuess == len(word):
        print("Correct!")
        stagesComplete = 1
    elif userGuess == 0:
        print("Are you even trying?")
    else:
        print("Incorrect! Try again...\n")
        # continue used to go to beginning of while loop
        continue
    # Block 1 ends
    print("Question 2: What are the first 10-digits of pi?")

    pi = 3.14159265359
    userGuess = float(input())

    # Block 2 start / ask user about guessing digits of pi
    if userGuess == pi:
        print("Correct!")
        stagesComplete = 2
    elif userGuess == 0:
        print("Are you even trying?")
    else:
        print("Incorrect! Try again...\n")
        continue
    # Block 2 ends

    # generate random integers for below for loop
    x = randomInt()
    y = randomInt()
    z = randomInt()

    print("Question 3: Challenge Mode!\n")

    loopCounter = 0
    # Block 3 start / prints three questions in sequence for user to answer
    for i in range(3):

        if i == 0:
            print("What is %d+%d-%d?" % (x, y, z))
            userGuess = int(input())
            if userGuess == (x + y - z):
                print("Correct!")
                loopCounter += 1
            else:
                print("Incorrect! Try again...")

                break
        elif i == 1:
            print("\nWhat is %d*%d//%d?" % (x, y, z))
            print("Hint: This uses integer division")
            userGuess = int(input())
            if userGuess == (x * y // z):
                print("Correct!")
                loopCounter += 1
            else:
                print("Incorrect! Try again...")

                break
        elif i == 2:
            print("What is %d+%d+%d?" % (x, y, z))
            userGuess = int(input())
            if userGuess == (x + y + z):
                print("Correct!")
                loopCounter += 1
                print(loopCounter)
            else:
                print("Incorrect! Try again...")

                break
    # Block 3 ends

    print(loopCounter)

    # check if user was able to answer all questions in for loop correctly
    if loopCounter != 3:
        continue
    else:
        stagesComplete = 3

    # check if user has completed the past 3 stages
    if stagesComplete == 3:
        print("\nCongratulations %s, you have answered all the questions correctly, "
              "the secret message is. . .\n" % userName)

        print("Before giving you the secret message, please enter any comments or suggestions \nat this time "
              "about the new Security 2000 system:")

        userSuggest = ""

        userSuggest += str(input())

        if userSuggest:
            print("The message you have entered is:\n %s" % userSuggest)
            print("\nNow, what you've been waiting for this whole time, the secret message is:")
            print("THE END IS NEAR!")
            print("\nThank you and please come again!")
            hasNotSucceeded = False
        # if user does not enter any text for suggestions, program restart (because no comments isn't very nice, right?
        else:
            print("Warning! Warning! ***User has not offered any comments or suggestions, "
                  "program will now restart!***\n")
            continue









