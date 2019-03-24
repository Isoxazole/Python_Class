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

fileName = "encrypted.pdf"

pdfFileObj = open(fileName, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


os.path.join(".", fileName)

# start timer
start = time.time()

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

print("Total time to find password: %s" % str(end - start))
