# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if computer_choice == user_choice:
    print("You tied!")
elif (computer_choice == "r" and user_choice == "s") or (computer_choice == "p" and user_choice == "r") or (computer_choice == "s" and user_choice == "p"):
    print("You lost!")
else:
    print("You won!")