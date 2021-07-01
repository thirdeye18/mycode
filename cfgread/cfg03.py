#!/usr/bin/env python3

## create file object in "r"ead mode
with open("vlanconfig.cfg", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    # configlist = configfile.read().splitlines()
    configlist = [line.strip() for line in configfile]
    
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
# Pulling new line characters from the list

# Printing the number of lines fro the original file
print("vlanconfig.cfg contains ", len(configlist), "lines")
