import random

# Set the likelihood that we'll randomly decide to stop
DONE_LIKELIHOOD = 0.3  # You can adjust this number (0.0 to 1.0) for testing

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return  # Exit early if done() returns True
        print(curr_num, end=' ')  # Print numbers on the same line

# There is no need to edit code beyond this point

def done():
    """ Returns True with a probability of DONE_LIKELIHOOD """
    return random.random() < DONE_LIKELIHOOD

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done")  # Move to new line before printing "I'm done"

if __name__ == "__main__":
    main()
