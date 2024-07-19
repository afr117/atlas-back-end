#!/usr/bin/python3
"""
Script to fetch and export TODO list of an employee to a JSON file.
"""

import json
import requests
import sys


def fetch_employee_todo_json(employee_id):
    """Fetch TODO list for a given employee ID from JSONPlaceholder API and export to JSON."""
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

        username = user_data.get('name')
        if not username:
            print("Username not found.")
            return

        json_filename = f"{employee_id}.json"
        
        # Prepare data for JSON
        tasks_list = [
            {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            }
            for task in todos_data
        ]

        # Write data to JSON file
        with open(json_filename, mode='w', encoding='utf-8') as file:
            json.dump({employee_id: tasks_list}, file, indent=4)

        print(f"Data successfully exported to {json_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_json(employee_id)
