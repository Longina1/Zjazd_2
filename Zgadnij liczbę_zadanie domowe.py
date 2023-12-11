secret_number = 13
guess = 0
count = 10
subsequent_guess = 0

for subsequent_guess in range(count):
    guess = int(input('Enter your guess: '))

    print('\nThis was your ', subsequent_guess + 1, 'guess.')
    if subsequent_guess == count:
        print('This was your last guess. You have not guessed the secret number.')
        break
    elif secret_number == guess:
        print("You've guessed it!")
        break
    elif guess > secret_number:
            print('Your number is higher than the secret number.')
            print('Enter a number from the range of infinity to', guess)
    elif guess < secret_number:
            print('Your number is lower than the secret number.')
            print('Enter a number from the range of', guess, 'to 20.')



#szukanaLiczba = 13
#zgadywanaLiczba = 0

#while zgadywanaLiczba != szukanaLiczba:
 #   zgadywanaLiczba = int(input("Odgadnij, o jakiej liczbie myślę: "))

  #  if zgadywanaLiczba == szukanaLiczba:
   #     print("Brawo! Zgadłeś")
    #elif zgadywanaLiczba < szukanaLiczba:
     #   print("Twoja liczba jest za mała")
    #elif zgadywanaLiczba > szukanaLiczba:
     #   print("Twoja liczba jest za duża")

# Ułatw użytkownikowi zgadywanie i podaj zakresy, w jakich sie obraca, np.:
#  20 >> print("Nowy przedział to: ") (nieskonczonosc, 20)
#  10 >>  print("Nowy przedział to: ") (10, 20)

# Ogranicz użytkownikowi liczbę prób do np. 10.
# liczbaProb = 10
# jeśli nie zgdałeś, to liczbaProb = liczbaProb - 1
