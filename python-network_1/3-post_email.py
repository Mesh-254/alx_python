#!/usr/bin/python3
"""post module"""

import sys
import requests

url = sys.argv[1]
email = {"email":sys.argv[2]}

response = requests.post(url, data=email)

print("Your email is: {:}".format(response.text))