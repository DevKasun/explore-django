class SpaceX:
    def __init__(self, *rockets):
        self.rockets = rockets

    def get_rocket_details(self):
        # for rocket in self.Rockets:
        #     print(f"Name: {rocket.name} | Landing Method: {rocket.landing_method}")
        details = []
        for rocket in self.rockets:
            details.append(f"Name: {rocket.name} | Landing method: {rocket.landing_method}")
        return "\n".join(details)

    def __repr__(self):
        return f"SpaceX has {len(self.rockets)} rockets"


class Rocket:
    def __init__(self, name, landing_method):
        self.name = name
        self.landing_method = landing_method


startship = Rocket("Starship", "Drone Ship")
falcon9 = Rocket("Falcon 9", "Ground")
spacex = SpaceX(startship, falcon9)
print(spacex)

print(spacex.get_rocket_details())
