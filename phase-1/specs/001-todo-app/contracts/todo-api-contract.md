# Todo API Contract

## CLI Commands Interface

### Add Todo
- **Command**: `todo add <description>`
- **Input**: Todo description as string argument
- **Output**: Success message with assigned ID
- **Error cases**: Empty description, system errors

### List Todos
- **Command**: `todo list`
- **Input**: None
- **Output**: Formatted list of all todos with ID, description, and completion status
- **Error cases**: No todos exist

### Update Todo
- **Command**: `todo update <id> <new_description>`
- **Input**: Todo ID (int) and new description (string)
- **Output**: Success message
- **Error cases**: Invalid ID, empty description, todo doesn't exist

### Delete Todo
- **Command**: `todo delete <id>`
- **Input**: Todo ID (int)
- **Output**: Success message
- **Error cases**: Invalid ID, todo doesn't exist

### Mark Todo Complete
- **Command**: `todo complete <id>`
- **Input**: Todo ID (int)
- **Output**: Success message
- **Error cases**: Invalid ID, todo doesn't exist

### Mark Todo Incomplete
- **Command**: `todo incomplete <id>`
- **Input**: Todo ID (int)
- **Output**: Success message
- **Error cases**: Invalid ID, todo doesn't exist