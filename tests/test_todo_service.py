"""
Unit tests for the TodoService.
"""
import pytest
from todo_app.todo_service import TodoService
from todo_app.todo import Todo


class TestTodoService:
    """Test cases for the TodoService."""

    def test_initial_state(self):
        """Test that TodoService starts with empty list and ID counter at 1."""
        service = TodoService()
        assert len(service.todos) == 0
        assert service.next_id == 1

    def test_add_todo(self):
        """Test adding a new todo."""
        service = TodoService()
        todo = service.add_todo("Test description")

        assert len(service.todos) == 1
        assert todo.id == 1
        assert todo.description == "Test description"
        assert todo.completed is False
        assert service.next_id == 2

    def test_add_todo_with_empty_description(self):
        """Test adding a todo with empty description raises ValueError."""
        service = TodoService()
        with pytest.raises(ValueError):
            service.add_todo("")

    def test_add_todo_with_whitespace_description(self):
        """Test adding a todo with whitespace-only description raises ValueError."""
        service = TodoService()
        with pytest.raises(ValueError):
            service.add_todo("   ")

    def test_get_all_todos_empty(self):
        """Test getting all todos when none exist."""
        service = TodoService()
        todos = service.get_all_todos()
        assert len(todos) == 0

    def test_get_all_todos_with_items(self):
        """Test getting all todos when they exist."""
        service = TodoService()
        service.add_todo("First todo")
        service.add_todo("Second todo")

        todos = service.get_all_todos()
        assert len(todos) == 2
        assert todos[0].description == "First todo"
        assert todos[1].description == "Second todo"

    def test_get_todo_by_id_found(self):
        """Test getting a todo by its ID when it exists."""
        service = TodoService()
        added_todo = service.add_todo("Test todo")
        found_todo = service.get_todo_by_id(added_todo.id)

        assert found_todo is not None
        assert found_todo.id == added_todo.id
        assert found_todo.description == "Test todo"

    def test_get_todo_by_id_not_found(self):
        """Test getting a todo by its ID when it doesn't exist."""
        service = TodoService()
        service.add_todo("Test todo")

        found_todo = service.get_todo_by_id(999)
        assert found_todo is None

    def test_update_todo_success(self):
        """Test successfully updating a todo's description."""
        service = TodoService()
        todo = service.add_todo("Original description")

        result = service.update_todo(todo.id, "Updated description")
        assert result is True

        updated_todo = service.get_todo_by_id(todo.id)
        assert updated_todo.description == "Updated description"

    def test_update_todo_not_found(self):
        """Test updating a non-existent todo returns False."""
        service = TodoService()
        result = service.update_todo(999, "Updated description")
        assert result is False

    def test_update_todo_invalid_id(self):
        """Test updating with invalid ID raises ValueError."""
        service = TodoService()
        with pytest.raises(ValueError):
            service.update_todo(-1, "Updated description")

    def test_update_todo_invalid_description(self):
        """Test updating with invalid description raises ValueError."""
        service = TodoService()
        todo = service.add_todo("Original")
        with pytest.raises(ValueError):
            service.update_todo(todo.id, "")

    def test_delete_todo_success(self):
        """Test successfully deleting a todo."""
        service = TodoService()
        todo = service.add_todo("Test todo")

        result = service.delete_todo(todo.id)
        assert result is True
        assert len(service.todos) == 0
        assert service.get_todo_by_id(todo.id) is None

    def test_delete_todo_not_found(self):
        """Test deleting a non-existent todo returns False."""
        service = TodoService()
        result = service.delete_todo(999)
        assert result is False

    def test_delete_todo_invalid_id(self):
        """Test deleting with invalid ID raises ValueError."""
        service = TodoService()
        with pytest.raises(ValueError):
            service.delete_todo(-1)

    def test_mark_complete_success(self):
        """Test successfully marking a todo as complete."""
        service = TodoService()
        todo = service.add_todo("Test todo")
        assert todo.completed is False

        result = service.mark_complete(todo.id)
        assert result is True

        completed_todo = service.get_todo_by_id(todo.id)
        assert completed_todo.completed is True

    def test_mark_complete_not_found(self):
        """Test marking a non-existent todo as complete returns False."""
        service = TodoService()
        result = service.mark_complete(999)
        assert result is False

    def test_mark_complete_invalid_id(self):
        """Test marking with invalid ID raises ValueError."""
        service = TodoService()
        with pytest.raises(ValueError):
            service.mark_complete(-1)

    def test_mark_incomplete_success(self):
        """Test successfully marking a todo as incomplete."""
        service = TodoService()
        todo = service.add_todo("Test todo")
        service.mark_complete(todo.id)  # First mark as complete
        assert todo.completed is True

        result = service.mark_incomplete(todo.id)
        assert result is True

        incomplete_todo = service.get_todo_by_id(todo.id)
        assert incomplete_todo.completed is False

    def test_mark_incomplete_not_found(self):
        """Test marking a non-existent todo as incomplete returns False."""
        service = TodoService()
        result = service.mark_incomplete(999)
        assert result is False

    def test_mark_incomplete_invalid_id(self):
        """Test marking with invalid ID raises ValueError."""
        service = TodoService()
        with pytest.raises(ValueError):
            service.mark_incomplete(-1)