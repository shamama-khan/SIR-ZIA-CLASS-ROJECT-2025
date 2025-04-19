INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches in 1 foot.

def main():
    feet: float = float(input("Enter the number of feet: "))  # Get the number of feet from the user (cast to float)
    inches: float = feet * INCHES_IN_FOOT  # Convert feet to inches using the conversion factor
    print(f"{feet} feet is equal to {inches} inches.")  # Print the result with clearer formatting

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()