import click # to create a cli
import json  # to save and load tasks from a file
import os    # to check if the file exists

TODO_FILE = "todo.json"  # Define the filename where tasks are stored


# Function to load tasks from the JSON file
def load_tasks():
    if not os.path.exists(TODO_FILE):     # Check if file exists
        return []  # If not, return an empty list
    with open(TODO_FILE, "r") as file:   # Open the file in read mode
        return json.load(file)    # Load and return the JSON data as a Python list
    
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


@click.group()
def cli():
    """Simple Todo List Manager"""
    pass 

@click.command()  
@click.argument("task")  
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(f"Task added successfully: {task}")


@click.command()    
def list():
    """List all the tasks"""
    tasks = load_tasks() 
    if not tasks:
        click.echo("No tasks found!.")
        return
    for index, task in enumerate(tasks, 1):
        status  = "✅" if task['done'] else '❌'
        click.echo(f"{index}. {task['task']} {{status}}")


@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    """Mark a task as complete"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number -1]["done"] = True
        save_tasks(tasks)
        click.echo(f"Task {task_number} markes as complete.")
    else:
        click.echo("Invalid task number.")

@click.command()        
@click.argument("task_number",type=int)
def remove(task_number):
    """Remove a task from the list"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number -1)
        save_tasks(tasks)
        click.echo(f"Removed task: {removed_task['task']}")
    else:
        click.echo(f"Invalid task number.")




# Add commands to the main CLI group
cli.add_command(add) 
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)

if __name__ == "__main__":
    cli()


         