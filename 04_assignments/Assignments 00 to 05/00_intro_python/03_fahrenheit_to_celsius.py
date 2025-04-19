def main():
    # Prompt the user to enter temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius using the correct formula
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Output the result
    print(f"Temperature: {fahrenheit}F = {celsius}C")

if __name__ == '__main__':
    main()
