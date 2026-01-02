"""
CLI handler for the Todo application.
Maps command-line arguments to appropriate service methods.
"""
import argparse
import sys
from typing import List
from .todo_service import TodoService
from .todo import Todo


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        prog="todo",
        description="A command-line Todo application",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  todo add "Buy groceries"
  todo list
  todo update 1 "Buy groceries and cook dinner"
  todo delete 1
  todo complete 1
  todo incomplete 1
        """.strip()
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands", required=False)

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new todo")
    add_parser.add_argument("description", nargs="+", help="Description of the todo")

    # List command
    subparsers.add_parser("list", help="List all todos")

    # Update command
    update_parser = subparsers.add_parser("update", help="Update a todo description")
    update_parser.add_argument("id", type=int, help="ID of the todo to update")
    update_parser.add_argument("description", nargs="+", help="New description for the todo")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a todo")
    delete_parser.add_argument("id", type=int, help="ID of the todo to delete")

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a todo as complete")
    complete_parser.add_argument("id", type=int, help="ID of the todo to mark complete")

    # Incomplete command
    incomplete_parser = subparsers.add_parser("incomplete", help="Mark a todo as incomplete")
    incomplete_parser.add_argument("id", type=int, help="ID of the todo to mark incomplete")

    # Interactive mode
    subparsers.add_parser("interactive", help="Start interactive mode")

    return parser


def format_todo(todo: Todo) -> str:
    """Format a single todo for display."""
    status = "✓" if todo.completed else "○"
    return f"[{status}] {todo.id}: {todo.description}"


def handle_add(service: TodoService, args) -> None:
    """Handle the add command."""
    description = " ".join(args.description)
    try:
        todo = service.add_todo(description)
        print(f"Added todo: {format_todo(todo)}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def handle_list(service: TodoService, args) -> None:
    """Handle the list command."""
    todos = service.get_all_todos()
    if not todos:
        print("No todos found.")
    else:
        for todo in todos:
            print(format_todo(todo))


def handle_update(service: TodoService, args) -> None:
    """Handle the update command."""
    description = " ".join(args.description)
    try:
        success = service.update_todo(args.id, description)
        if success:
            updated_todo = service.get_todo_by_id(args.id)
            print(f"Updated todo: {format_todo(updated_todo)}")
        else:
            print(f"Error: Todo with ID {args.id} not found", file=sys.stderr)
            sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def handle_delete(service: TodoService, args) -> None:
    """Handle the delete command."""
    success = service.delete_todo(args.id)
    if success:
        print(f"Deleted todo with ID {args.id}")
    else:
        print(f"Error: Todo with ID {args.id} not found", file=sys.stderr)
        sys.exit(1)


def handle_complete(service: TodoService, args) -> None:
    """Handle the complete command."""
    success = service.mark_complete(args.id)
    if success:
        completed_todo = service.get_todo_by_id(args.id)
        print(f"Marked as complete: {format_todo(completed_todo)}")
    else:
        print(f"Error: Todo with ID {args.id} not found", file=sys.stderr)
        sys.exit(1)


def handle_incomplete(service: TodoService, args) -> None:
    """Handle the incomplete command."""
    success = service.mark_incomplete(args.id)
    if success:
        incomplete_todo = service.get_todo_by_id(args.id)
        print(f"Marked as incomplete: {format_todo(incomplete_todo)}")
    else:
        print(f"Error: Todo with ID {args.id} not found", file=sys.stderr)
        sys.exit(1)


def interactive_mode(service: TodoService) -> None:
    """Run the application in interactive mode."""
    print("Welcome to the Todo App!")
    print("Commands: add, list, update, delete, complete, incomplete, exit")

    while True:
        print("\nOptions:")
        print("1. Add Todo (a)")
        print("2. List Todos (l)")
        print("3. Update Todo (u)")
        print("4. Delete Todo (d)")
        print("5. Mark Complete (c)")
        print("6. Mark Incomplete (i)")
        print("7. Exit (e)")

        choice = input("\nEnter your choice (1-7) or command letter: ").strip().lower()

        if choice in ['1', 'a', 'add']:
            description = input("Enter todo description: ").strip()
            if description:
                try:
                    todo = service.add_todo(description)
                    print(f"Added todo: {format_todo(todo)}")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Description cannot be empty!")

        elif choice in ['2', 'l', 'list']:
            todos = service.get_all_todos()
            if not todos:
                print("No todos found.")
            else:
                print("\nYour Todos:")
                for todo in todos:
                    print(format_todo(todo))

        elif choice in ['3', 'u', 'update']:
            try:
                todo_id = int(input("Enter todo ID to update: "))
                description = input("Enter new description: ").strip()
                if description:
                    success = service.update_todo(todo_id, description)
                    if success:
                        updated_todo = service.get_todo_by_id(todo_id)
                        print(f"Updated todo: {format_todo(updated_todo)}")
                    else:
                        print(f"Error: Todo with ID {todo_id} not found")
                else:
                    print("Description cannot be empty!")
            except ValueError:
                print("Please enter a valid ID number.")

        elif choice in ['4', 'd', 'delete']:
            try:
                todo_id = int(input("Enter todo ID to delete: "))
                success = service.delete_todo(todo_id)
                if success:
                    print(f"Deleted todo with ID {todo_id}")
                else:
                    print(f"Error: Todo with ID {todo_id} not found")
            except ValueError:
                print("Please enter a valid ID number.")

        elif choice in ['5', 'c', 'complete']:
            try:
                todo_id = int(input("Enter todo ID to mark complete: "))
                success = service.mark_complete(todo_id)
                if success:
                    completed_todo = service.get_todo_by_id(todo_id)
                    print(f"Marked as complete: {format_todo(completed_todo)}")
                else:
                    print(f"Error: Todo with ID {todo_id} not found")
            except ValueError:
                print("Please enter a valid ID number.")

        elif choice in ['6', 'i', 'incomplete']:
            try:
                todo_id = int(input("Enter todo ID to mark incomplete: "))
                success = service.mark_incomplete(todo_id)
                if success:
                    incomplete_todo = service.get_todo_by_id(todo_id)
                    print(f"Marked as incomplete: {format_todo(incomplete_todo)}")
                else:
                    print(f"Error: Todo with ID {todo_id} not found")
            except ValueError:
                print("Please enter a valid ID number.")

        elif choice in ['7', 'e', 'exit']:
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


def handle_interactive(service: TodoService, args) -> None:
    """Handle the interactive command."""
    interactive_mode(service)


def main() -> None:
    """Main entry point for the CLI application."""
    parser = create_parser()
    args = parser.parse_args()

    # Create a single instance of the service to maintain state in memory
    service = TodoService()

    # Map commands to handler functions
    command_handlers = {
        "add": handle_add,
        "list": handle_list,
        "update": handle_update,
        "delete": handle_delete,
        "complete": handle_complete,
        "incomplete": handle_incomplete,
        "interactive": handle_interactive
    }

    # Execute the appropriate handler
    handler = command_handlers.get(args.command)
    if handler:
        handler(service, args)
    else:
        # If no command is provided, start interactive mode
        interactive_mode(service)