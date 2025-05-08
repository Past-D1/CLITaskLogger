from .data import save_tasks, load_tasks
from datetime import datetime

def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds

def start():
    tasks = load_tasks() # Loads the tasks to then list them and start a timer for the selected task

    if not tasks: # Checks if tasks.json is empty, if it is, it ends the function as there's no task to start a timer for
        print("Task not found!")
        return
    print("\n\nPlease select a task to start working on")
    for index, task in enumerate(tasks, start=1): # Prints out an enumerated list of tasks saved in tasks.json
        print(f"{index}. {task['name']}")

    while True: # Loops over the prompt asking the user which task they'd like to start the timer for in order to handle invalid user choices
        user_choice = input("Enter choice: ").strip()
        try:
            user_choice = int(user_choice)
            if 1 <= int(user_choice) <= len(tasks):
                break # No ValueError detected and user input is within range, exits the loop
            else:
                print(f"Please enter a number from 1 to {len(tasks)}")
        except ValueError:
            print("Invalid choice!")

    # Next step will probably be creating a "time_started" variable wherein we'll store the current (at the time the function is called) (using datetime)
    # I will then probably have to somehow associate that timer with "user_choice"

    selected_task = tasks[user_choice - 1] # Fetches the right task in tasks.json (through 'tasks')
    if selected_task["start_time"] is not None:
        print(f"Task '{selected_task['name']}' is already running!")
        return
    selected_task["start_time"] = datetime.now().astimezone().isoformat() # Changes the value of the key 'start_time' to be the current time and date (in isoformat)

    save_tasks(tasks)

    print(f"Timer started for '{selected_task['name']}' at {selected_task['start_time']}.")

def stop():
    tasks = load_tasks()

    if not tasks: # Checks if tasks.json is empty, if it is, it ends the function as there's no task to start a timer for
        print("No tasks found! Please create a new task and start a new timer to try again!")
        return

    for index, task in enumerate(tasks, start=1): # Prints out an enumerated list of tasks saved in tasks.json
        print(f"{index}. {task['name']}")

    while True:  # Loops over the prompt asking the user which task they'd like to start the timer for in order to handle invalid user choices
        user_choice = input("Enter choice: ").strip()
        try:
            user_choice = int(user_choice)
            if 1 <= int(user_choice) <= len(tasks):
                break  # No ValueError detected and user input is within range, exits the loop
            else:
                print(f"Please enter a number from 1 to {len(tasks)}")
        except ValueError:
            print("Invalid choice!")
            continue

    selected_task = tasks[user_choice - 1]
    if selected_task["start_time"] is None:
        print(f"No start time found for '{selected_task['name']}'!")
        return

    now = datetime.now().astimezone()

    start_time = datetime.fromisoformat(selected_task["start_time"])

    duration =  now - start_time

    selected_task['total_time'] += duration.total_seconds()

    selected_task['history'].append({
        "start":selected_task["start_time"],
        "end": now.isoformat()
    })

    selected_task['start_time'] = None

    save_tasks(tasks)

    hours, minutes, seconds = format_duration(duration)
    print(f"Added {hours} hours, {minutes} minutes, {seconds} seconds to '{selected_task['name']}'.")