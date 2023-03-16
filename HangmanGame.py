import random

print("Welcome to Hangman!")

# list of possible words
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

# select a random word from the list
word = random.choice(words)

# initialize the number of guesses and the list of guessed letters
num_guesses = 6
guessed_letters = []

# prompt the user to guess the word
while num_guesses > 0:
    # print out the current state of the word
    word_state = ""
    for letter in word:
        if letter in guessed_letters:
            word_state += letter
        else:
            word_state += "_"
    print(f"\nWord: {word_state}")

    # prompt the user to guess a letter
    guess = input("Guess a letter: ")

    # make sure the user input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please try again.")
        continue

    # check if the letter has already been guessed
    if guess in guessed_letters:
        print("You already guessed that letter. Please try again.")
        continue

    # add the guessed letter to the list
    guessed_letters.append(guess)

    # check if the guessed letter is in the word
    if guess in word:
        print("Correct!")
    else:
        print("Incorrect.")
        num_guesses -= 1

    # check if the user has guessed the entire word
    if set(word) == set(guessed_letters):
        print(f"\nCongratulations! You guessed the word '{word}'!")
        break

# check if the user has run out of guesses
if num_guesses == 0:
    print(f"\nSorry, you ran out of guesses. The word was '{word}'.")
