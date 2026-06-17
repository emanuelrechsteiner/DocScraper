---
inclusion: always
---

# Development Workflow & Best Practices

## Pre-Phase Planning Protocol

**Always formulate and discuss plans before implementation:**

1. **Understand the request** - what specific outcome is desired?
2. **Identify affected systems** - authentication, dashboard rendering, Firebase, UI components
3. **Propose approach** - reference existing patterns where possible
4. **Confirm scope** - what's in scope vs. future enhancements
5. **Get explicit approval** before proceeding with implementation

**Example Planning Response:**
```
I understand you want to [specific goal]. Here's my approach:

1. [Step 1 with file references]
2. [Step 2 with existing pattern references] 
3. [Step 3 with testing approach]

This will affect @file1, @file2, and follow the pattern from @existing-example.
Should I proceed with this approach?
```

## Task Decomposition & Documentation

### Focused Tasks
- Avoid multi-tasking in single actions
- Target specific changes rather than broad refactors
- For complex requests, propose step-by-step breakdown first

### Build Notes Structure
For complex features, create structured documentation:

```md
# Build Notes: [Task Name]

## Task Objective
[Concise description of the goal]

## Current State Assessment
[Current implementation or status]

## Future State Goal
[Target implementation or outcome]

## Implementation Plan
1. Step One
   - [ ] Task 1.1
   - [ ] Task 1.2
2. Step Two
   - [ ] Task 2.1 

## Progress Updates
- [Date]: [Update description]
```

## Context Preservation

### File Reference System
- Use @ symbols to maintain context:
  - @Files - Reference specific files (e.g., @components/Header.tsx)
  - @Folders - Reference entire directories for broader context
  - @Code - Reference specific code snippets or symbols

### Context Recovery Protocol
- Before every action, review recent chat history and current editor context
- Use @ references to confirm understanding of relevant files/symbols
- If context seems lost, prompt for clarification before proceeding

## Code Quality Standards

### File Organization
- Maximum file size: 150 lines (refactor if larger)
- Use semantic naming with auxiliary verbs (isLoading, hasError)
- One component per file, named same as component

### Minimal Changes Philosophy
- "Lines of code = Technical debt"
- Make changes with minimal impact on existing code
- Focus edits only on required areas, avoiding unrelated "improvements"

### Safety Checks
Before suggesting significant changes:
- Verify compatibility with existing patterns
- Consider potential side effects
- Suggest tests or verification methods

## Error Prevention & Management

### Task Decomposition Process
For large requests:
- Break down into step-by-step plan
- Use @ references for relevant files/functions
- Present plan for approval before suggesting code changes

### Scope Discipline
- Don't modify unrelated code/files unless essential
- Provide rationale when broader changes are needed
- Ask specific questions for ambiguous requests

## Implementation Standards

### Code Quality Focus
- Write concise, maintainable, and strongly typed TypeScript
- Use descriptive, semantic variable names
- Follow existing project patterns and conventions
- Implement proper error handling with user-friendly messages

### Testing Integration
- Add tests with changes, especially for business logic
- Use existing testing patterns from the project
- Mock Firebase services for isolated testing
- Ensure tests cover both success and error scenarios