"""
Homework 5, Exercise 3
William Morris
3/04/19
This program finds every phone number and email address in a long web
page or document by getting text of clipboard, using Regex to parse
the text and then pasting onto the clipboard
"""

import pyperclip
import re

phoneRegex = re.compile(r'''(
    (\d{3} | \(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != "":
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

for group in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy(("\n".join(matches)))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or emails addresses found')