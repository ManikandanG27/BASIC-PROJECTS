# Prompt the user to input their name and greet them
name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

# Prompt the user to choose a direction
answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

# Handling the user's choice to go left
if answer == "left":
    # Prompt the user to decide how to cross the river
    answer = input(
        "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

    # Handling the user's choice to swim or walk around the river
    if answer == "swim":
        print("You swam acrross and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')  # Error message for invalid input

# Handling the user's choice to go right
elif answer == "right":
    # Prompt the user to decide whether to cross the bridge or go back
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    # Handling the user's choice to cross the bridge or go back
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        # Prompt the user to decide whether to talk to a stranger
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        # Handling the user's choice to talk to the stranger or not
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print('Not a valid option. You lose.')  # Error message for invalid input
    else:
        print('Not a valid option. You lose.')  # Error message for invalid input

else:
    print('Not a valid option. You lose.')  # Error message for invalid input

# Thanking the user for playing the game
print("Thank you for trying", name)
