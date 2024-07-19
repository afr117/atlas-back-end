#!/usr/bin/python3
""" api project task 3 """

import json
import sys
import urllib.request

base = "https://jsonplaceholder.typicode.com/"


if __name__ == '__main__':
    out = {}

    with urllib.request.urlopen(base + "users") as response:
        users = json.loads(response.read())
    with urllib.request.urlopen(base + "todos") as response:
        todos = json.loads(response.read())

    for user in users:
        user_id = user["id"]
        user_username = user["username"]

        tasks = []
        for todo in todos:
            if todo['userId'] != user_id:
                continue
            task = {}
            task['task'] = todo['title']
            task['completed'] = todo['completed']
            task['username'] = user_username
            tasks.append(task)
        out[user_id] = tasks

    with open(f"todo_all_employees.json", "w") as f:
        json.dump(out, f)


def do_it_with_github():
    """ trying this task again with github typicode data """
    base = "https://raw.githubusercontent.com/typicode/" + \
        "jsonplaceholder/master/data.json"
    with urllib.request.urlopen(base) as response:
        data = json.loads(response.read())

    out = {}
    for user in data["users"]:
        user_id = user["id"]
        tasks = []
        for task in data["todos"]:
            if task["userId"] != user_id:
                continue
            task_dict = {}
            task_dict["task"] = task["title"]
            task_dict["completed"] = task["completed"]
            task_dict["username"] = user["username"]
            tasks.append(task_dict)
        out[user_id] = tasks

    out = json.dumps(out, indent=4)

    with open(f"todo_all_employees.json", "w") as f:
        f.write(out)
