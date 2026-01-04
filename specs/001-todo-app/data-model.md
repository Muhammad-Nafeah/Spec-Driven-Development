# Data Model for Todo In-Memory Python Console Application

## Todo Entity

**Fields**:
- `id` (int): Unique identifier for the todo item, auto-incrementing
- `description` (str): Text description of the task
- `completed` (bool): Boolean indicating completion status (default: False)

**Validation rules**:
- `id` must be a positive integer
- `description` must be non-empty string
- `completed` must be boolean value

**State transitions**:
- `incomplete` → `completed` when marked as complete
- `completed` → `incomplete` when marked as incomplete

## Todo List

**Fields**:
- `todos` (list): Collection of Todo objects
- `next_id` (int): Counter for generating next unique ID (starts at 1)

**Validation rules**:
- Must maintain unique IDs for all Todo objects
- No validation required for the list itself as it's a container