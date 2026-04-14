import json
import os

USERS_FILE = "app/data/users.json"

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    return {}

USERS = load_users()


def get_user(api_key: str):
    return USERS.get(api_key)