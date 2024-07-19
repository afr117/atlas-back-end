#!/usr/bin/python3
"""
Script to fetch and display TODO list progress of an employee from a given API.
"""

import requests
import sys


def fetch_employee_todo(employee_id):
    """Fetch TODO list for a given employee ID from JSONPlaceholder API."""
    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos?userId={employee_id}'

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        user_data = user_response.json()
        todos_data = todos_response.json()

        if not user_data or not todos_data:
            print("No data found.")
            return

        employee_name = user_data.get('name')
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task.get('completed')]

        print(f"Employee {employee_name} is done with tasks({len(done_tasks)}
        /{total_tasks}):")
        for task in done_tasks:
            print(f"\t {task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo(employee_id)
