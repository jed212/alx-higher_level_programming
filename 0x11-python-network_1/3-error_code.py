#!/usr/bin/python3
"""
Takes a URL, sends a request, and displays the body of the response or handles HTTPError
"""

import urllib.request
import urllib.error
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
else:
    print("Usage: ./3-error_code.py <URL>")
