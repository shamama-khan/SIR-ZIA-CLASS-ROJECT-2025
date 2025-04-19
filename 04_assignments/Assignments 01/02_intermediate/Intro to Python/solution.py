MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14
EARTH_GRAVITY = 1.0

def main():
    earth_weight = float(input("Enter a weight on Earth: "))  # Get weight on Earth
    planet = input("Enter a planet: ")  # Get the planet name

    # Determine the gravity constant for the planet
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    else:  # Default to Neptune
        gravity_constant = NEPTUNE_GRAVITY

    planetary_weight = earth_weight * gravity_constant  # Calculate weight on selected planet
    rounded_planetary_weight = round(planetary_weight, 2)  # Round to 2 decimal places
    print("The equivalent weight on " + planet + ": " + str(rounded_planetary_weight))  # Print result

if __name__ == '__main__':
    main()
