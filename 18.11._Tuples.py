
my_tuple = (1, 1, 1, 1, 1, 1, 2, 3, 4, 5, True, False, 'dom')

list = ['daughter', 'second daughter']
my_tuple2 = tuple(list)
print('Tuple: ', my_tuple2, 'and the type is:', type(my_tuple2))

print(my_tuple2[0])

#działają metody dla listy, jeśli lista w tuple:
#my_tuple2[0].append('Cat is brown')

my_big_tuple = my_tuple + my_tuple2
print(my_big_tuple)

#wypisanie kilka razy na ekranie, ale nie jest modyfikacją
print(my_tuple * 3)

print(my_tuple.count(1))
print(len(my_big_tuple))
print(my_tuple.index(5))

i = 0
for element in my_big_tuple:
    print(i, ':', element)
    i += 1

print(my_big_tuple)
print(my_big_tuple[::-1])

