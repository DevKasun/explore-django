import re

def validate_input(func):
    def wrapper(x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Arguments must be numbers")
        return func(x, y)
    return wrapper

@validate_input
def divide(a, b):
    return a / b

# print(divide(10, 2))


def check_password(func):
    def wrapper(*args, **kwargs):
        password = args[2]
        regex_pattern = r'^(?=.*[A-Za-z])(?=.*\d).{8,}$'
        password_match = re.match(regex_pattern, password)
        if password_match:
            return func(*args, **kwargs)
        else:
            return False
    return wrapper

user_password = "awdawd12345678"

@check_password
def create_password(name, username, user_password):
    return name, username, True

print(create_password("Kasun Lakshitha", "example_username", user_password))
