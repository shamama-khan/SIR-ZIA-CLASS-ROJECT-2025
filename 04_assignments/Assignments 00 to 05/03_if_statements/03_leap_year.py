def is_leap_year(year: int) -> bool:
    """
    Determines whether the given year is a leap year based on Gregorian calendar rules.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def main():
    # Ask the user to enter a year
    try:
        year = int(input("Enter a year: "))
        if is_leap_year(year):
            print("That's a leap year!")
        else:
            print("That's not a leap year.")
    except ValueError:
        print("Invalid input. Please enter a valid integer year.")


if __name__ == '__main__':
    main()
