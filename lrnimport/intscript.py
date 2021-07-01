#!/usr/bin/env python3

from subprocess import call

# reveals those interfaces that are currently in an up state using call
call(["ip", "link", "show", "up"])
print("This program will check your interfaces.")

# prompt the user for an interface they'd like more detail on
interface = input("Enter an interface, like, ens3: ")

# use the input collected by the user to issue ip addr show dev, which will reveal IPv4 and IPv6 details
# use the input collected by the user to issue ip route show dev, which will reveal IPv4 and IPv6 details
call(["ip", "addr", "show", "dev", interface])
call(["ip", "route", "show", "dev", interface])

