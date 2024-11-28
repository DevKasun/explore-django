# Arbitrary Positional Arguments (*args)
# Collect multiple positional arguments

def sum_numbers(*args):
    return sum(args)

numbers = {1, 2, 3, 4, 5}
# print(sum_numbers(*numbers))

def add_nums(x, y):
    return x + y

nums = {"x": 15, "y": 25} #dictionary
# print(add_nums(nums["x"], nums["y"]))
# OR
# print(add_nums(**nums))

def calculator(*args, operator):
    if operator == "+":
        return sum(args)
    elif operator == "-":
        return args[0] - args[1]
    elif operator == "*":
        return args[0] * args[1]
    elif operator == "/":
        return args[0] / args[1]
    elif operator == "**":
        return args[0] ** args[1]
    else:
        return "Invalid operator"

# number_input_1 = input("Enter your first number: ")
# number_input_2 = input("Enter your second number: ")
# args = [int(number_input_1), int(number_input_2)]
# operator_input = input("Enter your operator(+, -, *, /): ")
# calculated_number = calculator(args, operator=operator_input)
# print(f"Result: {calculated_number}")


# Arbitrary Keyword Arguments (**kwargs)
# Collect multiple positional arguments

def display_full_name(**kwargs):
    return f"{kwargs['first_name']} {kwargs['last_name']}"

names = {"first_name": "John", "last_name": "Doe"}
print(display_full_name(**names))
