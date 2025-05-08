from .data import load_tasks
from .task_timer import format_duration
from datetime import datetime, timedelta

def individual():
    tasks = load_tasks()
    today = datetime.now().astimezone().date()

    print("\nTime spent on each task today:\n")
    for task in tasks:
        task_duration = timedelta()

        for session in task["history"]:
            start = datetime.fromisoformat(session["start"])
            end = datetime.fromisoformat(session["end"])

            # Only count sessions from today
            if start.date() == today:
                task_duration += (end - start)

            if task_duration > timedelta(0):
                hours, minutes, seconds = format_duration(task_duration)
                print(f"{task['name']}: {hours}h {minutes}m {seconds}s")

def overall():
    tasks = load_tasks()
    total_duration = timedelta()
    today = datetime.now().astimezone().date()
    for task in tasks:
        for session in task["history"]:
            start = datetime.fromisoformat(session["start"])
            end = datetime.fromisoformat(session["end"])

            if start.date() == today:
                total_duration += (end - start)

    hours, minutes, seconds = format_duration(total_duration)
    print(f"Time spent today: {hours}h {minutes}m {seconds}s")