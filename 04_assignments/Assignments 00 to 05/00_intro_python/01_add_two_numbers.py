def main():
    print("This program adds two numbers")
    num1 : str = input("Enter the first number: ")
    num1: int = int(num1)
    num2 : str = input("Enter the second number: ")
    num2: int = int(num2)
    print(f"The sum of {num1} and {num2} is {num1 + num2}")

if __name__ == "__main__":
    main()