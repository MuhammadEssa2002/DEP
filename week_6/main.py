import json

# Function to load tasks from file
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save tasks to file
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Function to add a task
def add_task(tasks):
    task_id = input("Enter Task ID: ")
    description = input("Enter Task Description: ")
    tasks.append({"id": task_id, "description": description, "status": "pending"})
    save_tasks(tasks)
    print("Task added successfully!")

# Function to view all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        for task in tasks:
            print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']}")

# Function to remove a task
def remove_task(tasks):
    task_id = input("Enter Task ID to remove: ")
    tasks[:] = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print("Task removed successfully!")

# Function to mark task as completed
def mark_completed(tasks):
    task_id = input("Enter Task ID to mark as completed: ")
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "completed"
            save_tasks(tasks)
            print("Task marked as completed!")
            return
    print("Task not found!")

# Function to edit a task
def edit_task(tasks):
    task_id = input("Enter Task ID to edit: ")
    for task in tasks:
        if task["id"] == task_id:
            new_description = input("Enter new task description: ")
            task["description"] = new_description
            save_tasks(tasks)
            print("Task updated successfully!")
            return
    print("Task not found!")

# Function to search tasks by keyword
def search_tasks(tasks):
    keyword = input("Enter keyword to search for: ")
    found_tasks = [task for task in tasks if keyword.lower() in task["description"].lower()]
    if found_tasks:
        for task in found_tasks:
            print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']}")
    else:
        print("No tasks found with the given keyword.")

# Function to filter tasks by status
def filter_tasks(tasks):
    status = input("Enter status to filter (pending/completed): ").lower()
    filtered_tasks = [task for task in tasks if task["status"] == status]
    if filtered_tasks:
        for task in filtered_tasks:
            print(f"ID: {task['id']} | Description: {task['description']} | Status: {task['status']}")
    else:
        print(f"No {status} tasks found.")

# Function to clear all tasks with confirmation
def clear_all_tasks(tasks):
    confirm = input("Are you sure you want to clear all tasks? (y/n): ").lower()
    if confirm == "y":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks cleared!")
    else:
        print("Operation cancelled.")

# Function to sort tasks by ID or status
def sort_tasks(tasks):
    choice = input("Sort by (1) ID or (2) Status: ")
    if choice == "1":
        tasks.sort(key=lambda x: x["id"])
    elif choice == "2":
        tasks.sort(key=lambda x: x["status"])
    save_tasks(tasks)
    print("Tasks sorted successfully!")
    view_tasks(tasks)

# Main menu function
def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Edit Task")
        print("6. Search Task")
        print("7. Filter Tasks")
        print("8. Clear All Tasks")
        print("9. Sort Tasks")
        print("0. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            mark_completed(tasks)
        elif choice == "5":
            edit_task(tasks)
        elif choice == "6":
            search_tasks(tasks)
        elif choice == "7":
            filter_tasks(tasks)
        elif choice == "8":
            clear_all_tasks(tasks)
        elif choice == "9":
            sort_tasks(tasks)
        elif choice == "0":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option! Please try again.")

if __name__ == "__main__":
    main()
