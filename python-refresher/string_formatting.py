user_name = "Alex Murcer"
welcome_message = f"Hi {user_name}, Welcome to Python Programming"
print(welcome_message)


# Or we can use this way
user_name_2 = "John Doe"
welcome_message_2 = "Hi {}, Welcome to Python Programming".format(user_name_2)
print(welcome_message_2)

# or this way
user_name_3 = "Bill Gates"
course_name = "Python Programming"
welcome_message_3 = "Hi {}, Welcome to {}"
welcome_message_with_name = welcome_message_3.format(user_name_3, course_name)
print(welcome_message_with_name)
