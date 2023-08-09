#!/usr/bin/python3
"""response header module"""
import requests
import sys

url = sys.argv[1]

response = requests.get(url)

# request_header_id = response.headers['X-Request-Id']
print(response.headers['X-Request-Id'])
