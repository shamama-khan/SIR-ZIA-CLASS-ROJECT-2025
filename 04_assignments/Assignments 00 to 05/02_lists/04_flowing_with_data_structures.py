# This function modifies the list in place by adding three copies of the data
def add_three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)  # Mutating the list directly (mutable data type)

# No need to edit code past this point
def main():
    message = input("Enter a message to copy: ")
    my_list = []
    print("List before:", my_list)
    add_three_copies(my_list, message)
    print("List after:", my_list)

if __name__ == "__main__":
    main()
