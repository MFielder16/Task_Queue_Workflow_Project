from task_manager import TaskManager

manager = TaskManager()

manager.create_task(title="Buy groceries", description="Milk, Bread, Eggs", priority="high")
manager.create_task(title="Clean the house", description="Vacuum, Dust, Mop", priority="medium")
manager.create_task(title="Finish project", description="Complete the report and presentation", priority="high")
manager.create_task(title="Exercise", description="Go for a run or do yoga", priority="low")

# save all tasks to a JSON file
manager.save_to_file("my_task.json")

# create one new task
#new_task = manager.create_task(title="Read a book", description="Read 'The Great Gatsby'", priority="medium")
#print(new_task.task_id)
#print(new_task)

# create a new TaskManager instance and load tasks from the JSON file
success = TaskManager()
old_tasks = success.load_from_file("my_task.json")
print(old_tasks)
for task in success.get_all_tasks():
    print(task)
newer_task = success.create_task(title="Write code", description="Work on the task management system", priority="high")
print(newer_task.task_id)

#print("All Tasks: \n")
#for task in manager.get_all_tasks():
#   print(task)
    
# Test get_task_by_id with valid and invalid IDs
#print("\nGet Task by ID (2): \n")
#print(manager.get_task_by_id(2))
# Test update_task_status with valid and invalid status transitions    
#print("\nUpdate Task Status (ID 1 to 'in_progress'): \n")
#print(manager.update_task_status(1, "in_progress"))
#print("\nUpdate Task Status (ID 2 to 'failed'): \n")
#print(manager.update_task_status(2, "failed"))
#print("\nUpdate Task Status (ID 3 to 'completed'): \n")
#print(manager.update_task_status(3, "completed"))
#print("\nUpdate Task Status (ID 1 to 'completed'): \n")
#print(manager.update_task_status(1, "completed"))
# Test update_task_status with missing task ID
#print("\nUpdate Task Status (ID 5 to 'completed'): \n")
#print(manager.update_task_status(5, "completed"))

# print all tasks after status updates
#for task in manager.get_all_tasks():
#    print(task)

#manager.delete_task(2)  # Delete task with ID 2
#manager.delete_task(5)# Attempt to delete a non-existent task)
#print("\nAll Tasks after deletion: \n")
#for task in manager.get_all_tasks():
#    print(task)
#print("\nProcess Next Task: \n")
#print(manager.process_next_task())  # Process the next task in the queue
#print("\nProcess Next Task: \n")
#print(manager.process_next_task())  # Process the next task in the queue
#print("\nAll Tasks after processing next task: \n")
#for task in manager.get_all_tasks():
#   print(task)