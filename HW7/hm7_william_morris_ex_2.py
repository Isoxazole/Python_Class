"""
Homework 7, Exercise 2
William Morris
3/17/19
This program searches the term the user has chosen as the argument in the
terminal. The program then searches that term on imgur and copies all
of the search result pictures to a pictures folder in the same directory.
"""

import re
import requests
import bs4
import sys
import os
import shutil
from urllib.request import urlretrieve

# Get website and make sure it's successful
res = requests.get('https://imgur.com/search/score?q=' + '+'.join(sys.argv[1:]))
res.raise_for_status()

# Parse through the html and select all of the img
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# img_tags = soup.find_all('img')
img_tags = soup.select('img')

# Get the image src address
urls = [img['src'] for img in img_tags]

# Create the pictures directory in current directory. If directory already
# exists, delete and remake directory
pictures = os.path.join(".", "pictures")
if os.path.exists(pictures):
    shutil.rmtree(pictures)
os.mkdir(pictures)

print("Copying pictures")
for url in urls:
    filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
    picturesPath = os.path.join(".", "pictures")
    urlretrieve("https:" + url, os.path.join(picturesPath, "%s" % (filename.group(1))))
print("Done!")
