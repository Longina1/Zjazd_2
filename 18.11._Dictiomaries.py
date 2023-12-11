person = {
    'Name': 'John',
    'Age': 36,
    'Weight': 90
}
print(person['Name'])

digits = {
    0: 'zero',
    1: 'one',
    2: 'two'
}
print(digits[0])

cars = {
    ('Toyota', 'Yaris'): 'PL1234',
    ('Toyota', 'Aygo'): 'PL5678'
}
print(cars)

person['Email'] = 'john@mail.pl'
print(person)
person['Email'] = 'john1@mail.pl'
print(person)

del person['Email']
print(person)

person['Age'] = 37
print(person)

digits.update({3: 'three', 4: 'four'})
print(digits)

if 3 in digits:
    print('3 is already defined.')

if 5 not in digits:
    print('5 is not defined.')

print(len(digits))
# len = od przecinka do przecinka

print(person.get('Age'))
print(person.get('Address', 0)) # żeby się zabezpieczyć przed error

print('Keys of the dictionary: ', person.keys())
print('Keys of the dictionary: ', person.values())
print('Items of the dictionary: ', person.items())

for key in person:
    print('Key: ', key)

for value in person:
    print('Value: ', value)

for key, value in person.items():
    print('Key: ', key, 'has the following value: ', value)
