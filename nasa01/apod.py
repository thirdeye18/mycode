#!/usr/bin/env python3
import requests
from pprint import pprint as pp # part of the standard library
# import webbrowser

## define some constants
NASAAPI = 'https://api.nasa.gov/planetary/apod?' # this is our API to call
MYKEY = 'api_key=CD0siZWVatruUArhyS2SnIwRSDWABF5uT00mA8cS' ## this is our api key

# MYKEY = open("nasa_key", "r").read().rstrip("\n")

## pretty print json
def main(date):
    """run-time code"""
    nasaapiobj = requests.get(NASAAPI + MYKEY + date) # call the webservice
    nasaread = nasaapiobj.json() # parse the JSON blob returned

    # Show converted json with just the date title and explanation
    print(f"{nasaread['date']}\n{nasaread['title']}\n{nasaread['explanation']}") # show converted JSON without pprint
    input('\nThis is converted json. Press ENTER to continue.') # pause for enter

    # Show Pretty Print json
    pp(nasaread) # this is pretty rint in action
    # pprint.pprint(convertedjson) # if you do a simple import pprint, the result is a long usage
    input('\nThis is pretty printed JSON. Press ENTER to continue.') # pause for ENTER

    # Print the description of the photo we are about to view
    print(nasaread['explanation']) # display the value for the key explanation
    print("Link to the APOD:", nasaread.get('hdurl',"No HD URL for today!"))


    #input('\nPress ENTER to view this photo of the day') # pause for ENTER
    # webbrowser.open(nasaread['hdurl']) # open in the webbrowser

# User input for the date the user would like
user_date = "&date=" + input("Please enter the date for the photo you would like. The date must be after 1995, and in the format yyyy-mm-dd.\n")


main(user_date)

# 
