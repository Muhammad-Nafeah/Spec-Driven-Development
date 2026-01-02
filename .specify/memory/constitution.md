<!--
Sync Impact Report:
- Version change: N/A → 1.0.0
- Modified principles: All principles added as new
- Added sections: All sections added as new
- Removed sections: None
- Templates requiring updates: ✅ Updated
- Follow-up TODOs: None
-->
# Todo In-Memory Python Console Application Constitution

## Core Principles

### I. Spec-Driven Development
All behavior must be defined in specifications before implementation. No code shall be written without corresponding specification documentation that clearly defines the expected behavior, inputs, outputs, and acceptance criteria.

### II. Agentic Development
Implementation must follow the Agentic Dev Stack workflow end-to-end. All development must be driven through Claude Code and Spec-Kit Plus tools, with no manual coding outside the defined workflow.

### III. Process Over Code
Evaluation focuses on specs, plans, tasks, and iterations rather than manual coding. The quality of specifications, planning artifacts, and task breakdowns takes precedence over the code implementation itself.

### IV. Clean Code Standards
Code must be readable, modular, and well-structured. All code must follow Python best practices, maintain clear separation of concerns, and include appropriate documentation and type hints where beneficial.

### V. Separation of Concerns
Core logic must be independent from CLI interaction. The business logic for todo operations must be implemented separately from the command-line interface layer to enable testability and reusability.

### VI. Deterministic Behavior

All Todo operations must exhibit deterministic behavior. Operations must produce consistent, predictable results given the same inputs and initial state, with no random or time-dependent behavior in core functionality.

## Technology and Implementation Constraints
Language: Python 3.13+ with UV package manager, Tooling: Claude Code, Spec-Kit Plus, Interface: Command-line / console only, Storage: In-memory only (no files, no database), No external services or network calls, No web, AI, or cloud components in this phase.

## Development Workflow and Quality Standards
All functionality must originate from Spec-Kit Plus specifications. No manual coding; all implementation generated via Claude Code. Python project structure must be clean and conventional. Core logic must be testable independently of the CLI. Clear naming, documentation, and modular design are required.

## Governance
This constitution supersedes all other development practices and must be followed for all work on this project. All pull requests and code reviews must verify compliance with these principles. Any deviation must be documented with clear justification and approval. The constitution may only be amended through the formal amendment process documented in the project's governance procedures.

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02
