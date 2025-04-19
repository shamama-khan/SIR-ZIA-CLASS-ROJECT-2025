def in_range(n, low, high):
    return low <= n <= high

def main():
    # Example usage
    print(in_range(5, 1, 10))  # True
    print(in_range(0, 1, 10))  # False

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
