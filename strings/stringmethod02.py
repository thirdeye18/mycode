#!/usr/bin/env python3

"""Alta3 Research || Author: RZFeeser@alta3.com"""

def main():
    """Run-time code"""
    # create a small string
    lilstring = "Alta3 Research offers classes on Python coding"
    # split list
    newlist = lilstring.split(" ")
    print(newlist)

    # create a list of strings
    myiplist = ["192", "168", "0", "12"]
    # join the list of strings with . seperator
    singleip = ".".join(myiplist)
    print(singleip)

# call the main() function
main()

