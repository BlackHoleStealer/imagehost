from flask import send_from_directory
import os

UPLOAD_FOLDER = "uploads"

def raw_route(file_id):
    return send_from_directory(os.path.abspath(UPLOAD_FOLDER), f"{file_id}.png")