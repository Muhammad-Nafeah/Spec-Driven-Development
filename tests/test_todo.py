"""
Unit tests for the Todo model.
"""
import pytest
from todo_app.todo import Todo


class TestTodo:
    """Test cases for the Todo data model."""

    def test_create_valid_todo(self):
        """Test creating a valid Todo object."""
        todo = Todo(id=1, description="Test description")
        assert todo.id == 1
        assert todo.description == "Test description"
        assert todo.completed is False

    def test_create_completed_todo(self):
        """Test creating a Todo object with completed status."""
        todo = Todo(id=1, description="Test description", completed=True)
        assert todo.id == 1
        assert todo.description == "Test description"
        assert todo.completed is True

    def test_invalid_id_negative(self):
        """Test creating a Todo with negative ID raises ValueError."""
        with pytest.raises(ValueError):
            Todo(id=-1, description="Test description")

    def test_invalid_id_zero(self):
        """Test creating a Todo with zero ID raises ValueError."""
        with pytest.raises(ValueError):
            Todo(id=0, description="Test description")

    def test_invalid_description_empty(self):
        """Test creating a Todo with empty description raises ValueError."""
        with pytest.raises(ValueError):
            Todo(id=1, description="")

    def test_invalid_description_whitespace_only(self):
        """Test creating a Todo with whitespace-only description raises ValueError."""
        with pytest.raises(ValueError):
            Todo(id=1, description="   ")

    def test_invalid_description_none(self):
        """Test creating a Todo with None description raises ValueError."""
        with pytest.raises(ValueError):
            Todo(id=1, description=None)

    def test_invalid_completed_type(self):
        """Test creating a Todo with non-boolean completed status raises ValueError."""
        with pytest.raises(ValueError):
            Todo(id=1, description="Test", completed="true")

    def test_mark_complete(self):
        """Test marking a todo as complete."""
        todo = Todo(id=1, description="Test description")
        assert todo.completed is False
        todo.mark_complete()
        assert todo.completed is True

    def test_mark_incomplete(self):
        """Test marking a todo as incomplete."""
        todo = Todo(id=1, description="Test description", completed=True)
        assert todo.completed is True
        todo.mark_incomplete()
        assert todo.completed is False

    def test_update_description(self):
        """Test updating a todo's description."""
        todo = Todo(id=1, description="Original description")
        assert todo.description == "Original description"
        todo.update_description("New description")
        assert todo.description == "New description"

    def test_update_description_empty(self):
        """Test updating a todo's description to empty raises ValueError."""
        todo = Todo(id=1, description="Original description")
        with pytest.raises(ValueError):
            todo.update_description("")

    def test_update_description_whitespace_only(self):
        """Test updating a todo's description to whitespace-only raises ValueError."""
        todo = Todo(id=1, description="Original description")
        with pytest.raises(ValueError):
            todo.update_description("   ")