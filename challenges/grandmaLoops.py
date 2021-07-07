#!/usr/bin/env python3

## Initial example for a basic loop
# For every [dish] I find in the [sink] I'm going to [scream].
sink= ["bowl","plate","fork","mug"]
for dish in sink:
    print(f"There's a dirty {dish} in the sink! AAAAGGGHH!")

print('\n\n')   # providing space between challenges

## Bonus Challenge
## For every [toy] I find in the [kitchen] I'm going to [scream]!
## You may only identify whether or not a key/value pair in this dictionary is a toy by the VALUE.

# Provided dictionary list of items
kitchen= {"pan":"tool","spoon":"tool","yo-yo":"toy","banana":"food","jump rope":"toy","stove":"appliance"}

# loop pulls both key and value pair to iterate through, matches value to trigger response
for key, value  in kitchen.items():
    if value == 'toy':
        print(f"There is a {key} in the kitchen. AGGGGHHHHHHH!!!")
