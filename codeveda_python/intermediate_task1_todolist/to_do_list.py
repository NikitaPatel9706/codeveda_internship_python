
import json
import os

FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

# Add a new task
def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    print(f"✅ Task added: {task}")

# List all tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📂 No tasks found.")
        return
    for i, t in enumerate(tasks, start=1):
        status = "✔️ Done" if t["done"] else "❌ Not Done"
        print(f"{i}. {t['task']} - {status}")

# Delete a task
def delete_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Task deleted: {removed['task']}")
    else:
        print("⚠️ Error: Task number does not exist.")

# Mark a task as done
def mark_done(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"✔️ Task marked as done: {tasks[index - 1]['task']}")
    else:
        print("⚠️ Error: Task number does not exist.")

# Command-line menu
def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            try:
                index = int(input("Enter task number to delete: "))
                delete_task(index)
            except ValueError:
                print("⚠️ Invalid input. Please enter a number.")
        elif choice == "4":
            try:
                index = int(input("Enter task number to mark as done: "))
                mark_done(index)
            except ValueError:
                print("⚠️ Invalid input. Please enter a number.")
        elif choice == "5":
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()