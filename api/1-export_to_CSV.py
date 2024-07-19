#!/usr/bin/python3
"""
Script to fetch and export TODO list of an employee to a CSV file.
"""

import csv
import requests
import sys


def fetch_employee_todo_csv(employee_id):
    """Fetch TODO list for a given employee ID from JSONPlaceholder API and export to CSV."""
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

        csv_filename = f"{employee_id}.csv"

        with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for task in todos_data:
                row = [
                    employee_id,
                    username,
                    str(task.get('completed')).capitalize(),
                    task.get('title')
                ]
                writer.writerow(row)

        print(f"Data successfully exported to {csv_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_csv(employee_id)
