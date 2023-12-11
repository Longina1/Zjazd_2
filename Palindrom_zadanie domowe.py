phrase_list = ["Ewo, żeby tu były buty beżowe", "Mer kilowy woli krem"]
list_without_spaces = []

phrase1 = phrase_list[0].replace(' ', '').replace(',', '').lower()
list_without_spaces.append(phrase1)

phrase2 = phrase_list[1].replace(' ', '').replace(',', '').lower()
list_without_spaces.append(phrase2)

for phrase in list_without_spaces:
    print('\nPhrase being checked: ', phrase)
    if list_without_spaces[0] == list_without_spaces[0][::-1]:
        print('This phrase is a palindrome.')
    else:
        print('This phrase is not a palindrome.')

phrase = input('Enter a phrase without any punctuation signs: ').replace(' ', '').lower()
print(phrase)
reversed_phrase = phrase[::-1]
if phrase == reversed_phrase:
    print('This phrase is a palindrome.')
else:
    print('This phrase is not a palindrome.')
