# Planet gravity constants compared to Earth's gravity
planet_gravity = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.360,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.140
}

# Get the user's weight on Earth
earth_weight = float(input("Enter a weight on Earth: "))

# Get the name of the planet
planet = input("Enter a planet: ")

# Check if the planet is in the dictionary
if planet in planet_gravity:
    # Calculate the weight on the specified planet
    planet_weight = earth_weight * planet_gravity[planet]
    
    # Round the result to 2 decimal places
    rounded_planet_weight = round(planet_weight, 2)
    
    # Output the equivalent weight on the planet
    print(f"The equivalent weight on {planet}: {rounded_planet_weight}")
else:
    print("Invalid planet name!")
