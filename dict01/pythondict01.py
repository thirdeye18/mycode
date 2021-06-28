#!/usr/bin/env python3

# create a dictionary
switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

# display parts of the dictionary
print( switch["hostname"] )
print( switch["ip"], "\n" )

# request a fake key
#print( switch["lynx"] )

# request a fake key with .get()
print( "First test - .get()" )
print( switch.get( "lynx" ), "\n" )

print( "Second test - .get()" )
print( switch.get( "lynx", "THE KEY IS IN ANOTHER CASTLE" ), "\n" )

print( "Third test - .get()" )
print( switch.get( "version" ), "\n" )

# Prints the keys
print( "Fourth test - .keys()" )
print( switch.keys(), "\n" )

# Prints the values
print( "Fifth test - .values()" )
print( switch.values(), "\n" )

# .pop removes passed key and value pairs
print( "Sixth test - .pop()" )
print( switch.pop( "version" ) )
print( switch.keys() )
print( switch.values(), "\n" )

# Adding new value to the list
print( "Seventh test - Add a new value" )
switch["adminlogin"] = "karl08"
print( switch.keys() )
print( switch.values(), "\n" )

print( "Eighth test - Add a new value" )
switch["password"] = "qwerty"
print( switch.values() )
print( switch.keys() )
print( switch.values(), "\n" )

