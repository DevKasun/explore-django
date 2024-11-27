def user_age_in_minutes():
    input_value = input("Enter you age:")
    int_input = int(input_value)
    print(int_input * 365 * 24 * 60)

# user_age_in_minutes()


def get_the_monthly_saving_rate(income, savings):
    saving_rate = (savings / income) * 100
    if saving_rate > 10:
        print("|")
        print("|")
        print(f"Your monthly saving rate is: {saving_rate:.2f}%")
        print("** ✅ You are doing great! ***")
    else:
        print("|")
        print("|")
        print(f"Your monthly saving rate is: {saving_rate:.2f}%")
        print("***❗️ You need to save more! ***")


# monthly_income = float(input("Enter your monthly income: "))
# monthly_savings = float(input("Enter your monthly savings: "))

# get_the_monthly_saving_rate(income = monthly_income, savings = monthly_savings)


# Functions return values
# Example

# G = 6.67430e-11 this is  gravitational constant
def calculate_escape_velocity(mass, radius, G = 6.67430e-11):
    return (2 * G * mass / radius) ** 0.5

earth_mass = 5.972e24
earch_radius = 6.371e6
earth_escape_velocity = calculate_escape_velocity(mass = earth_mass, radius = earch_radius)
print(f"Earth Escape Velocity: {earth_escape_velocity/1000:.2f} km/s")

moon_mass = 7.34e22
moon_radius = 1.737e6
moon_escape_velocity = calculate_escape_velocity(mass = moon_mass, radius = moon_radius)
print(f"Moon Escape Velocity: {moon_escape_velocity/1000:.2f} km/s")
