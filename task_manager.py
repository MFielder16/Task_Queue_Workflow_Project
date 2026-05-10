# Import json  and Path from pathlib for file handling and JSON serialization
import json
#optional: import os
import os
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
        if task is None:
            # Task does not exist
            return None

        # Transition map: current_status -> list of allowed next statuses
        transition_map = {
            "queued": ["in_progress"],
            "in_progress": ["completed", "failed"],
            # add other statuses and allowed transitions here as needed
        }

        allowed_next = transition_map.get(task.status, [])
        if new_status in allowed_next:
            task.status = new_status
            return task

        # Invalid transition
        return False

    # Add delete_task to Taskmanager
    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                return True

        return False

    # Add process_next_task to Taskmanager
    def process_next_task(self):
        for task in self.tasks:
            if task.status == "queued":
                task.status = "in_progress"
                return task
        return None

    # Add save_tasks_to_file to Taskmanager
    def save_to_file(self, filename = "tasks.json"):
        # Convert each Task object to a dictionary
        tasks_data = [task.to_dict() for task in self.tasks]

        # write the list of task dictionaries to a JSON file
        with open(filename, 'w') as file:
            json.dump(tasks_data, file, indent=4)

    # add load_tasks_from_file to Taskmanager
    def load_from_file(self, filename = "tasks.json"):

        # check if the file exists before trying to load
        if not os.path.exists(filename):
            print( f"File '{filename}' does not exist. No tasks loaded. Starting with an empty task list.")
            return False

        try:
            # open and read the JSON file
            with open(filename, 'r') as file:
                tasks_data = json.load(file)

            # rebuild Task objects from the list of task dictionaries
            self.tasks = [Task.from_dict(task_dict) for task_dict in tasks_data]

            #update the next_task_id to be one greater than the maximum existing task ID
            if self.tasks:
                max_id = max(task.task_id for task in self.tasks)
                self.next_task_id = max_id + 1

            print (f"Successfully loaded {len(self.tasks)} tasks from '{filename}'.")
            return True
            
            
               


        except json.JSONDecodeError:
            print(f"Error: File '{filename}' contains invalid JSON.")
            return False
         
        except Exception as e:
            print (f"An error occurred while loading tasks from '{filename}': {e}")
            return False
       


