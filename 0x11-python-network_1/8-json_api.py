#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    payload = {"q": q}

    try:
        response = requests.post(url, data=payload)
        data = response.json()

        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")

