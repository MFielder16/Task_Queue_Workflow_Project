# This file defines the Task class, which represents a task in the task management system.
# Import datetime for handling task creation time
from datetime import date, datetime
class Task:
    # define the Task class with attributes for id, title, description, status, priority, and created_at
    # generate timestamp for created_at if not provided
    def __init__(self, title, description, status = "queued", priority = None, created_at = None,  _id = None):
        self.id = _id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.created_at = datetime.now()

    # method to return a string representation of the task
    def __str__(self):
        # return a string representation of the task with: id, title, description, status, priority, and created_at
        return f"Task ID: {self.id}\nTitle: {self.title}\nDescription: {self.description}\nStatus: {self.status}\nPriority: {self.priority}\nCreated At: {self.created_at}"
       
    
    
    




