def main():
    # Conversion factors for each planet (compared to Earth's gravity)
    planet_gravities = {
        "Mercury": 0.38,
        "Venus": 0.91,
        "Earth": 1.0,
        "Mars": 0.38,
        "Jupiter": 2.34,
        "Saturn": 1.06,
        "Uranus": 0.92,
        "Neptune": 1.19
    }

    # Prompt the user for weight on Earth
    weight_earth = float(input("Enter your weight on Earth (in kg): "))

    # Prompt the user for a planet
    planet = input("Enter the name of the planet: ")

    # Check if the planet is valid and calculate the weight on that planet
    if planet in planet_gravities:
        weight_planet = weight_earth * planet_gravities[planet]
        print(f"Your weight on {planet} would be {weight_planet:.2f} kg.")
    else:
        print("Sorry, the planet name is not recognized or not supported.")

if __name__ == "__main__":
    main()
