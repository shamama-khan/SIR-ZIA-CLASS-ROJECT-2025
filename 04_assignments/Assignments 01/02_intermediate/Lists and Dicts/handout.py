# Function to access an element at a given index
def access_element(lst, index):
    if index < 0 or index >= len(lst):
        return "Index out of range."
    return lst[index]

# Function to modify an element at a given index
def modify_element(lst, index, new_value):
    if index < 0 or index >= len(lst):
        return "Index out of range."
    lst[index] = new_value
    return lst

# Function to slice the list from a start index to an end index
def slice_list(lst, start_index, end_index):
    if start_index < 0 or end_index > len(lst) or start_index >= end_index:
        return "Invalid indices."
    return lst[start_index:end_index]

# Game function to interact with the user
def game():
    lst = [10, 'apple', 3.14, 'orange', 42]
    
    while True:
        print("\nCurrent List:", lst)
        print("Select an operation:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice list")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
        if choice == '1':
            index = int(input("Enter the index: "))
            print("Element at index:", access_element(lst, index))
        
        elif choice == '2':
            index = int(input("Enter the index: "))
            new_value = input("Enter the new value: ")
            print("Updated List:", modify_element(lst, index, new_value))
        
        elif choice == '3':
            start_index = int(input("Enter the start index: "))
            end_index = int(input("Enter the end index: "))
            print("Sliced List:", slice_list(lst, start_index, end_index))
        
        elif choice == '4':
            print("Exiting game.")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    game()
