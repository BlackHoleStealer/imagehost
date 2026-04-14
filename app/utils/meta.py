import json
import os
import time

META_FILE = "app/data/meta.json"

os.makedirs("app/data", exist_ok=True)


def load_meta():
    if os.path.exists(META_FILE):
        with open(META_FILE, "r") as f:
            try:
                return json.load(f)
            except:
                return {}
    return {}


def save_meta(meta):
    with open(META_FILE, "w") as f:
        json.dump(meta, f)


META = load_meta()


def add_upload(file_id: str, username: str):
    META[file_id] = {
        "username": username,
        "time": int(time.time())
    }
    save_meta(META)


def get_upload(file_id: str):
    return META.get(file_id)