#!/usr/bin/env python3

# importing required libraries
import urllib.request
import re

# Get url to search from the user
print("Where should we search? ")
url = input()

# get user input for the search phrase
print("Great! So we'll try to open this url " + str(url) + " to search for the phrase: ")
searchFor = input()

# use the urllib library to parse the URL entered by the user
searchMe = urllib.request.urlopen(url).read().decode("utf-8")

if re.search(searchFor, searchMe):
    print("Found a match!")
else:
    print("No match!")
