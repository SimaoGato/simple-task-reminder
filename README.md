# SimpleTaskReminder

SimpleTaskReminder is a terminal-based task management tool that allows you to add, list, update, and search for tasks. It uses JSON files for data storage.

## Table of Contents
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)

## Features

- Add new tasks with descriptions, due dates, statuses, and priorities.
- List all existing tasks in a well-formatted table.
- Store tasks in a JSON file for persistence.
- Delete tasks (command not yet implemented).
- Update tasks (command not yet implemented).
- Search for tasks (command not yet implemented).

## Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/SimaoGato/SimpleTaskReminder.git
   cd SimpleTaskReminder

2. **Install Dependencies**
   ```bash
   pip3 install -r requirements.txt

3. **Run the Application**
   ```bash
   python3 task_manager.py -h

## Usage
To use SimpleTaskReminder, you can run the task_manager.py script in your terminal. Here are some example commands:

- **Add a new task**
  ```bash
  python3 task_manager.py -a -t 1 -n "Complete Project" -s "Pending" -D "2023-08-31" -p "High"

- **List tasks**
  ```bash
  python3 task_manager.py -l

- More commands are available, run python3 task_manager.py -h to see the full list.

## Commands
- `-a` or `--add`: Add a new task.
- `-l` or `--list`: List all tasks.
- `-t` or `--task_id`: Task ID (required for adding and updating tasks).
- `-n` or `--description`: Task description (required for adding and updating tasks).
- `-s` or `--status`: Task status (required for adding and updating tasks).
- `-D` or `--due_date`: Due date in the format "YYYY-MM-DD" (required for adding and updating tasks).
- `-p` or `--priority`: Task priority (required for adding and updating tasks).
