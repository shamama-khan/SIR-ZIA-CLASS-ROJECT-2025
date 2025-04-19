# Constant to define maximum allowed length of list
MAX_LENGTH: int = 3

def shorten(lst):
    """
    Removes elements from the end of the list and prints them
    until the list is MAX_LENGTH items long.
    """
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(f"Removed: {removed_item}")

def get_lst():
    """
    Prompts the user to enter one element of the list at a time
    and returns the resulting list.
    """
    lst = []
    while True:
        elem = input("Enter an element (or press Enter to stop): ")
        if elem == "":
            break
        lst.append(elem)
    return lst

def main():
    lst = get_lst()
    print(f"\nOriginal list: {lst}")
    shorten(lst)
    print(f"Shortened list (max {MAX_LENGTH} items): {lst}")

if __name__ == '__main__':
    main()
