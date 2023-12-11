# dodaj zadania, wyświetl zadanie, usuń zadanie, zakończ program
# po wybraniu opcji, program wykonuje daną czynność

to_do = []

while True:
    print( '''=========== Menu ==========
            1. Add task
            2. Display task
            3. Delete task
            4. Exit
        ''')

    choice = input('Choose one option from the menu: ')

    if choice == '4':
            break
    elif choice == '1':
        print('Add task')
        task = input('Enter your task: ')
        to_do.append(task)
        print('Task added')
    if choice == '2':
        print('Display task')
        # ładnie wyświetl zadania w formie listy jednoo zadanie pod drugim
        for i in to_do:
            print('i')
    if choice == '3':
        print('Delete task')
        task_to_delete = int(input('Enter the index of the task to be deleted: '))
        del to_do[task_to_delete]
        #przed usuwaniem wyświetlić całą listę zadań
        # usunąć za pomocą indeksu (numer 3, nie nazwę)
        break
    else:
        print('Invalid command')



