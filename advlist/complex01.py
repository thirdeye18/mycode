#!/usr/bin/env python3

# create list1
list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]
# display list1
print(list1)
# display item 2 of list1
print(list1[1])
# create second list
list2 = ["juniper"]
# combine lists into single list
list1.extend(list2)
# display list1 with new addition
print(list1)
# create list3
list3 = ["10.1.0.1", "10.2.0.1", "10.3.0.1"]
# append list3 to list1
list1.append(list3)
# display list1
print(list1)
# display the list of IP addresses
print(list1[4])
# print just the first item in the list
print(list1[4][0] )

