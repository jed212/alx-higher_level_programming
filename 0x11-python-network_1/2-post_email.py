#!/usr/bin/python3
"""
Takes a URL and an email, sends a POST request, and displays the body of the response
"""

import urllib.parse
import urllib.request
import sys

if len(sys.argv) == 3:
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print("Your email is: {}".format(body))
else:
    print("Usage: ./2-post_email.py <URL> <email>")
