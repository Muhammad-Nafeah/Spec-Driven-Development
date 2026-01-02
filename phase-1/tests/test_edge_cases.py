"""
Tests for edge cases identified in the specification.
"""
import pytest
import io
from contextlib import redirect_stdout, redirect_stderr
from unittest.mock import patch
from todo_app.todo_service import TodoService
from todo_app.cli_handler import handle_add, handle_list, handle_update, handle_delete, handle_complete, handle_incomplete


class TestEdgeCases:
    """Test edge cases as identified in the specification."""

    def test_update_nonexistent_todo(self):
        """What happens when trying to update a todo that doesn't exist?"""
        service = TodoService()
        result = service.update_todo(999, "New description")
        assert result is False

    def test_delete_nonexistent_todo(self):
        """What happens when trying to delete a todo that doesn't exist?"""
        service = TodoService()
        result = service.delete_todo(999)
        assert result is False

    def test_mark_nonexistent_todo_complete(self):
        """What occurs when trying to mark a non-existent todo as complete?"""
        service = TodoService()
        result = service.mark_complete(999)
        assert result is False

    def test_mark_nonexistent_todo_incomplete(self):
        """What occurs when trying to mark a non-existent todo as incomplete?"""
        service = TodoService()
        result = service.mark_incomplete(999)
        assert result is False

    def test_empty_todo_list_display(self):
        """How does the system behave when there are no todos to display?"""
        service = TodoService()
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            class MockArgs:
                command = 'list'

            handle_list(service, MockArgs())

        output = captured_output.getvalue()
        assert "No todos found." in output

    def test_invalid_description_handling(self):
        """How does the system handle empty or invalid todo descriptions?"""
        service = TodoService()

        # Test adding with empty description
        with pytest.raises(ValueError):
            service.add_todo("")

        # Test adding with whitespace-only description
        with pytest.raises(ValueError):
            service.add_todo("   ")

        # Test updating with empty description
        todo = service.add_todo("Valid description")
        with pytest.raises(ValueError):
            service.update_todo(todo.id, "")

        # Test updating with whitespace-only description
        with pytest.raises(ValueError):
            service.update_todo(todo.id, "   ")

    def test_invalid_id_handling(self):
        """How does the system handle invalid IDs?"""
        service = TodoService()

        # Test with negative IDs
        with pytest.raises(ValueError):
            service.update_todo(-1, "New description")

        with pytest.raises(ValueError):
            service.delete_todo(-1)

        with pytest.raises(ValueError):
            service.mark_complete(-1)

        with pytest.raises(ValueError):
            service.mark_incomplete(-1)

        # Test with zero ID
        with pytest.raises(ValueError):
            service.update_todo(0, "New description")

        with pytest.raises(ValueError):
            service.delete_todo(0)

        with pytest.raises(ValueError):
            service.mark_complete(0)

        with pytest.raises(ValueError):
            service.mark_incomplete(0)

    def test_cli_invalid_input_handling(self):
        """Test CLI handling of invalid inputs."""
        service = TodoService()

        # Test CLI add with empty description
        captured_error = io.StringIO()
        with redirect_stderr(captured_error):
            class MockArgs:
                command = 'add'
                description = ['']

            with pytest.raises(SystemExit):
                handle_add(service, MockArgs())

        error_output = captured_error.getvalue()
        assert "Error" in error_output

        # Test CLI update with empty description
        captured_error = io.StringIO()
        with redirect_stderr(captured_error):
            class MockArgs:
                command = 'update'
                id = 999
                description = ['']

            with pytest.raises(SystemExit):
                handle_update(service, MockArgs())

        error_output = captured_error.getvalue()
        assert "Error" in error_output