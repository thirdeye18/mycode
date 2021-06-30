#!/usr/bin/env python3

# create a dictionary of strings
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# loop across the keys and values
for x in range(len(farms)):
    print("\nFarm data: ", farms[x-1])   # newline, print the name of the farm


#    for values in farms.keys(keys):
#        print("\tAnimals: ", values, end=", ")    #printing the values from the provided dictionary key, start tabbed, seperate with comma


print("\nOur loop has ended.") # print when loop has finished

