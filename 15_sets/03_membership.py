allowed_users = {"Alice", "Bob", "David", "John"}

def check_user(allowed_users, username):
    if username in allowed_users:
        return "Access granted"
    else:
        return "Access denied"

print(check_user(allowed_users, "Tom"))