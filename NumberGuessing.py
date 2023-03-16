import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# generate random number between 1 and 100
secret_number = random.randint(1, 100)

# initialize the number of guesses
num_guesses = 0

# prompt the user to guess the number
while True:
    guess = int(input("Guess the number: "))
    num_guesses += 1

    if guess < secret_number:
        print("Too low, try again.")
    elif guess > secret_number:
        print("Too high, try again.")
    else:
        print(f"Congratulations! You guessed the number in {num_guesses} guesses.")
        break
