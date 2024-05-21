#!/usr/bin/python3

"""
Contains a script that
make a request from an API
"""


import requests
from sys import argv

todo_req = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={argv[1]}')
user_re = requests.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')

user = user_re.json()
todos = todo_req.json()

total_task = len(todos)
task_done = 0
titles = []

for todo in todos:
    if todo["completed"] == True:
        task_done += 1
        titles.append(todo["title"])

print(f'Employee {user["name"]} is done with task({task_done}/{total_task}):')

for title in titles:
    print(f'\t {title}')
