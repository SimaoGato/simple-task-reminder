import argparse

class Task:
    def __init__(self, task_id, description, status, due_date, priority):
        self.task_id = task_id
        self.description = description
        self.status = status
        self.due_date = due_date
        self.priority = priority

def create_parser():
    parser = argparse.ArgumentParser(description='Terminal-Based Task Reminder')
    parser.add_argument('-a', '--add', help='Add a new task', action='store_true')
    parser.add_argument('-d', '--delete', help='Delete a task', action='store_true')
    parser.add_argument('-l', '--list', help='List all tasks', action='store_true')
    parser.add_argument('-u', '--update', help='Update a task', action='store_true')
    parser.add_argument('-s', '--search', help='Search for a task', action='store_true')
    return parser
