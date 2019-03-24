"""
Homework 6, Exercise 2
William Morris
3/09/19
This program renames files with American-style dates to European-style
dates.
"""

#! python3

import shutil
import os
import re
# Regex pattern for getting the american date pattern
datePattern = re.compile(r"""^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    """, re.VERBOSE)
# search for files that are in the specified regex format and change them
for amerFilename in os.listdir('.'):
    date = datePattern.search(amerFilename)

    if date is None:
        continue
    # Get the date data from the regex used
    before = date.group(1)
    month = date.group(2)
    day = date.group(4)
    year = date.group(6)
    after = date.group(8)

    # reformat the date in euro format
    euroFilename = before + day + '-' + month + '-' + year + after

    # get present working directory and add to the file names created
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    print('Renaming "%s" to "%s". . .' % (amerFilename, euroFilename))

    # change the american format to the euro format
    shutil.move(amerFilename, euroFilename)
