import json

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return [] # Return empty list if file doesn't exist or is corrupted

def save_tasks(data):
    with open("tasks.json", "w") as f:
        json.dump(data, f, indent=4)

def create_task():
    task_name = input("If you wish to go back, enter '0'\nEnter task name: ").strip()
    if not task_name:
        print("Task name cannot be empty.")
        return
    if task_name == "0":
        print("Task creation cancelled successfully.")
        return
    # Create a task dictionary with initial values
    new_task = {
        "name": task_name,
        "start_time": None,
        "total_time": 0,
        "history": []
    }
    # Load current tasks, add the new task, and save back to file
    tasks = load_tasks()
    tasks.append(new_task)
    save_tasks(tasks)

    print(f"Task {task_name} created successfully!")

def delete_task():
    tasks = load_tasks()
    while True:
        if not tasks:
            print("No tasks to delete.")
            return

        print("Please select the task you would like to delete:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['name']}")

        try:
            user_choice = int(input(f"Enter a number between 1 and {len(tasks)}, or 0 to cancel: ").strip())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_choice == 0:
            print("Task deletion cancelled.")
            return
        elif 1 <= user_choice <= len(tasks):
            while True:
                confirm = input(f"Are you sure you want to delete '{tasks[user_choice - 1]['name']}'? (y/n): ").lower()
                if confirm == "y":
                    removed = tasks.pop(user_choice - 1)
                    save_tasks(tasks)
                    print(f"Deleted task: {removed['name']}")
                    return
                elif confirm == "n":
                    nav = input("Do you want to:\n1. Go back to the main menu\n2. Select another task\nEnter 1 or 2: ").strip()
                    if nav == "1":
                        print("Task deletion cancelled.")
                        return
                    elif nav == "2":
                        break
                    else:
                        print("Please enter a valid option (1 or 2).")
                else:
                    print("Please enter either 'y' or 'n'.")
        else:
            print(f"Invalid number. Please select between 1 and {len(tasks)}.")

def list_tasks():
    tasks = load_tasks()
    if len(tasks) == 0:
        print("You have no tasks at the moment.")
        return
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['name']}")
