import argparse

class Task:
    def __init__(self, task_id, description, status, due_date, priority):
        self.task_id = task_id
        self.description = description
        self.status = status
        self.due_date = due_date
        self.priority = priority
