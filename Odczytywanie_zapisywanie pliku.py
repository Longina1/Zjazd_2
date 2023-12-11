all_names = []

with open('Imiona_nazwiska.txt', 'r', encoding='UTF-8') as file1_txt: #kodowanie z rozpoznaniem znaków
    for line in file1_txt:
        all_names.append(tuple(line.split()))

#all_names = [
  #  ('Wioletta', 'Bulczak'),
    #('Oskar', 'Piosik'),
    #('Halina', 'Parafiniuk')
#]
#print(all_names[0][1])

print(all_names)
print(all_names[0][1])

with open('firstNames', 'w', encoding='UTF-8') as file1_txt:
    for element in all_names:
        file1_txt.write(element[0]+ '\n') # zero, bo do imienia

with open('familyNames', 'w', encoding='UTF-8') as file1_txt:
    for element in all_names:
        file1_txt.write(element[1]+ '\n')
