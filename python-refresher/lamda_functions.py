rockets_with_heights = [("Starship", 121), ("Falcon 9", 70), ("Ariane 5", 50), ("Delta IV Heavy", 72), ("Atlas V", 58), ("Saturn V", 111), ("Falcon Heavy", 70)]
sorted_by_height = sorted(rockets_with_heights, key=lambda rocket: rocket[1], reverse=True)

def show_tallest_to_shortest(rockets):
    for rocket in rockets:
        print(rocket[0])

show_tallest_to_shortest(sorted_by_height)


sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

double = lambda x: x * 2

print(list(map(double, sequence)))
