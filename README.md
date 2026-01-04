# Todo In-Memory Python Console Application

A command-line Todo application that stores tasks entirely in memory, built with Python.

## Features

- Add new todos with descriptions
- List all todos with their completion status
- Update existing todo descriptions
- Delete todos
- Mark todos as complete/incomplete
- Interactive mode with menu-driven interface
- All data stored in-memory only (no persistence)

## Requirements

- Python 3.13 or higher

## Installation

1. Clone the repository
2. Install dependencies using your preferred method:
   - Using pip: `pip install -e .`
   - The application is also set up to work with UV if available

## Usage

### Command-Line Mode

Add a new todo:
```bash
python -m todo_app add "Buy groceries"
```

List all todos:
```bash
python -m todo_app list
```

Update a todo:
```bash
python -m todo_app update 1 "Buy groceries and cook dinner"
```

Delete a todo:
```bash
python -m todo_app delete 1
```

Mark a todo as complete:
```bash
python -m todo_app complete 1
```

Mark a todo as incomplete:
```bash
python -m todo_app incomplete 1
```

### Interactive Mode (Recommended)

Start the interactive mode:
```bash
python -m todo_app
# or
python -m todo_app interactive
```

This will launch a menu-driven interface where you can:
1. Add Todo (a)
2. List Todos (l)
3. Update Todo (u)
4. Delete Todo (d)
5. Mark Complete (c)
6. Mark Incomplete (i)
7. Exit (e)

### Example Workflow

```bash
# Command-line usage
python -m todo_app add "Buy groceries"
python -m todo_app add "Walk the dog"
python -m todo_app list
python -m todo_app complete 1
python -m todo_app list

# Or use the interactive mode for menu-driven experience
python -m todo_app
```

## Project Structure

```
todo_app/
├── __main__.py          # Entry point for CLI
├── todo_service.py      # Core business logic
├── todo.py              # Todo data model
├── cli_handler.py       # CLI command parsing
└── __init__.py
```

## Architecture

The application follows a clean architecture with clear separation of concerns:

- **Data Model** (`todo.py`): Defines the Todo entity
- **Service Layer** (`todo_service.py`): Contains all business logic
- **CLI Handler** (`cli_handler.py`): Handles command-line interface
- **Entry Point** (`__main__.py`): Application entry point

## Testing

To run the tests:
```bash
pytest tests/
```

The application includes comprehensive unit tests, integration tests, and tests for edge cases and functional requirements.

## Design Principles

- **In-Memory Storage**: All data is stored in memory only and will be lost when the application exits
- **Separation of Concerns**: Business logic is separated from CLI interface
- **Error Handling**: Graceful handling of invalid inputs with helpful error messages
- **Deterministic Behavior**: Operations produce consistent, predictable results
- **User Experience**: Interactive mode provides menu-driven interface for ease of use
