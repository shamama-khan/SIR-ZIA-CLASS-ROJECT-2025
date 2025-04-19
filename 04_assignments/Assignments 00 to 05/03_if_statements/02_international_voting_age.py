# Define the voting ages for each fictional country
VOTING_AGES = {
    "Peturksbouipo": 16,
    "Stanlau": 25,
    "Mayengua": 48
}

def main():
    # Get the user's age
    try:
        user_age = int(input("How old are you? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # Check voting eligibility for each country
    for country, age_limit in VOTING_AGES.items():
        if user_age >= age_limit:
            print(f"You can vote in {country} where the voting age is {age_limit}.")
        else:
            print(f"You cannot vote in {country} where the voting age is {age_limit}.")

# Run the program
if __name__ == '__main__':
    main()
