

definitions = {}

while True:
    print('1. Add definition')
    print('2. Search for definition')
    print('3. Delete definition')
    print('4. Dispaly all definitions')
    print('5. Exit')

    choice = input('What do you want to do? ')

    if choice == '1':
        key = input('Enter key word to be defined: ')
        definition = input('Enter definition of word: ')
        definitions[key] = definition
        print('Definition added')
    elif choice == '2':
        key = input('What word are you searching for? ')
        if key in definitions:
            print(definitions[key])
        else:
            print('Definition does not exist')
    elif choice == '3':
        key = input('Enter a word to be deleted: ')
        if key in definitions:
            del definitions[key]
            print('Definition deleted')
        else:
            print('Definition does not exist')
    elif choice == '4':
        pass # wyświetl wszystkie definicje
    elif choice == '5':
        break
    else:
        print('Invalid command')

