#!/usr/bin/python3

"""
    Interacts with a REST API to get information about
    employees
"""


import csv
import json
import sys
import urllib.request

base = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    for employee_id in sys.argv[1:]:
        try:
            url = base + "users/{}".format(employee_id)
            with urllib.request.urlopen(url) as response:
                user_data = response.read()
            user = json.loads(user_data)
            username = user["username"]

            url = base + "todos?userId={}".format(employee_id)
            with urllib.request.urlopen(url) as response:
                todo_data = response.read().decode()
            todos = json.loads(todo_data)

            with open("{}.csv".format(employee_id),
                      "w", newline='') as csvfile:
                writer = csv.writer(csvfile, quotechar=None)

                for todo in todos:
                    writer.writerow([
                        f'"{employee_id}"',
                        f'"{username}"',
                        f'"{str(todo["completed"])}"',
                        f'"{todo["title"]}"'
                        ])
        except Exception as e:
            print(e)
