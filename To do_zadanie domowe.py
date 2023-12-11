to_do_list = []

while True:
    print("======= Menu ======= ")
    print("1. Add task")
    print("2. Display task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose one of the available options ")

    if choice == "1":
        task = input("Enter a task: ")
        to_do_list.append(task)
        print("Task added")
    elif choice == "2":
        # wyświetl zadania >> ładnie wyświetl zadania (w formie listy, jedno zadnie pod drugim)
        print("List of your tasks:", *to_do_list, sep = '\n')
    elif choice == "3":
        print("List of your tasks:", *to_do_list, sep = '\n')
        to_be_deleted = int(input("Enter the index of the task to be deleted: "))
        del to_do_list[to_be_deleted - 1]
        # zad dom. przed usuwaniem lepiej wyswietlic cala liste zadań
    elif choice == "4":
        print("List of your tasks:", *to_do_list, sep = '\n')
        break
    else:
        print("Invalid command.")
