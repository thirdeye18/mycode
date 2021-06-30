#!/usr/bin/env python3

## Program checks the hostname against the expected value

hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
if hostname.lower() == "mtg":
    print("The hostname matches the expected configuration(mtg)")
else:
    print("The hostname does not match the expected configuration")

# Final message for exiting program, always prints
print("The program is exiting.")
