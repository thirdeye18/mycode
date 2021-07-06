#!/usr/bin/env python3

# importing required libraries for http requests
import requests

# URL to request
url = "https://anapioficeandfire.com/api/characters/583"

resp = requests.get(url)
data = resp.json()

print(data["name"])

for i in data["aliases"]:
    print(i)
