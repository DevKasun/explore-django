users = [
    (0, "Bob", "pswrd"),
    (1, "Alex", "123456"),
    (2, "Jack", "qwerty"),
    (3, "Mike", "bnmghgh"),
    (4, "Anne", "12334"),
    (5, "Jessie", "pwd123"),
]

username_mapping = {user[1]: user for user in users}
# print(username_mapping["Bob"])

def search_by_username(username):
    user_data = username_mapping.get(username)
    if user_data:
        return user_data
    return "Username not found"

username_input = input("Enter username: ")
result = search_by_username(username_input)
print(result)

print("------------------------------------------------------")

rockets_with_heights = [
    (0, "Starship", 121),
    (1, "Falcon 9", 70),
    (2, "Ariane 5", 50),
    (3, "Delta IV Heavy", 72),
    (4, "Atlas V", 58),
    (5, "Saturn V", 111),
    (6, "Falcon Heavy", 70)
]

rocket_mapping = {rockets_with_heights[1]: rocket for rocket in rockets_with_heights}

# rocket_name_input  = input("Enter rocket name: ")
# rocket_data = rocket_mapping.get(rocket_name_input)
