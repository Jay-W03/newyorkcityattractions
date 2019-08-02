from random import *
tries = 0 #sets number of tries to 0
aRandomNumber = randint(1,20)
# For Testing Purposes: print (aRandomNumber)

while tries < 3:
    guess = input("Guess a number between 1 and 20 (inclusive): ")
    if not guess.isnumeric():
        print("That's not a positive whole number, try again!")
    else:
        guess = int(guess)

        tries += 1

        if guess == aRandomNumber:
            print("You got it!", aRandomNumber, "was the number")
            break
        elif tries == 3:
            print("You failed!Try again.")

        elif guess < aRandomNumber:
            print("Try a higher number!")

        elif guess > aRandomNumber:
                print("Try a lower number!")
