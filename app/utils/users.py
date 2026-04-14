USERS = {
    "7xsxd7": "Willow"
}

def get_user_by_key(key):
    for user_id, data in USERS.items():
        if data["key"] == key:
            return user_id, data
    return None, None