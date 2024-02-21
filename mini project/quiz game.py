# Print welcome message
print("Welcome to Learn with Asprit")

# Prompt the player to decide if they want to play
player = input("Do you want to play? ")

# If the player does not want to play, quit the game
if player.lower() != "yes":
    quit()

# Print a message to start the game
print("Ok, let's play")

# Initialize the score variable
score = 0

# Ask the first question and check if the answer is correct
question = input("How many days do we have in a week? ")
if question.lower() == "seven":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Ask the second question and check if the answer is correct
question = input("In which direction does the sun rise? ")
if question.lower() == "east":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Ask the third question and check if the answer is correct
question = input("What is our national bird? ")
if question.lower() == "peacock":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Ask the fourth question and check if the answer is correct
question = input("Which is the fastest animal on land? ")
if question.lower() == "cheetah":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Print the player's score
print("Your correct answers are: " + str(score))
