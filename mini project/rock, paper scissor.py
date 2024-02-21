import random

# Initialize variables to keep track of user and computer wins
user_wins = 0
computer_wins = 0

# List of options for the game
options = ["rock", "paper", "scissors"]

# Main game loop
while True:
    # Prompt the user to type their choice or to quit
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    
    # Check if the user wants to quit the game
    if user_input == "q":
        break

    # Check if the user's input is valid
    if user_input not in options:
        continue  # If not valid, skip to the next iteration of the loop

    # Generate a random number to represent the computer's choice
    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    # Determine the winner of the round and update the scores
    if (user_input == "rock" and computer_pick == "scissors") or \
       (user_input == "paper" and computer_pick == "rock") or \
       (user_input == "scissors" and computer_pick == "paper"):
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

# Print the final scores and a goodbye message
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")
