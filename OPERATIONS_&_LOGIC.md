# Task Organizer CLI

A simple command-line application to manage tasks efficiently. This tool allows you to add, update, delete, and list tasks while keeping track of their statuses (To-Do, In Progress, Done). The tasks are stored in a JSON file for persistence.

## Features
#### Add new tasks with descriptions.
#### Update task descriptions.
#### Delete tasks.
#### Mark tasks as "In Progress" or "Done."
#### List tasks by their status (all, To-Do, In Progress, Done).

## CODE Structure
#### Here is the organizational structure of the commands, explaining their usage and logic:
```plaintext
Begin
↳ Add Tasks
   ↳ Substep: Add a new task to the organizer
      ↳ Command: python task-cli.py add "Task Description"
         ↳ Example: python task-cli.py add "Buy groceries"
↳ Update Tasks
   ↳ Substep: Modify the description of an existing task
      ↳ Command: python task-cli.py update <Task ID> "New Description"
         ↳ Example: python task-cli.py update 1 "Buy groceries and cook dinner"
↳ Delete Tasks
   ↳ Substep: Remove a task from the organizer
      ↳ Command: python task-cli.py delete <Task ID>
         ↳ Example: python task-cli.py delete 1
↳ Manage Task Status
   ↳ Substep 1: Mark a task as "In Progress"
      ↳ Command: python task-cli.py mark-in-progress <Task ID>
         ↳ Example: python task-cli.py mark-in-progress 1
   ↳ Substep 2: Mark a task as "Done"
      ↳ Command: python task-cli.py mark-done <Task ID>
         ↳ Example: python task-cli.py mark-done 1
↳ List Tasks
   ↳ Substep 1: Display all tasks
      ↳ Command: python task-cli.py list
   ↳ Substep 2: Filter tasks by status
      ↳ Done
         ↳ Command: python task-cli.py list done
      ↳ In Progress
         ↳ Command: python task-cli.py list in-progress
      ↳ To Do
         ↳ Command: python task-cli.py list todo
End
```
## Each task includes the following properties:

### id: A unique identifier for the task.
### description: A short description of the task.
### status: The status of the task (todo, in-progress, done).
### createdAt: The date and time when the task was created.
### updatedAt: The date and time when the task was last updated.
