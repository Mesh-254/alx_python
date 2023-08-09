#!/usr/bin/python3
"""Making request module"""
import requests

response = requests.get('https://alu-intranet.hbtn.io/status')

print(dir(response))
print("Body response:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))
