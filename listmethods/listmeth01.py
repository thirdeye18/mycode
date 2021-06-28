#!/usr/bin/env python3

# create initial list
proto = ["ssh", "http", "https"]
# create second list
protoa = ["ssh", "http", "https"]

print(proto)
# add dns to the end of the list
proto.append("dns")
# add dns to the end of second list
protoa.append("dns")

print(proto)

# create 3rd list
proto2 = [22, 80, 443, 53]
print(proto)

# pass proto2 as argument to the extend method
proto.extend(proto2)

# pass proto2 as argument to the append method
protoa.append(proto2)

print(protoa)


