# TODO: Define the Task class
# Each task should store a title and a completed status (default False)
# Add a complete() method that marks the task as completed and prints confirmation

class Task:
    def __init__(self, description):
        self.description = description
        self.is_completed = False  # rename the attribute

    def complete(self):  # now complete() works as a method
        self.is_completed = True
        print(f"✅ Task '{self.description}' completed.")


class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"📌 Task '{task.description}' added to {self.name}.")
        
    def get_task_by_title(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None
