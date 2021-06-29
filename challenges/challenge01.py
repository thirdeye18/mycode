#!/usr/bin/env python3

## Does the number 6 appear?
## Given a list of ints determine if the number 6 is in the list.

## This function receives input from user and puts it into a list
## values must be seperated by a space
## pressing enter stops list input
def createList():
    # Instructions for the user
    print("Please input a list of integers to test. Follow each value with a space.\nPress enter following the last number to continue") 
    
    # take multiple inputs into list, iteration with for loop until enter pressed
    userTestList = [ int(x) for x in input().split()]
    # printing the users list  
    print("List to test:", userTestList)
    return userTestList

# Function to test the presence of a specified int
def intSearch(userTestList):
    searchValue = int(input("What number are you looking for? "))
    print("You are looking for:", searchValue)
    if searchValue in userTestList:
        print(searchValue, "is in the list")
    else:
        print(searchValue, "is not in the list")

# Start of main program calling functions defined above
def main():
    # use creatList() to generate testList
    #testlist = createList()
    #intSearch(testlist2)
    intSearch(createList())

main()
