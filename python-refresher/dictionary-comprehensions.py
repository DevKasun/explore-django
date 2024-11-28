users = [
    (1, "Bob", "pswrd"),
    (2, "Alex", "123456"),
    (3, "Jack", "qwerty"),
    (4, "Mike", "bnmghgh"),
    (5, "Anne", "12334"),
    (6, "Jessie", "pwd123"),
]

username_mapping = {user[1]: user for user in users}
# print(username_mapping["Bob"])

def search_by_username(username):
    user_data = username_mapping.get(username)
    if user_data:
        return user_data
    return "Username not found ❌"

# username_input = input("> Enter username: ")
# result = search_by_username(username_input)
# print(f"> {result}")

# print("------------------------------------------------------")

rockets_with_heights = [
    (1, "Starship", "SpaceX", 121),
    (2, "Falcon 9", "SpaceX", 70),
    (3, "Ariane 5", "Arianespace", 50),
    (4, "Delta IV Heavy", "ULA", 72),
    (5, "Atlas V", "ULA", 58),
    (6, "Saturn V", "NASA", 111),
    (7, "Falcon Heavy", "SpaceX", 70)
]

rockets_map_by_company = {company[2] for company in rockets_with_heights}

print("List of space companies:")
for company in rockets_map_by_company:
    print(company)

def search_by_company(company):
    rockets = [rocket for rocket in rockets_with_heights if rocket[2] == company]
    return rockets


company_name_input = input("> Enter space company name: ")
result2 = search_by_company(company_name_input)

for rocket in result2:
    print(f"| Rocket name: {rocket[1]} | Height: {rocket[3]} |")
