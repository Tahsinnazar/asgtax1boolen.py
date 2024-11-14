# List of planets in the solar system
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

# Dictionary of planet characteristics
planet_characteristics = {
    "Mercury": {"has_moons": False, "is_gas_giant": False},
    "Venus": {"has_moons": False, "is_gas_giant": False},
    "Earth": {"has_moons": True, "is_gas_giant": False},
    "Mars": {"has_moons": True, "is_gas_giant": False},
    "Jupiter": {"has_moons": True, "is_gas_giant": True},
    "Saturn": {"has_moons": True, "is_gas_giant": True},
    "Uranus": {"has_moons": True, "is_gas_giant": True},
    "Neptune": {"has_moons": True, "is_gas_giant": True},
    "Pluto": {"has_moons": True, "is_gas_giant": False}
}

# Function to check if a planet has moons
def has_moons(planet):
    return planet_characteristics[planet]["has_moons"]

# Function to check if a planet is a gas giant
def is_gas_giant(planet):
    return planet_characteristics[planet]["is_gas_giant"]

# Display information about each planet
for planet in planets:
    print(f"{planet}:")
    print(f"  Has moons: {has_moons(planet)}")
    print(f"  Is a gas giant: {is_gas_giant(planet)}")
    print()
