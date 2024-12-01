from typing import List


class SpaceX:
    def __init__(self, *rockets):
        self.rockets = rockets

    def get_rocket_details(self) -> str:
        # for rocket in self.Rockets:
        #     print(f"Name: {rocket.name} | Landing Method: {rocket.landing_method}")
        #
        #
        details: List[str] = []
        try:
            for rocket in self.rockets:
                details.append(f"Name: {rocket.name} | Landing method: {rocket.landing_method}")
            return "\n".join(details)
        except AttributeError:
            return "One or more rockets are missing required attributes"
        except TypeError:
            return "Invalid rocket object"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    def __repr__(self):
        return f"SpaceX has {len(self.rockets)} rockets"


class Rocket:
    def __init__(self, name, landing_method):
        self.name = name
        self.landing_method = landing_method


# startship = Rocket("Starship", "Drone Ship")
# falcon9 = Rocket("Falcon 9", "Ground")
# spacex = SpaceX(startship, falcon9)
# print(spacex)
# spacex = SpaceX()
# print(spacex.get_rocket_details())


rockets = [
    {"name": "Starship", "landing_method": "Drone Ship"},
    {"name": "Falcon 9", "landing_method": "Ground"},
    {"name": "Falcon Heavy", "landing_method": "Ground"},
    {"name": "Crew Dragon", "landing_method": "Drone Ship"}
]

try:
    if not rockets:
        raise ValueError("No rockets available")
    for rocket in rockets:
        name = rocket["name"]
        landing_method = rocket["landing_method"]
        print(f"Name: {name} | Landing method: {landing_method}")
except ValueError as e:
    print(e)
else:
    print("Rockets printed successfully")
finally:
    print("Rocket details retrieval completed")


numbers = [20, 3, 5, 6, 7, 8, 9, 10]
