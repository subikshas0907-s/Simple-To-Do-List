def todo_list():
    tasks = []

    while True:
        print("\n📝 To-Do List Manager 📝")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ")

        if choice == '1':
            # Add a new task
            task = input("Enter the task: ")
            tasks.append({"task": task, "completed": False})
            print(f"✅ Added: '{task}'")

        elif choice == '2':
            # View all tasks
            if not tasks:
                print("No tasks yet! Add some tasks first.")
            else:
                print("\n--- Your Tasks ---")
                for idx, task in enumerate(tasks, start=1):
                    status = "✓" if task["completed"] else "✗"
                    print(f"{idx}. [{status}] {task['task']}")

        elif choice == '3':
            # Mark task as complete
            if not tasks:
                print("No tasks to mark as complete!")
            else:
                print("\nCurrent Tasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task['task']}")
                try:
                    task_num = int(input("Enter task number to mark as complete: ")) - 1
                    if 0 <= task_num < len(tasks):
                        tasks[task_num]["completed"] = True
                        print(f"✅ Marked '{tasks[task_num]['task']}' as complete!")
                    else:
                        print("❌ Invalid task number!")
                except ValueError:
                    print("❌ Please enter a valid number!")

        elif choice == '4':
            # Delete a task
            if not tasks:
                print("No tasks to delete!")
            else:
                print("\nCurrent Tasks:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task['task']}")
                try:
                    task_num = int(input("Enter task number to delete: ")) - 1
                    if 0 <= task_num < len(tasks):
                        deleted_task = tasks.pop(task_num)
                        print(f"❌ Deleted: '{deleted_task['task']}'")
                    else:
                        print("❌ Invalid task number!")
                except ValueError:
                    print("❌ Please enter a valid number!")

        elif choice == '5':
            # Exit the program
            print("Goodbye! 👋")
            break

        else:
            print("❌ Invalid choice! Please select 1-5.")

# Run the to-do list manager
todo_list()
