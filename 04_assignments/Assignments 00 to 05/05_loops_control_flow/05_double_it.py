def main():
    # Prompt user for an initial number
    curr_value = int(input("Enter a number: "))
    
    # Keep doubling the number and printing until it's >= 100
    while curr_value < 100:
        curr_value *= 2
        print(curr_value, end=" ")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
