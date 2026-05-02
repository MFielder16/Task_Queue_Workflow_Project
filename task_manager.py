# import the Task class from the task module
from task import Task
# This module defines the TaskManager class, which is responsible for managing and executing tasks in a concurrent environment.
class TaskManager:
    # create a method to initialize a list for Task objects and a counter for generating unique task IDs
    def __init__(self):
        # create a list comprehension to initialize an empty list for Task objects and set a counter to 1 for generating unique task IDs
        self.tasks = []
        self.next_task_id = 1
        

        
    # create method called create_task accepts parameters for title, description, and priority, and creates a new Task object with a unique task ID
    def create_task(self, title, description, priority):
        # created a Task object with the provided title, description, and priority, and a unique task ID generated from the counter
        # append the new Task object to the tasks list and increment the counter for the next task ID
        self.tasks.append(Task(title=title, description=description, task_id = self.next_task_id, priority=priority))
        self.next_task_id += 1
        # return the newly created Task object
        return self.tasks[-1]

    # created method called get_all_tasks that returns the list of all Task objects
    def get_all_tasks(self):
        # return the list of all Task objects
        return self.tasks

    # create method called get_task_by_id that accepts a task ID as a parameter and returns the corresponding Task object if found, or None if not found
    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    # Add update_task_status to Taskmanager
    def update_task_status(self, task_id, new_status):
        task = self.get_task_by_id(task_id)
        if task:
            task.status = new_status
            return task
        return None

    # Add delete_task to Taskmanager
    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                return True

        return False
       


