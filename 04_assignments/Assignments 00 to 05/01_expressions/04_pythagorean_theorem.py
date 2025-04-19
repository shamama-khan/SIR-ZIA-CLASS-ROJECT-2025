import math  # Import the math library so we can use the sqrt function

def main():
    # Get the two side lengths from the user and cast them to be numbers
    side_ab: float = float(input("Enter the length of AB: "))
    side_ac: float = float(input("Enter the length of AC: "))

    # Calculate the hypotenuse using the two sides and print it out
    hypotenuse: float = math.sqrt(side_ab**2 + side_ac**2)
    print(f"The length of BC (the hypotenuse) is: {hypotenuse:.2f}")

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
