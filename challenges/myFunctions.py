# myFunctions.py>
## All the functions I have made for Python so far
## import to desired app using <from ~/mycode/myFunctions.py import *>
"""Function list: createList, intSearch, firstLastSearch, reverseList, removeSpaces, isPalindrome,  """

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
## Function will reverse a list or string that is passed as an argument, returns the input as a list, but reversed
## Function borrowed from method described in https://www.geeksforgeeks.org/python-reversing-list/

def reverseList(passed_list):
    return [ele for ele in reversed(passed_list)]

## removeSpaces
## Function accepts string input and removes spaces returning the non-space string
## Works by splitting the string to a list of words then joining them back together 

def removeSpaces(passed_str):
    return "".join(passed_str.split())

## isPalindrome
## Function takes a string as an argument to determine is it is a palindrome
## Case does not matter, but I have not figured out how to ignore spaces yet
## string input is converted to lower case and then converted to a list for comparing

def isPalindrome(passed_str):
    # convert the string being tested to lowercase and remove spaces
    mod_str = "".join(passed_str.split()).lower()
    # print for validation
    print("The transformed string is ", mod_str)
    
    # create a new variable to hold the reversed list and get the reversed list from function
    reverse_str = "".join(reverseList(mod_str))
    #print for validation
    print("The list reversed is ", reverse_str)
    
    # Convert the reversed list back to a string for comparing
    # backwards_str = "".join(backwards_list)
    # print for validation
    print("The modified string is ", mod_str)
    print("The reversed string is ", reverse_str)
    print("The passed string is ", passed_str)

    if mod_str == reverse_str:
        print("\nYou entered a palindrome")
    else:
        print("\nYou did not enter a palindrome")

## getWords
## reads in a file and returns a list of all the words in the file

def getWords(filename):

## countWords
## accepts the list of words from the previous function and counts the occurrences, returning a dictionary

def countWords(word_list):

## display
## displays the counts after accepting a dictionary containing those counts from count_words()

def display(word_dictionary):
