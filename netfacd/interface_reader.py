#!/usr/bin/env python3

# import netifaces to manipulate network interfaces
import netifaces

# print network interfaces
print(netifaces.interfaces())

# create for loop to iterate across network interfaces
for i in netifaces.interfaces():
    print('\n**************Details of Interface - ' + i + ' *********************')
    try: # This is a new line, you also need to indent lines below
        # pulling the MAC addresses from each of the interfaces
        print('MAC: ', end='')  # Label
        print(netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr'])
        print('IP: ', end='')   # Label
        print(netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr'])
    except: # To print error if try does not find data
        print('Could not collect adapter information')  # error message
