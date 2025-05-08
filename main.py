import json
from tools import summary, task_timer, data


def main():
    # Create tasks.json if it doesn't exist for some reason
    try:
        with open('tasks.json', 'x') as json_file:
            json.dump([], json_file)
    except FileExistsError:
        pass
    while True: # Main loop
        user_choice_menu = input("""
                       What would you like to do?
                       1. List all tasks
                       2. Create a new task
                       3. Delete a task
                       4. Start working on a task
                       5. Stop working on a task
                       6. Show summary
                       7. Exit
                       Enter choice: """).strip()
        if user_choice_menu == "1":
            data.list_tasks()
        elif user_choice_menu == '2': # User chose "Create a new task"
            data.create_task()
        elif user_choice_menu == '3': # User chose "Delete a task"
            data.delete_task()
        elif user_choice_menu == '4': # User chose "Start working on a task"
            task_timer.start()
        elif user_choice_menu == '5': # User chose "Stop working on a task"
            task_timer.stop()
        elif user_choice_menu == '6': # User chose "Show today's summary"
            while True:
                user_choice_summary = input("Do you want to see a task-by-task breakdown? (y/n): ").strip().lower()
                if user_choice_summary == 'y':
                    summary.individual()
                elif user_choice_summary == 'n':
                    summary.overall()
                else:
                    print("Please enter either 'y' or 'n'.")
        elif user_choice_menu == '7': # User chose "Exit"
            print('Goodbye')
            break
        else: # User input is invalid
            print("Invalid input. Please try again.")



if __name__ == "__main__":
    main()