#!/usr/bin/python3
"""
This script gathers data from an API
and displays information about a specific
employee's tasks."""

# Import the necessary libraries
from sys import argv
import csv
import requests


# Get the user_id from the command line arguments
user_id = argv[1]

# Define the endpoint URL to access specific todo items for the user
url_todos = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

# Define the endpoint URL to get specific employee details
url_user = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

# Make an API request to retrieve user data
user_data = requests.get(url_user)
res = user_data.json()
username = res['username']

# Make an API request to retrieve todo items for the user
todos_response = requests.get(url_todos)
todo_data = todos_response.json()

# Initialize lists
csv_rows = []


# Iterate through the todo items and count completed and not completed tasks
for x in todo_data:
    title = x['title']
    taskStatus = x["completed"]

    # Format the row as a tuple
    row = (user_id, username, taskStatus, title)
    csv_rows.append(row)

with open(f'{user_id}.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)

    # Write the data rows
    writer.writerows(csv_rows)
