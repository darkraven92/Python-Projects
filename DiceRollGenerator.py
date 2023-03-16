import random

print("Welcome to the Dice Roll Generator!")

# prompt the user to roll the dice
while True:
    roll = input("Press enter to roll the dice (or q to quit): ")

    # check if the user wants to quit
    if roll == "q":
        break

    # generate random numbers between 1 and 6 for each dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    # print out the results
    print(f"\nYou rolled a {dice1} and a {dice2}.")
    print(f"Total: {dice1 + dice2}\n")

print("Thanks for rolling the dice!")
