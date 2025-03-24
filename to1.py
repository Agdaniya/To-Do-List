while True:
    def add_task():
        task = input("enter the task")
        with open("tasks.txt", "a") as file:
            file.write(task + "\n")
        print(f"Task '{task}' added successfully!")
    def view_task():
        try:
            with open("tasks.txt","r") as file:
                tasks = file.readlines()
            if tasks:
                print("\n Your Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}.{task.strip()}")
            else:
                print("\n No Tasks found.")
        except FileNotFoundError:
            print("\n No tasks Found.")
    def mark_done():
        try:
            with open("tasks.txt","r") as file:
                tasks = file.readlines()
            if not tasks:
                print("No Tasks")
                return
            print("\n Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}.{task.strip()}")
            choice = int(input("Enter the task number to mark as done")) - 1
            if 0<= choice <len(tasks):
                tasks[choice] = tasks[choice].strip() + "[DONE]\n"
                with open("tasks.txt","w") as file:
                    file.writelines(tasks)
                print("Marked as done")
            else:
                print("invalid")
        except FileNotFoundError:
            print("\n No tasks found.")
        except ValueError:
            print("\n Enter valid number")
    def delete_task():
        try:
            with open("tasks.txt","r") as file:
                tasks = file.readlines()
            if not tasks:
                print("No Tasks")
                return
            print("\n Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}.{task.strip()}")
            choice = int(input("Enter the task number you want to delete")) - 1
            if 0<= choice <len(tasks):
                del tasks[choice]
                with open("tasks.txt","w") as file:
                    file.writelines(tasks)
                print("Deleted")
            else:
                print("invalid")
        except FileNotFoundError:
            print("\n No tasks found.")
        except ValueError:
            print("\n Enter valid number")
        

    print("\n To Do List")
    print("1.Add a Task")
    print("2.View Tasks")
    print("3.Mark as Done")
    print("4.Delete Task")
    print("5.Exit")

    choice = input("enter your choice:")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting..")
        break
    else:
        print("invalid")




