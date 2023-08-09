#!/usr/bin/python3
"""post module"""

import sys
import requests

url = sys.argv[1]
arg2 = {"email":sys.argv[2]}

response = requests.post(url, data=arg2)

print("Your email is: {:s}".format(response.text))
