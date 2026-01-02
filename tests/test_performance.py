"""
Performance tests to ensure operations complete within 1 second.
"""
import time
from todo_app.todo_service import TodoService


class TestPerformance:
    """Test performance requirements."""

    def test_add_operation_performance(self):
        """Test that adding a todo completes within 1 second."""
        service = TodoService()

        start_time = time.time()
        service.add_todo("Performance test todo")
        end_time = time.time()

        duration = end_time - start_time
        assert duration < 1.0, f"Add operation took {duration:.4f} seconds, which is more than 1 second"

    def test_list_operation_performance(self):
        """Test that listing todos completes within 1 second."""
        service = TodoService()

        # Add some todos to make the test meaningful
        for i in range(10):
            service.add_todo(f"Todo {i}")

        start_time = time.time()
        todos = service.get_all_todos()
        end_time = time.time()

        duration = end_time - start_time
        assert duration < 1.0, f"List operation took {duration:.4f} seconds, which is more than 1 second"

    def test_update_operation_performance(self):
        """Test that updating a todo completes within 1 second."""
        service = TodoService()
        todo = service.add_todo("Original description")

        start_time = time.time()
        service.update_todo(todo.id, "Updated description")
        end_time = time.time()

        duration = end_time - start_time
        assert duration < 1.0, f"Update operation took {duration:.4f} seconds, which is more than 1 second"

    def test_delete_operation_performance(self):
        """Test that deleting a todo completes within 1 second."""
        service = TodoService()
        todo = service.add_todo("Todo to delete")

        start_time = time.time()
        service.delete_todo(todo.id)
        end_time = time.time()

        duration = end_time - start_time
        assert duration < 1.0, f"Delete operation took {duration:.4f} seconds, which is more than 1 second"

    def test_mark_complete_operation_performance(self):
        """Test that marking a todo complete completes within 1 second."""
        service = TodoService()
        todo = service.add_todo("Todo to mark complete")

        start_time = time.time()
        service.mark_complete(todo.id)
        end_time = time.time()

        duration = end_time - start_time
        assert duration < 1.0, f"Mark complete operation took {duration:.4f} seconds, which is more than 1 second"

    def test_large_dataset_performance(self):
        """Test performance with a larger dataset (100 todos)."""
        service = TodoService()

        # Add 100 todos
        start_time = time.time()
        for i in range(100):
            service.add_todo(f"Performance test todo {i}")
        add_duration = time.time() - start_time

        # Test listing 100 todos
        start_time = time.time()
        todos = service.get_all_todos()
        list_duration = time.time() - start_time

        # Test updating one of them
        start_time = time.time()
        service.update_todo(50, "Updated performance todo")
        update_duration = time.time() - start_time

        # All operations should be under 1 second
        assert add_duration < 1.0, f"Adding 100 todos took {add_duration:.4f} seconds, which is more than 1 second"
        assert list_duration < 1.0, f"Listing 100 todos took {list_duration:.4f} seconds, which is more than 1 second"
        assert update_duration < 1.0, f"Updating with 100 todos took {update_duration:.4f} seconds, which is more than 1 second"