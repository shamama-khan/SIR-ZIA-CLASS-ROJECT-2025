import random

def high_low_game():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0
    rounds = 5

    for round_number in range(1, rounds + 1):
        print(f"\nRound {round_number}")
        user_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)

        print(f"Your number is {user_number}")
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

        if (guess == "higher" and user_number > computer_number) or (guess == "lower" and user_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}")

    print("\nThanks for playing!")

high_low_game()
