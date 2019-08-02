import random

# A list of words that are
potential_words = ["starbucks", "spaghetti", "icecream", "pancakes", "subway"]

word = random.choice(potential_words)

# Use to test your code:
# print(word)

# Converts the word to lowercase
word = word.lower()

current_word = ["'__'"*len(word)]


# Some useful variables
guesses = []
maxfails = 6
fails = 0

while fails < maxfails:
    guess = input("Guess a letter:")
    # check if the guess is valid: Is it one letter? Have they already guessed it?# check if the guess is correct: Is it in the word? If so, reveal the letters!
    if len(guess) > 1:
        print("This is not a valid guess. Please answer only 1 letter.")
    elif guess in guesses:
        print("You have already guessed this.")
    elif guess in word:
        for i in range(len(word)):
            if guess == word[i]:
                current_word[i] = guess

    else:
        print("Sorry that letter is not in the word.")
        fails = fails+1
        print("You have " + str(maxfails - fails) + " tries left!")
        guesses.append(guess)

        print(current_word)
