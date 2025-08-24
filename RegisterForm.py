# Register Form

users = []  # store all registered users here

def register_user(name, email, password):
    user = {
        "name": name,
        "email": email,
        "password": password
    }
    users.append(user)
    return "User registered successfully!"
