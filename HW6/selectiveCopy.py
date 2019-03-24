"""
Homework 6, Exercise 3
William Morris
3/09/19
This program walks through a folder tree and searches for files
with a certain file extension then copies those files into a new folder
in the current directory
"""


import os
import shutil

# set the starting directory
startDir = os.path.abspath(os.sep)

# list of wanted file extensions
imageFiles = ['.PNG']

# Begin directory walk and copying pictures
pictures = os.path.join(".", "pictures")
os.mkdir(pictures)
for foldername, subfolders, filenames, in os.walk(startDir):
    for name in filenames:
        for fileType in imageFiles:
            if name.endswith(fileType.lower()):
                source = os.path.join(foldername, name)
                shutil.copy(source, pictures)
                print(source)
