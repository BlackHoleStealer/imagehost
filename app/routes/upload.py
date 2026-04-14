from flask import request
import os, time

from app.utils.utils import generate_id
from app.utils.meta import add_upload
from config import DOMAIN, UPLOAD_FOLDER


def upload_route():
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    file = request.files["file"]
    preset_name = request.args.get("preset", "default")

    while True:
        file_id = generate_id(preset_name)
        file_name = file_id + ".png"
        path = os.path.join(UPLOAD_FOLDER, file_name)

        if not os.path.exists(path):
            break
    
    file.save(path)
    add_upload(file_id, "willow")

    return f"{DOMAIN}/view?id={file_id}"