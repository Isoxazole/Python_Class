"""Homework2, Exercise 4
William Morris
1/29/2019
This program transposes a given 2d array by turning it clockwise 90degrees"""

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

transposedGrid = []

# transposes the grid above
for i in range(0, len(grid[0])):
    smallGrid = []
    for j in range(0, len(grid)):
        value = grid[j][i]
        smallGrid.append(value)
    transposedGrid.append(smallGrid)

# print the transposed grid
for x in transposedGrid:
    print(*x, sep="")
