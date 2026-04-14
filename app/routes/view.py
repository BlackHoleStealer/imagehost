import os, time
import datetime
from flask import request, send_from_directory
import random

from config import DOMAIN, UPLOAD_FOLDER
from app.utils.meta import get_upload

QUOTES = [
    "A genius admires simplicity",
    "love is a shitty concept",
    "Those who live in glass houses shouldn't throw stones",
    "image made by a chinese factory worker"
]

def get_random_quote():
    return random.choice(QUOTES)

def view_route():
    file_id = request.args.get("id")

    filename = f"{file_id}.png"
    path = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(path):
        return "Not found", 404

    user_agent = request.headers.get("User-Agent", "").lower()
    print(f"view_route hit")
    print(f"User Agent: {user_agent}\nIp Address: hackedez")
    is_discord = "discordbot" in user_agent

    image_url = f"{DOMAIN}/i/{file_id}"

    title = f"{file_id}.png"
    url = f"{DOMAIN}/view?id={file_id}"
    description = get_random_quote()

    meta = get_upload(file_id)
    username = meta["username"] if meta else "unknown"

    if is_discord:
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta property="og:type" content="website">
            <meta property="og:url" content="{url}">
            <meta property="og:image" content="{image_url}">
            <meta property="og:site_name" content="saintofwillow.online">
            <meta property="og:description" content="{description}">
            <meta property="og:image:width" content="1200">
            <meta property="og:image:height" content="630">

            <meta name="twitter:card" content="summary_large_image">
            <meta name="twitter:title" content="{filename}">
            <meta name="twitter:description" content="{description}">
            <meta name="twitter:image" content="{image_url}">
        </head>
        </html>
        """

    return send_from_directory(os.path.abspath(UPLOAD_FOLDER), filename)