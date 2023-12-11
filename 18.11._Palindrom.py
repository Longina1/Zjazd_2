word_list = ['kajak', 'mama', 'axa', 'myszka']
# pytaj użytkomika o słowa, dodać je do listy lub nie i sprawdzić

#liczba iteracji = długość słowa / 2

flag_is_palindrome = True

for word in word_list:
    print('\nWord being checked: ', word)
    number_of_iterations = len(word) // 2
    for i in range(number_of_iterations):
        if word[i] != word[-1 - i]:
            print('Letters', word[i], 'are not equal.')
            print('Word', word, 'is not a palindorme.')
            flag_is_palindrome = False
            break
    else:
        print('Letter', word[i], ' is fine.')
        print('Word', word, 'is a palindrome.')

if flag_is_palindrome:
    print('Word', word, 'is a palindrome.')
else:
    print('Word', word, 'is not a palindrome.')


# Opcja druga

word_list = ['kajak', 'mama', 'axa', 'myszka']
for word in word_list:
    print('\nWord being checked: ', word)
    word_backword = word [::-1]
    if word_backword == word:
        print('Word', word, 'is a palindrome.')
    else:
        print('Word', word,'is not a palindrome.')


# Sprawdzić, czy zdanie jest palindromem, ignorując spacje
# phrase_list = [Ewo
