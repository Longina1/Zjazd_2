secret_number = 13
user_guess = 0

while user_guess != secret_number:
    user_guess = int(input('Enter your guess: '))

    if user_guess == secret_number:
        print('You have guessed!')
    elif user_guess < secret_number:
        print('Your number is lower than the secret number.')
    elif user_guess > secret_number:
        print('Your number is higher than the secret number.')

# 20 >> print('New range: nieskończoność, 20)
# 10 >> print('Nowy przedział: 10, 20)
# ogranicz liczbę prób do 10 (dodać zmienną count = 10, pomniejsza o -1)
