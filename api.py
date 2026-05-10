# import FastAPI
from fastapi import FastAPI
from task_manager import TaskManager

# Create a FastAPI app instance
app = FastAPI(title = "Task Management API", description = "API for managing tasks in a task management system", version = "1.0")

# intialize a TaskManager instance to manage tasks
manager = TaskManager()

# Load exisiting tasks from file when the app starts
manager.load_from_file("my_task.json")

# Add a basic test route to verify the API is working
@app.get("/health")
def health_check():
    """Health check endpoint to verify the API is running."""
    return {
        "status": "healthy", 
        "message": "Task Management API is up and running!"
        }

@app.get("/")
def root():
    """Root endpoint - welcome message. 
    Alternative simple route to test if the app works. """
    return{
        "message": "Welcome to Task Queue Workfloow API", 
        "docs": "/docs" # linke to interactive API docs
        } 
