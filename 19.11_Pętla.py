outcome = 0
count = 0

#while count < 3:
 #   x = float(input('Enter a non-negative number: '))
   # if x >= 0:
      #  outcome += x # zwiększa wynik o pdaną liczbę przez użytkownika
   # else:
      #  print('Your number is negative.')
       # #break # przeywa pętlę i program
        #continue # pomija jedną iterację pętli
    #print('Current outcome: ', outcome)
    #count += 1 #ręcznie zwiększyć licznik

for i in range(3):
    x = float(input('Enter a non-negative number: '))
    if x >= 0:
        outcome += x # zwiększa wynik o pdaną liczbę przez użytkownika
    else:
        print('Your number is negative.')
        #break # przeywa pętlę i program
        continue # tylko trzy próby
    print('Current outcome: ', outcome)
