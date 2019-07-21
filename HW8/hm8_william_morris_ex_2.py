"""
Homework 8, Exercise 2
William Morris
3/17/19
This program will attempt to brute-force attack the password of an
encrypted PDF file.
Total Time to find password = 2055.18 sec
Password = satisfaction
"""

import os
import PyPDF2
import time

# Define the file to unencrypt
fileName = "encrypted.pdf"

# Open pdf
pdfFileObj = open(fileName, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


# start timer
start = time.time()

# Loop through text file of words and try each one as lower and upper case
# If password is found, break loop
with open("dictionary.txt") as file:
    for word in file.readlines():
        word = word[:-1]
        if pdfReader.decrypt(word.lower()) == 1:
            print("The password is %s" % (word.lower()))
            break
        elif pdfReader.decrypt(word.upper()) == 1:
            print("The password is %s" % (word.upper()))
            break
end = time.time()

#print time to find password
print("Total time to find password: %s" % str(end - start))
