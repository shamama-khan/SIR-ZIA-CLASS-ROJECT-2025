def get_user_numbers():
    """
    Prompts the user to enter numbers and stores them in a list.
    Stops when the user enters a blank line.
    Returns the list of numbers.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")

        if user_input.strip() == "":
            break

        try:
            num = int(user_input)
            user_numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    return user_numbers


def count_nums(num_list):
    """
    Counts how many times each number appears in the list.
    Returns a dictionary with numbers as keys and counts as values.
    """
    num_dict = {}
    for num in num_list:
        num_dict[num] = num_dict.get(num, 0) + 1
    return num_dict


def print_counts(num_dict):
    """
    Prints the count of each number in a formatted way.
    """
    print("\n--- Number Counts ---")
    for num, count in num_dict.items():
        print(f"{num} appears {count} time{'s' if count > 1 else ''}.")


def main():
    """
    Main function to run the number counting program.
    """
    user_numbers = get_user_numbers()
    if user_numbers:
        num_counts = count_nums(user_numbers)
        print_counts(num_counts)
    else:
        print("No numbers were entered.")


if __name__ == '__main__':
    main()
