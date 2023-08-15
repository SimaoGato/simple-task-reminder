import argparse
import json
from datetime import datetime
from tabulate import tabulate

task_list = []

class Task:
    def __init__(self, task_id, description, status, due_date, priority):
        # Initialize a Task object with provided attributes
        self.task_id = task_id
        self.description = description
        self.status = status
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d')
        self.priority = priority

    def to_dict(self):
        # Return a dictionary representation of the Task object
        return {
            'task_id': self.task_id,
            'description': self.description,
            'status': self.status,
            'due_date': self.due_date.strftime('%Y-%m-%d'),
            'priority': self.priority
        }
    
    def __str__(self):
        return f'{self.task_id} | {self.description} | {self.status} | {self.due_date.strftime("%Y-%m-%d")} | {self.priority}'

def create_parser():
    parser = argparse.ArgumentParser(description='Terminal-Based Task Reminder')
    parser.add_argument('-a', '--add', help='Add a new task', action='store_true')
    parser.add_argument('-d', '--delete', help='Delete a task', action='store_true')
    parser.add_argument('-l', '--list', help='List all tasks', action='store_true')
    parser.add_argument('-u', '--update', help='Update a task', action='store_true')
    parser.add_argument('-S', '--search', help='Search for a task', action='store_true')
    
    # Add the single-letter flags for adding a task
    parser.add_argument('-t', '--task_id', help='Task ID')
    parser.add_argument('-n', '--description', help='Task description')
    parser.add_argument('-s', '--status', help='Task status')
    parser.add_argument('-D', '--due_date', help='Due date')
    parser.add_argument('-p', '--priority', help='Task priority')
    
    return parser

def save_tasks_to_file(tasks):
    task_list = [task.to_dict() for task in tasks]
    with open('data.json', 'w') as file:
        json.dump(task_list, file, indent=4)

def load_tasks_from_file():
    try:
        with open('data.json', 'r') as file:
            content = file.read()
            if content.strip() == '':
                return []
            task_list = json.loads(content)
            tasks = [Task(**task_dict) for task_dict in task_list]
            return tasks
    except FileNotFoundError:
        return []
    except json.decoder.JSONDecodeError as e:
        #print('Error decoding JSON:', e)
        return []

def add_task(task_id, description, status, due_date, priority):
    # Function to add a new task
    new_task = Task(task_id, description, status, due_date, priority)
    task_list = load_tasks_from_file()
    task_list.append(new_task)
    save_tasks_to_file(task_list)
    print(f'Task {task_id} added successfully!')

def delete_task():
    # Function to delete a task
    pass

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    task_data = [[
        task.task_id,
        task.description,
        task.status,
        task.due_date.strftime('%Y-%m-%d'),
        task.priority
    ] for task in tasks]

    headers = ["Task ID", "Description", "Status", "Due Date", "Priority"]
    print(tabulate(task_data, headers=headers, tablefmt="grid"))

def update_task():
    # Function to update a task
    pass

def search_task():
    # Function to search for a task
    pass

def main():
    parser = create_parser()
    args = parser.parse_args()

    task_list = load_tasks_from_file()  # Load tasks from file

    if args.add:
        if args.task_id and args.description and args.status and args.due_date and args.priority:
            add_task(args.task_id, args.description, args.status, args.due_date, args.priority)
        else:
            print("Missing arguments for adding a task.")
    elif args.delete:
        # Implement the delete command
        pass
    elif args.list:
        list_tasks(task_list)  # List all tasks
    elif args.update:
        # Implement the update command
        pass
    elif args.search:
        # Implement the search command
        pass
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
