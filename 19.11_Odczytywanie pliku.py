with open('My file.txt', 'r') as file1:
    #content = file1.read(5)
    #print(content)
    content = file1.read()
    #print(content)

#plik już zamknięty, ale zawrtość nadal jest, poza instrukcją with open
print(content)

#liczba unikalnych słów
print('Type of the variable before the split method: ', type(content))
#content = content.split() # ze str na list
content = content.lower().replace(',', '').replace('(', '').replace(')', '').replace('.', '').split()

print('Type of the variable after the split method: ', type(content))
print(content)
print(content[15])

content = set(content)
#liczba elementów listy:
print('Number of words in the file:', len(content))
print(content)




