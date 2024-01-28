#!/usr/bin/python3
"""
Takes a URL, sends a request to thr url, and displays the value of the X-Request-Id variable in the header
"""

import urllib.request
import sys

if len(sys.argv) == 2:
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_request_id = response.info().get('X-Request-Id')
        print(x_request_id)
else:
    print("Usage: ./1-hbtn_header.py <URL>")
