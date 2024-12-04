#README commands guide

##  Add a task:

### python task-cli.py add "Buy groceries"

This will add a new task and automatically generate the tasks.json file if it doesn’t exist.

## List all tasks:

#### python task-cli.py list

## Update a task (by ID):

If the taskhas ID 1, update its description with:

### python task-cli.py update 1 "Buy groceries and cook dinner"

## Mark a task as in progress:

### python task-cli.py mark-in-progress 1

## Delete a task:
```bash
 python task-cli.py delete 1
```

## List tasks by status:

```bash
python task-cli.py list done          # Shows completed tasks
python task-cli.py list in-progress   # Shows tasks in progress
python task-cli.py list todo          # Shows pending tasks
```


### **Rendered Output in GitHub:**
```bash
python task-cli.py list done          # Shows completed tasks
python task-cli.py list in-progress   # Shows tasks in progress
python task-cli.py list todo          # Shows pending tasks
