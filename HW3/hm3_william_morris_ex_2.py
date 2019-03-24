"""
Homework 3, Exercise 2
William Morris
2/12/19
This program models a tic-tac-toe board but does not check if a
player has won.
"""

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# function to print the board out
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# intialize first turn as X
turn = 'X'

# loop through 9 times taking turns for each iteration
for i in range(9):
    printBoard(theBoard)
    incorrectInput = True

    # loop while user input is not valid
    while incorrectInput:
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        if move in theBoard.keys() and theBoard[move] == ' ':
            theBoard[move] = turn
            incorrectInput = False
        else:
            print('Please enter a valid input! \n')
    # switch turns
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'O'
#print the resulting board out
printBoard(theBoard)
