# This file defines the Task class, which represents a task in the task management system.
# Import datetime for handling task creation time
from datetime import datetime
from typing import Optional, Any, Dict, Union

class Task:
    def __init__(
        self,
        title: str,
        description: str,
        task_id: Optional[int] = None,
        status: str = "queued",
        priority: Optional[int] = None,
        created_at: Optional[Union[float, int, str, datetime]] = None,
    ):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority

        # Normalize created_at: accept None, timestamp (int/float), ISO string, or datetime
        if created_at is None:
            self.created_at = datetime.now()
        elif isinstance(created_at, datetime):
            self.created_at = created_at
        elif isinstance(created_at, (int, float)):
            self.created_at = datetime.fromtimestamp(created_at)
        elif isinstance(created_at, str):
            try:
                # ISO 8601 string like "2026-05-03T12:34:56"
                self.created_at = datetime.fromisoformat(created_at)
            except Exception:
                # fallback: try parsing as numeric timestamp string
                self.created_at = datetime.fromtimestamp(float(created_at))
        else:
            # Fallback to now if type is unexpected
            self.created_at = datetime.now()

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the Task to a JSON-serializable dict.
        `created_at` is stored as a POSIX timestamp (float).
        """
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
            "created_at": self.created_at.timestamp(),
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        """
        Rebuild a Task from dictionary data produced by `to_dict`.
        Accepts `created_at` as timestamp (int/float) or ISO string; `__init__` normalizes it.
        """
        return cls(
            title=data.get("title"),
            description=data.get("description"),
            task_id=data.get("task_id"),
            status=data.get("status", "queued"),
            priority=data.get("priority"),
            created_at=data.get("created_at"),
        )

    # method to return a string representation of the task
    def __str__(self) -> str:
        # return a string representation of the task with: id, title, description, status, priority, and created_at
        return (
            f"Task ID: {self.task_id}\n"
            f"Title: {self.title}\n"
            f"Description: {self.description}\n"
            f"Status: {self.status}\n"
            f"Priority: {self.priority}\n"
            f"Created At: {self.created_at.isoformat()}\n"
        )




