def get_first_element(lst):
    """
    Prints the first element of the provided non-empty list.
    """
    print("The first element in the list is:", lst[0])

def get_list_from_user():
    """
    Prompts the user to enter elements of the list one by one.
    Returns the resulting list.
    """
    lst = []
    while True:
        elem = input("Enter an element (or press Enter to stop): ")
        if elem == "":
            break
        lst.append(elem)
    return lst

def main():
    user_list = get_list_from_user()
    if user_list:  # Just an extra safety check
        get_first_element(user_list)

if __name__ == '__main__':
    main()
