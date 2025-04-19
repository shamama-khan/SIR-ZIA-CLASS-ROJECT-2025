def main():
    # Initialize an empty list to store user inputs
    values_list = []

    while True:
        # Prompt user for input
        user_input = input("Enter a value (or press Enter to finish): ")
        
        # If the input is empty, break the loop
        if user_input == "":
            break
        
        # Add the input to the list
        values_list.append(user_input)

    # Print the final list
    print("Here's the list:", values_list)


# Start the program
if __name__ == '__main__':
    main()
