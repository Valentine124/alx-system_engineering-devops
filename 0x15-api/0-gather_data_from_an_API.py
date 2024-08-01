#!/usr/bin/python3
"""Make a request to a server using request"""


import requests
from sys import argv

ID = argv[1]
URL = f'https://jsonplaceholder.typicode.com/todos?userId={ID}'

print(requests.get(URL).json())