from typing import List

def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)

print(list_avg([1, 2, 4, 3]))

def calculate_escape_velocity(mass, radius, G = 6.67430e-11) -> float:
    return (2 * G * mass / radius) ** 0.5

earth_mass = 5.972e24
earch_radius = 6.371e6
earth_escape_velocity = calculate_escape_velocity(mass = earth_mass, radius = earch_radius)
print(f"Earth Escape Velocity: {earth_escape_velocity/1000:.2f} km/s")
