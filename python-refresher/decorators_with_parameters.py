def check_user_role(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if role in args[1]:
                return func(*args, **kwargs)
            return "Access denied ❌"
        return wrapper
    return decorator

@check_user_role("admin")
def add_user(user, roles):
    return f"{user} added successfully ✅"

@check_user_role("admin")
def delete_user(user, roles):
    return f"{user} deleted successfully ✅"


user = {"kasun", "user"}
print(delete_user("alex", user))
