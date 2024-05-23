#!/usr/bin/python3

"""Contains a script that
make a request from an API
and print the reponse to the
std output
"""

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    todo_req = requests.get(f'https://jsonplaceholder.typicode'
                            f'.com/todos?userId={argv[1]}')
    user_re = requests.get(f'https://jsonplaceholder.typicode.com'
                           f'/users/{argv[1]}')

    user = user_re.json()
    todos = todo_req.json()
    FILE = 'USER_ID.csv'

    with open(FILE, 'w', newline='') as file:
        csv_writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
        for todo in todos:
            csv_writer.writerow([f'{user.get("id")}',
                                 f'{user.get("username")}',
                                 f'{todo.get("completed")}',
                                 f'{todo.get("title")}'])
