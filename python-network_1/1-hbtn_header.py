#!/usr/bin/python3
"""Response header value (X-Request-Id)"""
import requests
import sys

url = sys.argv[1]

response = requests.get(url)


request_header_id = response.headers['X-Request-Id']


print(request_header_id)
