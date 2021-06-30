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
## Function searches the passed list for the presence of a user specified int in the first or last spot

def intSearch(test_list):
    search_int = int(input("What integer are you looking for? "))
    print("You are looking for:", search_int)
    if search_int in test_list:
        print(search_int, "is in the list")
    else:
        print(search_int, "is not in the list")

## firstLastSearch
## Function searches the passed list fro the presence of a user specified int

def firstLastSearch(test_list):
    search_int = int(input("What integer are you looking for? "))
    print("You are looking for ", search_int, "in the first, or last spot." )
    if search_int == test_list[0] or search_int == test_list[len(test_list) - 1]:
        print("The first, or last digit is ", search_int)
    else:
        print("The first, or last digit is not ", search_int)

## reverseList
## Function will reverse a list that is passed as an argument

def reverseList(passed_list):
    passed_list.reverse()
    return passed_list

## isPalindrome
## Function takes a string as an argument to determine is it is a palindrome
## Spaces are ignored

def isPalindrome(passed_str):
    # also will be converting string to lowercase 
    str_list = list(passed_str.lower())
    print("The string as a list is ", str_list)
    backwards_str = reverseList(str_list)
    print("The list reversed is ", backwards_str)
    if str_list == backwards_str:
        print("\nThe words are a palindrome")
    else:
        print("\nThe words are not a palindrome")
