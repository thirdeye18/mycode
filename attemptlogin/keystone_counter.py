#!/usr/bin/env python3

## Program goes line-by-line, searching for the expression - - - - -] Authorization failed 
## When the expression is encountered, counter is increased
## At the conclusion of the program, the value of the counter (or the number of failed logins) displayed to the user

# initialize counter for number of failed and successful login attempts
fail = 0
success = 0
# establish search string for failed login
search_fail = "- - - - -] Authorization failed"
search_succ = "-] Authorization failed"

# Open the log file in read mode
with open("keystone.common.wsgi", "r") as keystone:
    # loop throught the file searching for search term
    for x in keystone:
        if search_fail in x:
            fail +=1 #increment counter
            print("Failed login from ", x.split(" ")[-1])
        elif search_succ in x:
            success +=1

# printing the results of the search
print("There have been ", fail, " failed login attempts")
print("There have been ", success, "successfull login attempts")
