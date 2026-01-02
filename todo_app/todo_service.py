"""
TodoService handles all business logic for managing todos in memory.
"""
from typing import List, Optional
from .todo import Todo


class TodoService:
    """
    Service class that manages todos in memory with all business logic.
    """

    def __init__(self) -> None:
        """Initialize the service with an empty list of todos and next ID counter."""
        self.todos: List[Todo] = []
        self.next_id: int = 1

    def add_todo(self, description: str) -> Todo:
        """
        Add a new todo with the given description.

        Args:
            description: The description of the new todo

        Returns:
            The created Todo object with assigned ID
        """
        if not isinstance(description, str) or not description.strip():
            raise ValueError("Description must be a non-empty string")

        todo = Todo(id=self.next_id, description=description.strip())
        self.todos.append(todo)
        self.next_id += 1
        return todo

    def get_all_todos(self) -> List[Todo]:
        """
        Get all todos in the system.

        Returns:
            List of all Todo objects
        """
        return self.todos.copy()  # Return a copy to prevent external modification

    def get_todo_by_id(self, todo_id: int) -> Optional[Todo]:
        """
        Get a specific todo by its ID.

        Args:
            todo_id: The ID of the todo to retrieve

        Returns:
            The Todo object if found, None otherwise
        """
        for todo in self.todos:
            if todo.id == todo_id:
                return todo
        return None

    def update_todo(self, todo_id: int, new_description: str) -> bool:
        """
        Update the description of an existing todo.

        Args:
            todo_id: The ID of the todo to update
            new_description: The new description for the todo

        Returns:
            True if the todo was found and updated, False otherwise
        """
        if not isinstance(todo_id, int) or todo_id <= 0:
            raise ValueError("Todo ID must be a positive integer")

        if not isinstance(new_description, str) or not new_description.strip():
            raise ValueError("Description must be a non-empty string")

        todo = self.get_todo_by_id(todo_id)
        if todo:
            todo.update_description(new_description)
            return True
        return False

    def delete_todo(self, todo_id: int) -> bool:
        """
        Delete a todo by its ID.

        Args:
            todo_id: The ID of the todo to delete

        Returns:
            True if the todo was found and deleted, False otherwise
        """
        if not isinstance(todo_id, int) or todo_id <= 0:
            raise ValueError("Todo ID must be a positive integer")

        for i, todo in enumerate(self.todos):
            if todo.id == todo_id:
                del self.todos[i]
                return True
        return False

    def mark_complete(self, todo_id: int) -> bool:
        """
        Mark a todo as complete.

        Args:
            todo_id: The ID of the todo to mark complete

        Returns:
            True if the todo was found and marked complete, False otherwise
        """
        if not isinstance(todo_id, int) or todo_id <= 0:
            raise ValueError("Todo ID must be a positive integer")

        todo = self.get_todo_by_id(todo_id)
        if todo:
            todo.mark_complete()
            return True
        return False

    def mark_incomplete(self, todo_id: int) -> bool:
        """
        Mark a todo as incomplete.

        Args:
            todo_id: The ID of the todo to mark incomplete

        Returns:
            True if the todo was found and marked incomplete, False otherwise
        """
        if not isinstance(todo_id, int) or todo_id <= 0:
            raise ValueError("Todo ID must be a positive integer")

        todo = self.get_todo_by_id(todo_id)
        if todo:
            todo.mark_incomplete()
            return True
        return False