# register form

users = []  # store all registered users here

def register_user(name, email, password):
    user = {
        "name": name,
        "email": email,
        "password": password
    }
    users.append(user)
    return "User registered successfully!"

def login_user(email, password):
    for user in users:
        if user["email"] == email and user["password"] == password:
            return f"Welcome back, {user['name']}!"
    return "Invalid email or password!"

