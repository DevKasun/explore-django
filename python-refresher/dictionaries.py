import json

developers = {
    "Alex": "MERN",
    "Bob": "React + .NEt",
    "Charlie": "MEAN",
    "David": "React + Hono"
}


# print("-------- Developer Stacks --------")
# for developer_stacks in developers.values():
    # print(developer_stacks)

# print(" ")

# print("-------- Developers and their Stacks --------")
# for developer, developer_stacks in developers.items():
    # print(f"{developer} : {developer_stacks}")


settings = [
    {
        "theme": "Base16",
        "profile": "web dev"
    },
    {
        "font_size": 16,
        "font_family": "Fira Code",
    },
    {
        "terminal": "zsh",
        "terminal_font-size": 13,
        "terminal_font_family": "MesloLGL Nerd Font"
    }
]

settings[0]["theme"] = "Dracula"
# print(f"Current theme: {settings[0]["theme"]}")

for setting in settings:
    print(setting)

# Dictionary to JSON
json_string = json.dumps(settings)
# pretty json
json_formatted = json.dumps(settings, indent=4)

# print(json_formatted)
