class Rocket:
    def __init__(self, name, height, weight, fuel_level=100):
        self.name = name
        self.height = height
        self.weight = weight
        self.fuel_level = fuel_level

    def check_fuel_level(self):
        return f"{self.name} fuel level: {self.fuel_level}%"

    def launch(self):
        if self.fuel_level >= 95:
            return f"{self.name} has launched successfully 🚀"
        return f"Insufficient fuel level to launch {self.name} 🛑"

class SpaceXRocket(Rocket):
    def __init__(self, name, weight, height, booster_recovery_method, landing_attempts=0, reusable=True):
        super().__init__(name, weight, height)
        self.landing_attempts = landing_attempts
        self.booster_recovery_method = booster_recovery_method
        self.reusable = reusable

    def land_rocket(self):
        if self.reusable:
            self.landing_attempts += 1
            return f"{self.name} has landed successfully 🛬"
        return f"{self.name} is not reusable"

    def check_landing_attempts(self):
        return f"{self.name} landing attempts: {self.landing_attempts}"

    def __repr__(self):
        return f"<Rocket: {self.name}, Height: {self.height}, Weight: {self.weight}, Fuel Level: {self.fuel_level}, Reusable: {self.reusable}, Booster recovery methods: {self.booster_recovery_method}, No. of landing attempts: {self.landing_attempts}>"

starship = SpaceXRocket("Starship", 120, 50, "Drone Ship", 5)
print(starship)
