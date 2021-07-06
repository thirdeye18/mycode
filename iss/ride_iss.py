#!/usr/bin/env python3
"""Alta3 || Tracking ISS"""

# original lab used these 2 libraries
# import urllib.request
# import json
import requests

## Define URL
MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    # simplifying code using only requests library
    helmetson = requests.get(MAJORTOM).json()

    ## Call the webservice
    ## groundctrl = urllib.request.urlopen(MAJORTOM)
    ## Put fileobject into helmet
    ## helmet = groundctrl.read()
    ## decode JSON to Python data structure
    ##helmetson = json.loads(helmet.decode('utf-8'))

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(helmetson)
    
    # printing the total number of people in space
    print("\n\nPeople in space: ", helmetson['number'])
    
    # putting the people into a list of dictionaries
    people = helmetson['people']
    
    # printing the name and craft for each of the people in space
    for i in people:
        print(f"{i['name']} on the {i['craft']}")
    
    # this would print the entire list of dictionaries in people
    # print(people)

main()
