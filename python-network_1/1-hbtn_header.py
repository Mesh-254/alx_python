#!/usr/bin/python3
"""Header module"""
import requests
import sys

url = sys.argv[1]

if __name__ == "__main__":
    """
    takes in a URL, sends a request to the URL and displays
    the value of the X-Request-Id variable found in the header
    of the response
    """

    response = requests.get(url)

    request_header_id = response.headers['X-Request-Id']
    print(request_header_id)
