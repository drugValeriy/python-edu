from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
own = 0
# Start your game!
while guesses_left > 0:
    
    while True:
        guess = raw_input("Guess my random from 1 to 10: ")
        int_guess = int(guess)
        if isinstance(int_guess, int): 
            break
        else: 
            print('DO YOU KNOW ENGLISH! TRIES! INTEGER BIATCH!')
    if int(int_guess) == random_number:
        print "You win!"
        break
    else:
        print "Nope!"
        guesses_left -= 1
    if guesses_left == 0:
        print "You suck"
        while True:
            new_try = raw_input('How many tries you need: ')
            int_try = int(new_try)
            if isinstance(int_try, int): 
                break
            else: 
                print('DO YOU KNOW ENGLISH! TRIES! INTEGER BIATCH!')
        if int_try == 0:
            print "YOU OWN ME %d$ BIATCH. WHERE IS MY MONEY!? WHERE IS MY MONEY BIATCH?!" % own
            break
        own += int_try * 100
        print "YOU OWN ME %d$ BIATCH" % own
        guesses_left += int_try

    