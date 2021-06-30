#!/usr/bin/env python3

"""Challenge01 from week 1 of Basic Python"""

# import all functions from myFunctions.py
# for the most part all methods will be come from myFunctions.py
from  myFunctions import *

## Part 1 *modified* Does the number 6 appear?
## Given a list of ints determine if the number 6 is in the list.

# createList passed to intSearch  
print("Creating integer list")
returned_list = createList()
print("\nPart 1a: Does a specified number appear in this list?")
intSearch(returned_list)

## Part 1b Given a list of int's determine if the first, or last value is a specified value

print("\nPart 1b: Does a specified number appear in the first, or last spot?")

# for simplicity I will use the list created in the first section
# call firstLastSearch() to evaluate the first and last digit of the list
firstLastSearch(returned_list)

## Part 2 Reverse the order of the list
print("\nThe original list ", returned_list)
# new variable for reversed list
# reverse_ints = returned_list.reverse
print("The reversed list is ", reverseList(returned_list))

##Part 3 Checking to see if a user supplied string is a palindrome
test_string = input("\nPlease enter a string to test - ")
print("You entered ", test_string)
isPalindrome(test_string)
