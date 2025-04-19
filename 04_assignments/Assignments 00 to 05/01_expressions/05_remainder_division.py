def main():
    # Get the numbers we want to divide
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    if divisor == 0:
        print("Error: Division by zero is not allowed.")
        return
    
    quotient: int = dividend // divisor  # Integer division (no remainder)
    remainder: int = dividend % divisor  # Get the remainder of the division
    
    # Improved output formatting
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
