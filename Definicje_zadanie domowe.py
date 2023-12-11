#utworzenie pustego słownika
definitions = {}

while True:
    print("1. Add definition")
    print("2. Find definition")
    print("3. Delete definition")
    print("4. Display definition") # W domu
    print("5. Exit")

    choice = input("What would you like to do? ")

    if choice == "1":  # dodaj definicję
        key = input("Enter a word that needs to be defined ")
        definition = input("Enter the definition of the word: ")
        definitions[key] = definition
        print("Definition has been added\n")
    elif choice == "2":  # wyświetl definicję
        key = input("What word are you searching for? ")
        if key in definitions:
            print(key, "is", definitions[key], "\n")
        else:
            print("Definition does not exist \n")
    elif choice == "3":  # usuwanie
        key = input("What word needs to be deleted?")
        if key in definitions:
            del definitions[key]
            print("Definition has been deleted.\n")
        else:
            print("Definition does not exist \n")
    elif choice == "4":  # wyświetl wszystkie definicje
        print(definitions.items())
    elif choice == "5":
        break
    else:
        print("Invalid command")
