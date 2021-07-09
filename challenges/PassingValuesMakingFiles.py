#!/usr/bin/python3
import random
## to write stdout to screen and a file
import logging

# data for use below
ship_name= "Bessie"
ship_type= "Intergalactic"
engines= "Dark Matter"
dark_matter_balls= 63
backup_engines= "Chemical"

# create a registration for our spaceship! Print out the following multi-line string with the appropriate data from above plugged in
# BONUS: Write this out to a file called ship_registration.txt instead of printing to screen!

print(f"Intergalactic Ship Registration:\n\n  name: {ship_name}\n  type: {ship_type}\n")
print(f"  engines:\n\n    type: {engines}\n      max capacity: {dark_matter_balls}")
print(f"    backup: {backup_engines}\n")

# Create the file
# and output every level since 'DEBUG' is used
# and remove all headers in the output
# using empty format='' prints exactly what is in the () to the file
logging.basicConfig(filename='ship_registration.txt', filemode = 'w', level=logging.DEBUG, format='')

# Logging with no format line will put the logging severity info in the message
# logging.basicConfig(filename='ship_registration.txt', filemode = 'w', level=logging.DEBUG)

logging.debug(f"Intergalactic Ship Registration:\n\n  name: {ship_name}\n  type: {ship_type}\n")
logging.info(f"  engines:\n\n    type: {engines}\n      max capacity: {dark_matter_balls}")
logging.warning(f"    backup: {backup_engines}\n")

# Choose your level of difficulty for the section below:
  # OPTION 1: 
    # Print out "Good news, everyone! We have another mission to accomplish:" to your screen.
    # Print out the appropriate delivery address below. The planet will be randomly selected!

  # OPTION 2:
    # To a file called "order.txt", add "Good news, everyone! We have another mission to accomplish:"
    # Also to the file "order.txt", add the appropriate delivery address below. The planet will be randomly selected!

## Picking random planet for delivery
planet= random.choice(["Earth", "Luna Park", "Omicron Persei 8", "Cineplex 14"])
with open('order.txt', 'a') as f:
    print("Good news, everyone! We have another mission to accomplish:", file = f)
    if planet == "Luna Park":
        # if the delivery is to Luna Park, print the following:
        print("Delivery to Luna Park\nContents: Prizes for the claw crane\nDelivery at: Luna Park, Moon", file = f)
    elif planet == "Cineplex 14":
        # if the delivery is to Cineplex 14, print the following:
        print("Delivery to Cineplex 14\nContents: Popcorn\nDelivery at: Cineplex 14", file = f)
    elif planet == "Omicron Persei 8":
        print("Delivery to Omicron Persei 8\nContents: Candy hearts\nDelivery at: Omicron Persei 8", file = f)
    else:
        # if not any of those destinations, the delivery is to Earth:
        print("Delivery to Earth\nContents: R&R / Time Off\nDelivery at: HQ", file = f)

