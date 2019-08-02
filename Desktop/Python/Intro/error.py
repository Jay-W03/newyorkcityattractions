number = [4, 10, 12, 33, 54, 95]
tries = 0
#if they choose a number in the list, say good job and end program
while tries < 3:
    choose = int(input("Guess a number between 0 and 100"))
    if choose in number:
        print("good choice!")
        break

    else:
        print("Sorry, try again")
        tries += 1 #increases tries by one
