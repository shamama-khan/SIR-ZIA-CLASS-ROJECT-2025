import random

# Number of sides on each die to roll
NUM_SIDES: int = 6

def roll_dice():
    # Roll die
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    
    # Get their total
    total: int = die1 + die2
    
    # Print out the results
    print(f"\nDice have {NUM_SIDES} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")
    
def main():
    while True:
        # Simulate rolling the dice
        roll_dice()
        
        # Ask the user if they want to roll again
        roll_again = input("\nDo you want to roll again? (y/n): ").strip().lower()
        if roll_again != 'y':
            print("Thanks for playing!")
            break

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
