number_list = [1, 1, 2, 2.5, 5, -1, -5]
list = []
print('Adding to the list')
list = ['dad']
print(list)

list.append('mum')
print(list)
list = list + ['daughter', 'second daughter']
print(list)
list.extend(['brother', 'second brother'])
print(list)
list.insert(2, 'grandmother')
print(list)

print(number_list)
number_list.sort()
print(number_list)

print(number_list)
number_list.sort(reverse=True)
print(number_list)

print(number_list)
print(max(number_list))
print(min(number_list))

print(number_list.count(1))

print(list.pop())
print(list)

print(number_list.remove(1))
print(number_list)

# print(list.clear())
# print(list)

del list[-1]
print(list)
