import random

print("Welcome to Rock Paper Scissors!")

# list of possible choices
choices = ["rock", "paper", "scissors"]

# initialize scores
player_score = 0
computer_score = 0

# prompt the user to play the game
while True:
    # get user input
    player_choice = input("Choose rock, paper, or scissors (or q to quit): ")

    # check if the user wants to quit
    if player_choice == "q":
        break

    # make sure the user input is valid
    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    # generate computer's choice
    computer_choice = random.choice(choices)

    # print out the choices
    print(f"\nYou chose {player_choice}.")
    print(f"The computer chose {computer_choice}.\n")

    # compare the choices and update scores
    if player_choice == computer_choice:
        print("Tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    # print out the scores
    print(f"\nPlayer score: {player_score}")
    print(f"Computer score: {computer_score}\n")

print("Thanks for playing!")
