print("Welcome to Mad Libs Generator!")

# Asking user for inputs
name = input("Enter a name: ")
place = input("Enter a place: ")
verb1 = input("Enter a verb: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
verb2 = input("Enter another verb: ")
noun3 = input("Enter a third noun: ")

# Printing out the Mad Libs story
print(f"\n{name} went to {place} to {verb1}.")
print(f"When {name} got there, they saw a {noun1} and a {noun2}.")
print(f"{name} thought that the {noun1} was {adjective1} and the {noun2} was {adjective2}.")
print(f"{name} decided to {verb2} the {noun1} and take the {noun2} home with them.")
print(f"On the way home, {name} saw a {noun3} and thought about how much fun they had at {place}.")
