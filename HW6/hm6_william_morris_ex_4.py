"""
Homework 6, Exercise 4
William Morris
3/09/19
This program walks through a folder tree and searches for files
that have a file size of more than 100MB and prints them to the console.
"""


import os

# set the starting directory
startDir = os.path.abspath(os.sep)

# declare file size limit
limit = 100000000

for foldername, subfolders, filenames, in os.walk(startDir):
    for name in filenames:
        abspath = os.path.join(foldername, name)
        if os.path.getsize(abspath) > limit:
            print(abspath)
