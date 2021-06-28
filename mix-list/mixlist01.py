#!/usr/bin/env python3

# create a list containing 3 items
my_list = ["192.168.0.5", 5060, "UP"]

# create new list of 6 items
iplist = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

# print first item in the list
print("The first item in the list (IP): " + str(my_list[0]) )

# print the second item in the list
print("The second item in the list (PORT): " + str(my_list[1]) )

# print the third item in the list
print("The third item in the list (STATE): " + str(my_list[2]) )

# print only the IP addresses using f string
print(f"The IP adresses are: \n {iplist[3]} \n {iplist[4]}" )
