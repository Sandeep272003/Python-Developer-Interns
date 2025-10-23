def load_tasks(filename="tasks.txt"):
    try:
        with open(filename, "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks, filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print(f'Task "{task}" added.')
    else:
        print("Empty task not added.")

def remove_task(tasks):
    try:
        index = int(input("Enter the task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f'Task "{removed}" removed.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks(tasks):
    if tasks:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    else:
        print("Your to-do list is empty.")

def todo_app():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Manager")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    todo_app()
