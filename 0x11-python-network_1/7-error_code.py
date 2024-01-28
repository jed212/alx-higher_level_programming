#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        print(response.text)
    except requests.exceptions.HTTPError as errh:
        print(f"Error code: {errh.response.status_code}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
