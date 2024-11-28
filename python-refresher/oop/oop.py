class Planet:
    def __init__(self, name, mass, diameter, distance_from_sun, sun_type):
        self.name = name
        self.mass = mass
        self.diameter = diameter
        self.distance_from_sun = distance_from_sun
        self.sun_type = sun_type

    def calculate_surface_gravity(self):
        G = 6.67430e-11  # gravitational constant
        radius = self.diameter  * 500
        return (G * self.mass) / (radius ** 2)

    def calculate_surface_area(self):
        import math
        return 4 * math.pi * (self.diameter / 2) ** 2

    def get_planet_info(self):
        return f"""
        Planet: {self.name}
        Star Type: {self.sun_type}
        Mass: {self.mass} kg
        Diameter: {self.diameter} km
        Distance from Sun: {self.distance_from_sun} km
        Surface Gravity: {self.calculate_surface_gravity():.2f} m/s²
        Surface Area: {self.calculate_surface_area():.2f} km²
        """


earth = Planet(
    name="Earth",
    mass=5.972e24,
    diameter=12742,
    distance_from_sun=149.6e6,
    sun_type="Yellow Dwarf"
)
mars = Planet(
    name="Mars",
    mass=6.39e23,
    diameter=6779,
    distance_from_sun=227.9e6,
    sun_type="Yellow Dwarf"
)

print(mars.get_planet_info())

# ------------------------------------------------------------------

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (90, 90, 93, 78, 90))
student2 = Student("Rolf", (90, 80, 93, 70, 88))

print(student.grades)
# print(student.average_grade())
# print(student2.average_grade())

# ------------------------------------------------------------------

# __str__ method and __repr__ method

class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    # def __str__(self):
    #     return f"{self.name} ({self.year})"

    def __repr__(self):
        return f"<Movie {self.name} ({self.year})>"

movie = Movie("The Matrix", 1999)
print(movie)
