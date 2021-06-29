# myFunctions.py>
## All the functions I have made for Python so far
## import to desired app using <from ~/mycode/myFunctions.py import *>

## createIntList.py
## Function creates a list of integers from user input
## values must be seperated by a space
## pressing enter stops list input
## No input validation yet

def createList():
    # Instructions for the user
    print("Please input a list of integers to test. Follow each value with a space.\nPress enter following the last number to continue")

    # take multiple inputs into list, iteration with for loop until enter pressed
    int_list = [ int(x) for x in input().split()]
    # printing the users list
    print("List to test:", int_list)
    return int_list

## intSearch
## Function searches the passed list fro the presence of a user specified int

def intSearch(test_list):
    search_int = int(input("What integer are you looking for? "))
    print("You are looking for:", search_int)
    if search_int in test_list:
        print(search_int, "is in the list")
    else:
        print(search_int, "is not in the list")
