"""
Homework 7, Exercise 1
William Morris
3/17/19
This program opens a browser with all the top search results in a new tab.
"""

#! python3

import requests
import sys
import webbrowser
import bs4

print('Googling...')
# Search google using search term and check if successful
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Get search results from the search
soup = bs4.BeautifulSoup(res.text)

# finds all <a> elements that are within an element that has the r CSS clas
linkElems = soup.select('.r a')

# Open browser tab for each result where min is either 5 or total number of  links
#(which ever is lower)
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))