tasks = []

def add_task():
    task = input("Enter task name: ")
    tasks.append(task)
    print("Task added successfully!")

def show_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def menu():
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")

while True:
    menu()
    choice = input("Choose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
