word_list = ['kajak', 'mama', 'axa', 'mysz']

for word in word_list:
    print('\nWord being checked: ', word)

    number_of_iterations = len(word) // 2

    flag_if_palindrome = True

    for i in range(number_of_iterations):
        if word[i] != word[-1 - i]:
            print('Letter', word[i], 'does not match.')
            flag_if_palindrome = False
            break
        else:
            print('Letter', word[i], 'matches.')

        if flag_if_palindrome:
            print('Word', word, 'is a palindrome.')
        else:
            print('Word', word, 'is not a palindrome.')
