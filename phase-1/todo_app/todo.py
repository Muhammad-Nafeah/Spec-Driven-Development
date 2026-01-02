"""
Todo data model representing a single task with description and completion status.
"""
from dataclasses import dataclass
from typing import Optional


@dataclass
class Todo:
    """
    Represents a single todo item with id, description, and completion status.
    """
    id: int
    description: str
    completed: bool = False

    def __post_init__(self):
        """
        Validate the Todo object after initialization.
        """
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError(f"ID must be a positive integer, got {self.id}")

        if not isinstance(self.description, str) or not self.description.strip():
            raise ValueError(f"Description must be a non-empty string, got {self.description}")

        if not isinstance(self.completed, bool):
            raise ValueError(f"Completed must be a boolean, got {self.completed}")

    def mark_complete(self) -> None:
        """Mark the todo as complete."""
        self.completed = True

    def mark_incomplete(self) -> None:
        """Mark the todo as incomplete."""
        self.completed = False

    def update_description(self, new_description: str) -> None:
        """Update the todo description with validation."""
        if not isinstance(new_description, str) or not new_description.strip():
            raise ValueError(f"Description must be a non-empty string, got {new_description}")
        self.description = new_description.strip()