"""
Tests to validate all functional requirements are met.
FR-001: System MUST allow users to add new todo items with a description
FR-002: System MUST display all current todo items in a readable format
FR-003: System MUST allow users to update existing todo items with new descriptions
FR-004: System MUST allow users to delete specific todo items from the list
FR-005: System MUST allow users to mark todos as complete or incomplete
FR-006: System MUST store all todo data in memory only (no persistent storage)
FR-007: System MUST provide a command-line interface for all operations
FR-008: System MUST handle invalid inputs gracefully and provide helpful error messages
FR-009: System MUST maintain data integrity during all operations (no corruption)
"""
import pytest
import io
from contextlib import redirect_stdout, redirect_stderr
from todo_app.todo_service import TodoService
from todo_app.cli_handler import handle_add, handle_list, handle_update, handle_delete, handle_complete, handle_incomplete


class TestFunctionalRequirements:
    """Test all functional requirements from the specification."""

    def test_fr_001_add_todo(self):
        """FR-001: System MUST allow users to add new todo items with a description"""
        service = TodoService()
        initial_count = len(service.get_all_todos())

        todo = service.add_todo("Test description")

        assert len(service.get_all_todos()) == initial_count + 1
        assert todo.description == "Test description"
        assert todo.id > 0

    def test_fr_002_display_todos(self):
        """FR-002: System MUST display all current todo items in a readable format"""
        service = TodoService()
        service.add_todo("First todo")
        service.add_todo("Second todo")

        todos = service.get_all_todos()
        assert len(todos) == 2
        assert todos[0].description == "First todo"
        assert todos[1].description == "Second todo"

    def test_fr_003_update_todo(self):
        """FR-003: System MUST allow users to update existing todo items with new descriptions"""
        service = TodoService()
        todo = service.add_todo("Original description")

        success = service.update_todo(todo.id, "Updated description")

        assert success is True
        updated_todo = service.get_todo_by_id(todo.id)
        assert updated_todo.description == "Updated description"

    def test_fr_004_delete_todo(self):
        """FR-004: System MUST allow users to delete specific todo items from the list"""
        service = TodoService()
        todo = service.add_todo("Test todo")
        initial_count = len(service.get_all_todos())

        success = service.delete_todo(todo.id)

        assert success is True
        assert len(service.get_all_todos()) == initial_count - 1
        assert service.get_todo_by_id(todo.id) is None

    def test_fr_005_mark_complete_incomplete(self):
        """FR-005: System MUST allow users to mark todos as complete or incomplete"""
        service = TodoService()
        todo = service.add_todo("Test todo")

        # Mark as complete
        success_complete = service.mark_complete(todo.id)
        completed_todo = service.get_todo_by_id(todo.id)

        assert success_complete is True
        assert completed_todo.completed is True

        # Mark as incomplete
        success_incomplete = service.mark_incomplete(todo.id)
        incomplete_todo = service.get_todo_by_id(todo.id)

        assert success_incomplete is True
        assert incomplete_todo.completed is False

    def test_fr_006_memory_only_storage(self):
        """FR-006: System MUST store all todo data in memory only (no persistent storage)"""
        service1 = TodoService()
        service1.add_todo("Test todo")

        # Create a new service instance (simulating application restart)
        service2 = TodoService()

        # Data should not persist between instances (in-memory only)
        assert len(service2.get_all_todos()) == 0

        # Original service still has the data
        assert len(service1.get_all_todos()) == 1

    def test_fr_007_command_line_interface(self):
        """FR-007: System MUST provide a command-line interface for all operations"""
        # Test CLI add functionality
        service = TodoService()

        class MockArgsAdd:
            command = 'add'
            description = ['CLI', 'test', 'todo']

        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            handle_add(service, MockArgsAdd())

        output = captured_output.getvalue()
        assert "Added todo" in output
        assert len(service.get_all_todos()) == 1

        # Test CLI list functionality
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            class MockArgsList:
                command = 'list'
            handle_list(service, MockArgsList())

        output = captured_output.getvalue()
        assert "CLI test todo" in output

    def test_fr_008_handle_invalid_inputs(self):
        """FR-008: System MUST handle invalid inputs gracefully and provide helpful error messages"""
        service = TodoService()

        # Test invalid input for add (empty description)
        captured_error = io.StringIO()
        with redirect_stderr(captured_error):
            class MockArgs:
                command = 'add'
                description = ['']

            with pytest.raises(SystemExit):
                handle_add(service, MockArgs())

        error_output = captured_error.getvalue()
        assert "Error" in error_output

        # Test invalid input for update (non-existent ID)
        captured_error = io.StringIO()
        with redirect_stderr(captured_error):
            class MockArgs:
                command = 'update'
                id = 999
                description = ['new', 'description']

            with pytest.raises(SystemExit):
                handle_update(service, MockArgs())

        error_output = captured_error.getvalue()
        assert "not found" in error_output

    def test_fr_009_data_integrity(self):
        """FR-009: System MUST maintain data integrity during all operations (no corruption)"""
        service = TodoService()

        # Add multiple todos
        todo1 = service.add_todo("First todo")
        todo2 = service.add_todo("Second todo")
        todo3 = service.add_todo("Third todo")

        # Perform various operations
        service.mark_complete(todo1.id)
        service.update_todo(todo2.id, "Updated second todo")
        service.delete_todo(todo3.id)

        # Verify data integrity - other todos remain intact
        remaining_todos = service.get_all_todos()
        assert len(remaining_todos) == 2

        # Check that todo1 is complete
        retrieved_todo1 = service.get_todo_by_id(todo1.id)
        assert retrieved_todo1 is not None
        assert retrieved_todo1.completed is True
        assert retrieved_todo1.description == "First todo"

        # Check that todo2 was updated
        retrieved_todo2 = service.get_todo_by_id(todo2.id)
        assert retrieved_todo2 is not None
        assert retrieved_todo2.description == "Updated second todo"

        # Verify todo3 is gone
        retrieved_todo3 = service.get_todo_by_id(todo3.id)
        assert retrieved_todo3 is None