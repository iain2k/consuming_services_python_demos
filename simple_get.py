#!/usr/bin/env

import requests

print('hi from requests')

url = 'https://talkpython.fm'

resp = requests.get(url)

print(resp)
