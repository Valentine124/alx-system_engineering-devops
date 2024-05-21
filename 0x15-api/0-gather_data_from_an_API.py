#!/usr/bin/python3

"""Contains a script that
make a request from an API
and print the reponse to the
std output
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    todo_req = requests.get(f'https://jsonplaceholder.typicode'
                            f'.com/todos?userId={argv[1]}')
    user_re = requests.get(f'https://jsonplaceholder.typicode.com'
                           f'/users/{argv[1]}')

    user = user_re.json()
    todos = todo_req.json()

    total_task = len(todos)
    task_done = 0
    titles = []

    for todo in todos:
        if todo.get("completed") is True:
            task_done += 1
            titles.append(todo.get("title"))

    print(f'Employee {user.get("name")} is done '
          f'with tasks({task_done}/{total_task}):')

    for title in titles:
        print(f'\t {title}')
