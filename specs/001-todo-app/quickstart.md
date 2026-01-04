# Quickstart Guide: Todo In-Memory Python Console Application

## Getting Started

1. **Install Dependencies**:
   ```bash
   uv sync  # or pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python -m todo_app
   # or
   python todo_app/main.py
   ```

## Available Commands

### Add a new todo:
```bash
python -m todo_app add "Buy groceries"
```

### List all todos:
```bash
python -m todo_app list
```

### Update a todo:
```bash
python -m todo_app update 1 "Buy groceries and cook dinner"
```

### Delete a todo:
```bash
python -m todo_app delete 1
```

### Mark a todo as complete:
```bash
python -m todo_app complete 1
```

### Mark a todo as incomplete:
```bash
python -m todo_app incomplete 1
```

## Example Workflow

```bash
# Add todos
python -m todo_app add "Buy groceries"
python -m todo_app add "Walk the dog"

# View all todos
python -m todo_app list

# Mark first todo as complete
python -m todo_app complete 1

# Update the second todo
python -m todo_app update 2 "Walk the dog in the morning"

# View updated list
python -m todo_app list
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