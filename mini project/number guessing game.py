import random

# Initialize the variable to count the number of guesses
guess_taken = 0

# Prompt the user to input their name
print("hello! what is your name? ")
name = input()

# Generate a random number between 1 and 30
num = random.randint(0, 30)

# Prompt the user to guess the number
guess = int(input(name + ", I am thinking of a number between 1 and 30, can you guess what it is? "))

# Loop to allow the user to guess the number up to 4 times
while guess_taken < 4:
    if guess < num:
        print("You need to guess higher.... Try again")
    else:
        print("You need to guess lower.... Try again")
    
    # Prompt the user to guess a number between 1 and 30 again
    guess = int(input("Guess a number between 1 and 30: "))
    guess_taken += 1

    # Break out of the loop if the guess is correct
    if guess == num:
        break

# Check if the guess is correct and provide appropriate output
if guess == num:
    guess_taken = str(guess_taken)
    print("Good job, " + name + "! You guessed my number in " + guess_taken + " guesses.")
else:
    print("Sorry, " + name + ", the number I was thinking of was", num)
