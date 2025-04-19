import random

def guess_my_number():
    number_to_guess = random.randint(1, 99)
    print("\n🎯 Welcome to 'Guess My Number' Game!")
    print("🤔 I'm thinking of a number between 1 and 99. Can you guess it?\n")

    attempts = 0

    while True:
        try:
            user_input = int(input("👉 Your guess: "))
            attempts += 1

            if user_input < number_to_guess:
                print("📉 Too low! Try a higher number.\n")
            elif user_input > number_to_guess:
                print("📈 Too high! Try a lower number.\n")
            else:
                print(f"🎉 Congratulations! You guessed it right in {attempts} tries.")
                print(f"✅ The number was: {number_to_guess}")
                break

        except ValueError:
            print("⚠️ Please enter a valid number!\n")

if __name__ == "__main__":
    guess_my_number()
