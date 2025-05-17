import json
import os
import hashlib

USERS_FILE = "data/users.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

def authenticate(username, password):
    users = load_users()
    hashed = hash_password(password)
    user = users.get(username)
    if user and user["password"] == hashed:
        return user
    return None

def create_user(username, password, name, role):
    users = load_users()
    if username in users:
        return False  # already exists
    users[username] = {
        "name": name,
        "password": hash_password(password),
        "role": role
    }
    save_users(users)
    return True
