#!/usr/bin/python3
"""
    api task 2
"""

import json
from json import decoder
import sys
import urllib.request

base = "https://jsonplaceholder.typicode.com/"


if __name__ == "__main__":
    for employee_id in sys.argv[1:]:
        url = base + "users/{}".format(employee_id)
        with urllib.request.urlopen(url) as response:
            user_data = response.read()
        user = json.loads(user_data)
        username = user["username"]

        url = base + "todos?userId={}".format(employee_id)
        with urllib.request.urlopen(url) as response:
            todo_data = response.read()

        todos = json.loads(todo_data)

        out = {}
        tasks = []
        for todo in todos:
            task = {}
            task["task"] = todo["title"]
            task["completed"] = todo["completed"]
            task["username"] = username
            tasks.append(task)
        out[employee_id] = tasks

        with open(f"{employee_id}.json", "w") as f:
            json.dump(out, f)
