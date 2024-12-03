import sys
import json
import os
from datetime import datetime

# Path to the JSON file where the tasks are stored
TASKS_FILE = "tasks.json"

# Function to load tasks from JSON file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

# Function to save tasks to JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to generate a unique ID for a new task
def generate_id(tasks):
    return max((task["id"] for task in tasks), default=0) + 1

# Function to add a new task
def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": generate_id(tasks),
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task['id']})")

# Function to update an existing task
def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return
    print(f"Task {task_id} not found.")

# Function to delete a task
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted successfully.")

# Function to change the status of a task
def change_status(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}.")
            return
    print(f"Task {task_id} not found.")

# Function to list tasks
def list_tasks(filter_status=None):
    tasks = load_tasks()
    if filter_status:
        tasks = [task for task in tasks if task["status"] == filter_status]
    if not tasks:
        print("No tasks found.")
    for task in tasks:
        print(f"[{task['id']}] {task['description']} - {task['status']} (Created: {task['createdAt']})")

# Main function to handle command line commands
def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [options]")
        return

    command = sys.argv[1]
    
    try:
        if command == "add":
            description = " ".join(sys.argv[2:])
            add_task(description)
        elif command == "update":
            task_id = int(sys.argv[2])
            new_description = " ".join(sys.argv[3:])
            update_task(task_id, new_description)
        elif command == "delete":
            task_id = int(sys.argv[2])
            delete_task(task_id)
        elif command == "mark-in-progress":
            task_id = int(sys.argv[2])
            change_status(task_id, "in-progress")
        elif command == "mark-done":
            task_id = int(sys.argv[2])
            change_status(task_id, "done")
        elif command == "list":
            if len(sys.argv) > 2:
                filter_status = sys.argv[2]
                if filter_status not in ["todo", "in-progress", "done"]:
                    print("Invalid status. Use 'todo', 'in-progress', or 'done'.")
                    return
                list_tasks(filter_status)
            else:
                list_tasks()
        else:
            print("Unknown command. Available commands: add, update, delete, mark-in-progress, mark-done, list")
    except IndexError:
        print("Invalid command or missing arguments.")
    except ValueError:
        print("Invalid task ID. Please use a numeric value.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
