# Define the affirmation
affirmation = "I am capable of doing anything I put my mind to."

def get_affirmation():
    # Ask the user to type the affirmation
    print(f"Please type the following affirmation: {affirmation}")
    return input()

def main():
    user_input = get_affirmation()

    # Keep asking for the correct affirmation until it matches
    while user_input != affirmation:
        print("Hmmm, that was not quite it.")
        user_input = get_affirmation()

    # Congratulate the user when they get it right
    print("That's right! :) You've got it!")

# Start the program
if __name__ == "__main__":
    main()
