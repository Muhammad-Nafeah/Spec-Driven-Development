# Tasks: Todo In-Memory Python Console Application

## Phase 1: Project Setup

**Goal**: Initialize Python project with proper structure and dependencies for the todo application.

**Independent Test**: Project structure is created and can run a basic Python script from the command line.

### Setup Tasks

- [X] T001 Create project directory structure: todo_app/, tests/, pyproject.toml
- [X] T002 Initialize UV project with Python 3.13+ and create pyproject.toml
- [X] T003 Create initial directory structure: todo_app/__init__.py, todo_app/__main__.py

## Phase 2: Foundational Components

**Goal**: Create the core data model and service layer that will be used by all user stories.

**Independent Test**: Core Todo model and TodoService can be instantiated and basic operations can be performed in isolation.

### Foundational Tasks

- [X] T004 [P] Create Todo data model in todo_app/todo.py with id, description, completed fields
- [X] T005 [P] Implement Todo validation rules in todo_app/todo.py
- [X] T006 [P] Create TodoService in todo_app/todo_service.py with in-memory storage
- [X] T007 [P] Implement add_todo method in TodoService with auto-incrementing IDs
- [X] T008 [P] Implement get_all_todos method in TodoService
- [X] T009 [P] Implement update_todo method in TodoService
- [X] T010 [P] Implement delete_todo method in TodoService
- [X] T011 [P] Implement mark_complete/mark_incomplete methods in TodoService
- [X] T012 [P] Add error handling for edge cases in TodoService
- [X] T013 Create CLI argument parser in todo_app/cli_handler.py
- [X] T014 Create basic CLI command mapping in cli_handler.py

## Phase 3: User Story 1 - Add and View Todos (Priority: P1)

**Goal**: Implement the core functionality to add new todo items and view all current todos.

**Independent Test**: Can add several todo items and view the complete list, delivering the fundamental value of task tracking.

**Acceptance Scenarios**:
1. Given I have no todos, When I add a new todo "Buy groceries", Then the todo should appear in my todo list
2. Given I have multiple todos in the list, When I view all todos, Then all todos should be displayed with their details

### Implementation Tasks

- [X] T015 [US1] Implement CLI command for adding todos: `todo add <description>`
- [X] T016 [US1] Add validation for empty descriptions in add command
- [X] T017 [US1] Implement CLI command for listing todos: `todo list`
- [X] T018 [US1] Format list output with ID, description, and completion status
- [X] T019 [US1] Test adding and viewing todos with multiple entries
- [X] T020 [US1] Handle edge case when no todos exist for list command

## Phase 4: User Story 2 - Update and Delete Todos (Priority: P2)

**Goal**: Implement functionality to update existing todo items and remove completed or unnecessary todos.

**Independent Test**: Can update a todo's description and delete specific todos, delivering task management capabilities.

**Acceptance Scenarios**:
1. Given I have a todo "Buy groceries", When I update it to "Buy groceries and cook dinner", Then the todo should reflect the updated description
2. Given I have multiple todos including "Buy groceries", When I delete "Buy groceries", Then that todo should no longer appear in my list

### Implementation Tasks

- [X] T021 [US2] Implement CLI command for updating todos: `todo update <id> <new_description>`
- [X] T022 [US2] Add validation for invalid IDs in update command
- [X] T023 [US2] Add validation for empty descriptions in update command
- [X] T024 [US2] Implement CLI command for deleting todos: `todo delete <id>`
- [X] T025 [US2] Add validation for invalid IDs in delete command
- [X] T026 [US2] Test update functionality with valid and invalid inputs
- [X] T027 [US2] Test delete functionality with valid and invalid inputs

## Phase 5: User Story 3 - Mark Todos as Complete (Priority: P3)

**Goal**: Implement functionality to mark completed todos as done so users can track progress and focus on remaining tasks.

**Independent Test**: Can mark todos as complete and view the status, delivering progress tracking capabilities.

**Acceptance Scenarios**:
1. Given I have an incomplete todo "Buy groceries", When I mark it as complete, Then the todo should show as completed in the list
2. Given I have a mix of complete and incomplete todos, When I view all todos, Then each should show its current completion status

### Implementation Tasks

- [X] T028 [US3] Implement CLI command for marking todos as complete: `todo complete <id>`
- [X] T029 [US3] Add validation for invalid IDs in complete command
- [X] T030 [US3] Implement CLI command for marking todos as incomplete: `todo incomplete <id>`
- [X] T031 [US3] Add validation for invalid IDs in incomplete command
- [X] T032 [US3] Verify completion status is displayed in list command output
- [X] T033 [US3] Test marking todos as complete and incomplete with valid and invalid inputs

## Phase 6: Testing and Validation

**Goal**: Create comprehensive tests for all functionality and validate against requirements.

**Independent Test**: All tests pass and all functional requirements are satisfied.

### Testing Tasks

- [X] T034 Create unit tests for Todo model in tests/test_todo.py
- [X] T035 Create unit tests for TodoService in tests/test_todo_service.py
- [X] T036 Create integration tests for CLI commands in tests/test_cli_handler.py
- [X] T037 Test all edge cases identified in specification
- [X] T038 Validate all functional requirements (FR-001 through FR-009) are met
- [X] T039 Test performance to ensure operations complete within 1 second

## Phase 7: Polish & Cross-Cutting Concerns

**Goal**: Complete the application with proper error handling, documentation, and final validation.

**Independent Test**: Application runs correctly from the command line without crashes during standard operations and all features work as specified.

### Polish Tasks

- [X] T040 Add comprehensive error handling and user-friendly messages for all commands
- [X] T041 Implement proper command-line help and usage instructions
- [X] T042 Verify in-memory storage behavior with no persistent storage
- [X] T043 Add type hints to all functions and classes for better code quality
- [X] T044 Document all modules and functions with docstrings
- [X] T045 Final validation that core logic is separated from CLI interface
- [X] T046 End-to-end testing of all 5 basic todo features
- [X] T047 Update README with usage instructions based on quickstart guide

## Dependencies

- T004-T014 must complete before T015-T027 (foundational components needed for user stories)
- T015-T019 (Add/View) can be tested independently as MVP
- T021-T027 (Update/Delete) depends on foundational components
- T028-T033 (Mark Complete) depends on foundational components
- T034-T039 (Testing) can run after each user story completion
- T040-T047 (Polish) runs after all user stories are complete

## Parallel Execution Examples

- **User Story 1 Parallel Tasks**: T015/T017 (Add and List commands can be developed in parallel)
- **User Story 2 Parallel Tasks**: T021/T024 (Update and Delete commands can be developed in parallel)
- **User Story 3 Parallel Tasks**: T028/T030 (Complete and Incomplete commands can be developed in parallel)
- **Testing Parallel Tasks**: T034/T035/T036 (Unit tests for different components can be developed in parallel)

## Implementation Strategy

1. **MVP First**: Complete User Story 1 (Add/View) to have a basic working application
2. **Incremental Delivery**: Add Update/Delete functionality, then Complete/Incomplete
3. **Parallel Development**: Where possible, develop commands in parallel as they use the same service layer
4. **Continuous Testing**: Validate each user story as it's completed before moving to the next