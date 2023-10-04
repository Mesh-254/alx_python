#!/usr/bin/python3

"""
This script gathers data from an API
and displays information about a specific
employee's tasks.
"""

# Import the necessary libraries
from sys import argv
import csv
import json
import requests

# Get the user_id from the command line arguments
user_id = argv[1]

# Define the endpoint URL to access specific todo items for the user
url_todos = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

# Define the endpoint URL to get specific employee details
url_user = f"https://jsonplaceholder.typicode.com/users/{user_id}"

# Make an API request to retrieve user data
user_data = requests.get(url_user)
res = user_data.json()
username = res['username']

# Make an API request to retrieve todo items for the user
todos_response = requests.get(url_todos)
todo_data = todos_response.json()

# Initialize an empty list to store rows
csv_rows = []

# Iterate through the todo items and build rows for the CSV
for x in todo_data:
    task_id = str(x['id'])
    title = x['title']
    taskStatus = str(x["completed"])

    # Format the row as a string
    row = f'"{user_id}","{username}","{taskStatus}","{title}"'

    # Append the formatted row to csv_rows
    csv_rows.append(row)

# Define the CSV file name
csv_file = f'{str(user_id)}.csv'

# Write the contents to the CSV file
with open(csv_file, 'w', encoding='utf-8', newline='') as f:
    # Write the data rows
    for row in csv_rows:
        f.write(row + '\n')
