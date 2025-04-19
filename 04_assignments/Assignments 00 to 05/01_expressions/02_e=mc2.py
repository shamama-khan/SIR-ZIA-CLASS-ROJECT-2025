C: int = 299792458  # The speed of light in m/s

def main():
    while True:
        user_input = input("Enter kilos of mass (or 'q' to quit): ")
        
        if user_input.lower() in ['q', 'quit']:
            print("Goodbye!")
            break

        try:
            mass_in_kg: float = float(user_input)

            # Calculate energy
            energy_in_joules: float = mass_in_kg * (C ** 2)

            # Display work to the user
            print("\ne = m * C^2...")
            print("m = " + str(mass_in_kg) + " kg")
            print("C = " + str(C) + " m/s")
            print(str(energy_in_joules) + " joules of energy!\n")

        except ValueError:
            print("Please enter a valid number or 'q' to quit.\n")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
