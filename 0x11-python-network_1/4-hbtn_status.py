#!/usr/bin/python3
import requests

url = 'https://alx-intranet.hbtn.io/status'
response = requests.get(url)

print('Body response:')
print(f'    - type: {type(response.text)}')
print(f'    - content: {response.text}')
