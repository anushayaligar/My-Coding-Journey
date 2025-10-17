# Helper function to save tasks
def save_tasks():
    with open("todo.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Step 1: Load tasks safely
try:
    with open("todo.txt", "r") as f:
        tasks = f.read().splitlines()
except FileNotFoundError:
    tasks = []

# Step 2: Main loop
while True:
    print("\n===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print("👉 You chose to ADD a new task.")
        new_task = input("Enter a new task: ")
        tasks.append(new_task)
        save_tasks()
        print("✅ Task added successfully!")

    elif choice == "2":
        print("👉 You chose to VIEW all tasks.")
        print("\n===== Your To-Do List =====")
        if not tasks:
            print("📂 No tasks yet!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        print("👉 You chose to DELETE a task.")
        if not tasks:
            print("📂 No tasks to delete!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                num = int(input("Enter task number to delete: "))
                removed = tasks.pop(num - 1)
                save_tasks()
                print(f"🗑️ Deleted task: {removed}")
            except (ValueError, IndexError):
                print("❌ Invalid input! Please enter a valid task number.")

    elif choice == "4":
        print("👉 You chose to EXIT the program.")
        print("👋 Exiting... Goodbye!")
        break  # loop stops here

    else:
        print("❌ Invalid choice, please select 1, 2, 3, or 4.")
