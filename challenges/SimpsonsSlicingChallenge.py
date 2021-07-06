#!/usr/bin/env python3

## Simpsons Slicing Challenge

# create list for the first challenge
challenge = ["science", "turbo", ["goggles", "eyes"], "nothing"]

# create trial list
trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

# create nightmare challenge list
nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]
# Create variables to hold individual portions for nightmare
e = nightmare[0]["user"]["name"]["first"]
g = nightmare[0]["kumquat"]
n = nightmare[0]["d"]

# printing sliced portion of the list using fstring for challenge
print(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}!")

# printing sliced portion to nightmare
print(f"My {e}! The {g} do {n}!")
