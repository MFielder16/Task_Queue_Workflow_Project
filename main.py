from task_manager import TaskManager

manager = TaskManager()

manager.create_task(title="Buy groceries", description="Milk, Bread, Eggs", priority="high")
manager.create_task(title="Clean the house", description="Vacuum, Dust, Mop", priority="medium")
manager.create_task(title="Finish project", description="Complete the report and presentation", priority="high")
manager.create_task(title="Exercise", description="Go for a run or do yoga", priority="low")

print("All Tasks: \n")
for task in manager.get_all_tasks():
    print(task)



print("\nGet Task by ID (2): \n")
print(manager.get_task_by_id(2))

print("\nUpdate Task Status (ID 3 to 'in_progress'): \n")
print(manager.update_task_status(3, "in_progress"))
print("\nUpdate Task Status (ID 4 to 'completed'): \n")
print(manager.update_task_status(4, "completed"))