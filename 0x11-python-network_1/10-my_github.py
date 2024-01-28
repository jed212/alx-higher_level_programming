#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    auth = (username, password)

    try:
        response = requests.get(url, auth=auth)
        data = response.json()
        print(data.get("id"))

    except ValueError:
        print("None")
