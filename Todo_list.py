todo = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        todo.append(task)
        print("Task added")

    elif choice == "2":
        print("Your To-Do List:")
        for task in todo:
            print("-", task)

    elif choice == "3":
        print("Exiting program")
        break

    else:
        print("Invalid choice")
