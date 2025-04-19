def add_many_numbers(numbers: list[int]) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    This version uses the built-in sum() function for a cleaner solution.
    """
    return sum(numbers)

# There is no need to edit code beyond this point

def main():
    numbers: list[int] = [12, 43, 23, 41, 98]  # Make a list of numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # Find the sum of the list
    print(sum_of_numbers)  # Print out the sum above
    

if __name__ == '__main__':
    main()
