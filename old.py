from flask import Flask, request, send_from_directory
from nanoid import generate
import os, uuid

DOMAIN = "http://127.0.0.1:8080"

PRESETS = {
    "default": "abcdefghijklmnopqrstuvwxyz0123456789",
    "emoji": "💀🥶☠️😈😭😢🥺😡🤬❤️🥵👿😔😎😂😤😨🤓🗣️👍❌"
}

def generate_id(preset:str) -> str:
    return generate(PRESETS[preset], 16)

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return "Yo im 1 high"

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    preset_name = request.args.get("preset", "default")

    while True:
        file_id = generate_id(preset_name)
        file_name = file_id + ".png"
        path = os.path.join(UPLOAD_FOLDER, file_name)

        if not os.path.exists(path):
            break
    
    file.save(path)

    return f"{DOMAIN}/view?id={file_id}"

@app.route("/i/<filename>")
def image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route("/view")
def view():
    file_id = request.args.get("id")
    filename = file_id + ".png"
    path = os.path.join(UPLOAD_FOLDER, filename)

    if not os.path.exists(path):
        return "Not found", 404
    
    user_agent = request.headers.get("User-Agent", "").lower()

    is_discord = "discord" in user_agent
    image_url = f"{DOMAIN}/i/{filename}"

    if is_discord:
        return f"""
        <html>
        <head>
            <meta property="og:title" content="Image">
            <meta property="og:image" content="{image_url}">
            <meta property="og:url" content="{DOMAIN}/view?id={file_id}">
        </head>
        <body></body>
        </html>
        """

    return send_from_directory(UPLOAD_FOLDER, file_id + ".png")

app.run(host="0.0.0.0", port=8080)