def read_phone_numbers():
    """
    Allows the user to input names and phone numbers.
    Returns a dictionary representing the phonebook.
    """
    phonebook = {}  # Create an empty phonebook

    while True:
        name = input("Enter name (or press Enter to finish): ").strip()
        if name == "":
            break
        number = input(f"Enter number for {name}: ").strip()

        if name in phonebook:
            print(f"{name} already exists with number {phonebook[name]}")
            confirm = input("Do you want to update the number? (yes/no): ").lower()
            if confirm != 'yes':
                continue

        phonebook[name] = number
        print(f"Saved {name} -> {number}\n")

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all entries in the phonebook.
    """
    if not phonebook:
        print("Phonebook is empty.\n")
        return

    print("\nPhonebook Entries:")
    print("-" * 25)
    for name, number in phonebook.items():
        print(f"{name} -> {number}")
    print("-" * 25 + "\n")


def lookup_numbers(phonebook):
    """
    Allows the user to look up numbers by name.
    """
    while True:
        name = input("Enter name to lookup (or press Enter to go back): ").strip()
        if name == "":
            break
        number = phonebook.get(name)
        if number:
            print(f"{name}'s number is {number}\n")
        else:
            print(f"{name} is not in the phonebook.\n")


def main():
    print("Welcome to the Python Phonebook!\n")
    phonebook = read_phone_numbers()

    while True:
        print("Choose an option:")
        print("1. View Phonebook")
        print("2. Lookup Number")
        print("3. Add/Update Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            print_phonebook(phonebook)
        elif choice == "2":
            lookup_numbers(phonebook)
        elif choice == "3":
            phonebook.update(read_phone_numbers())
        elif choice == "4":
            print("Exiting Phonebook. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.\n")


if __name__ == '__main__':
    main()
