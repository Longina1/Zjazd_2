digits = {0, 1, 2, 3, 4, 5, 6}

my_set = {'mama', 'pies', False, True, 2, 5, 0, 1}
print(my_set)
# nie ma zera, bo False=0, a True=1

my_tuple = (1, 2, 3, 4, 5, 6, 6)
my_set2 = set(my_tuple)
print(my_set2)

body = {'head', ('left hand', 'right hand'), 'belly'}
# tu nie może być list [], ale może być tuple w środku

if 'head' in body:
    print('You are bariny!')

print(len(my_set2))

letters = {'a', 'b', 'c'}
letters2 = {'b', 'c', 'd', 'e'}

print(letters.union(letters2))
sum = letters | letters2
print(sum)
print(letters.intersection(letters2)) #część wspólna
sum = letters & letters2
print(letters.difference(letters2)) # 1- 2
difference = letters - letters2
print(letters.symmetric_difference(letters2)) # wszystko bez części wspólnej
symetic_difference = letters ^ letters2

letters.update({'g', 'h'})
print(letters)
letters.add('i')
print(letters)
letters.remove('a')
print(letters)
